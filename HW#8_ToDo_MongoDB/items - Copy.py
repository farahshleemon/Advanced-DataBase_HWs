import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
conn = MongoClient()
db = conn.todo
tasktable = db.tasktable
def get_items(status = -1):
    if (status >= 0):
        items = db.tasktable.find({"status": status})
    else:
        items = db.tasktable.find()
    return items
    
def new_item(task, status):
   eid = db.tasktable.insert_one({'task': task, 'status': status}).inserted_id
    
    
def get_item(id):
    item = items = db.tasktable.find_one({"_id": ObjectId(id)})
    return item

def save_item(item):
    eid = item['_id']
    db.tasktable.update({'_id': ObjectId(eid)},{'$set':{'task':item['task'],'status':item['status']}})
def discard_item(id):
    eid = ObjectId(id)
    db.tasktable.remove({'_id': eid})

if __name__ == "__main__":
    new_item("Do your Homework",0)
    new_item("Do your project",1)
    items = get_items(-1)
    for item in items:
        print (item)
    print ('-----')
    
    
