import sqlite3
from bottle import route, run, debug, template, request,error
from peewee import *
from datetime import date


db = SqliteDatabase('todo.db')

class Todo(Model):
    ID=IntegerField()
    status = BooleanField()
    task = CharField()

    class Meta:
        database = db



db.connect()

'''@route('/Model', method='GET')
def new_Modelitem():

    if request.GET.get('save','').strip():
        new = request.GET.get('task', '').strip()
        s=0
        Todo.create(task=new,status=s)
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')'''

@route('/model2')
def model_list2():
    query = Todo.select()
    result = []
    for todo in query:
        result.append((todo.id,todo.task,todo.status))
    output = template('model_list_view', rows=result)
    return output
   

@route('/model/<status:int>')
def model_list(status=0):
    query = Todo.select().where(Todo.status==status)
    result = []
    for todo in query:
        result.append((todo.id,todo.task,todo.status))
    output = template('model_list_view', rows=result)
    return output

@route('/')
@route('/todo/<status:int>')
def todo_list(status=-1):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    if (status >= 0):
       c.execute("SELECT id, task, status FROM todo WHERE status LIKE '"+str(status)+"'")
    else:
        c.execute("SELECT id, task, status FROM todo")
    result = c.fetchall()
    output = template('list_view', rows=result)
    return output

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    #return str(result)
    output = template('make_table', rows=result)
    return output

@route('/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

@route('/delete/<no:int>', method='GET')
def confirm_delete_item(no):
    return '''
        <form action="/delete/%s" method="post">
            <input value="Confirm deletion..." type="submit" />
        </form>
    ''' % no
@route('/delete/<no:int>', method='POST')
def delete_item(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id LIKE ?", (str(no)))
    conn.commit()
	
    return '<p>The new task was DELETED from the database, the ID was ' + str(no) + '</p>'



@error(404)
def mistake(code):
    return 'nothing here'
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run()
