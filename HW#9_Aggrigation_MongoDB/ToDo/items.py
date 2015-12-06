import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON
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

def information():
    result={};
    pipeline =  [
      { "$match": { "status": { "$eq": 1 } } },{ "$group": { "_id": "null", "Completed": { "$sum": 1 } } }
      
   ]
    x=list(db.tasktable.aggregate(pipeline))
    print "Completed: ",x[0]["Completed"]
    result["Completed"]=x[0]["Completed"]
    pipeline2 =  [
      { "$match": { "status": { "$eq": 0 } } },{ "$group": { "_id": "null", "NotDone": { "$sum": 1 } } }
      
   ]
    x1=list(db.tasktable.aggregate(pipeline2))
    print "Not Done : ",x1[0]["NotDone"]
    result["NotDone"]=x1[0]["NotDone"]
    return result;
if __name__ == "__main__":
    '''new_item("Do your Homework9",1)
    new_item("Do ToDo App",1)
    new_item("Do mongoImport",1)
    new_item("Do example in mongo shell",1)
    new_item("Do example in python",1)
    new_item("Do your work for research",0)
    new_item("Go to walmart",0)
    new_item("Prepare the lab guide",0)
    new_item("Do map reduce stuff",0)
    new_item("work on final project",0)'''
    '''items = get_items(-1)
    for item in items:
        print (item)'''
    '''r=information()
    print r'''
    print ('-----')
    
    
