             
from bottle import route, run, template
from items import *
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/cntask')
def cntask():
    r=information();
    completed=r["Completed"]
    NotDone=r["NotDone"]
    return template('<h1>Completed : {{c}}</h1> !<br/><hr/><br/><h1>NotDone : {{NotDone}}</h1> !',c=completed, NotDone=NotDone)

run(host='localhost', port=8080)

