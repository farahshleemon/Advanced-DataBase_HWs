from pymongo import MongoClient
from bson.son import SON
db = MongoClient().zipsc
pipeline = [ { "$group": { "_id": "$state", "totalPop": { "$sum": "$pop" } } },{ "$match": { "totalPop": { "$gte": 10*1000*1000 } } }]
x=list(db.zipcode.aggregate(pipeline))
print x
pipeline2 = [{ "$group": { "_id": { "state": "$state", "city": "$city" }, "pop": { "$sum": "$pop" } } },{ "$group": { "_id": "$_id.state", "avgCityPop": { "$avg": "$pop" } } }] 
x2=list(db.zipcode.aggregate(pipeline2))
print x2
pipeline3 = [
   { "$group":
      {
        "_id": { "state": "$state", "city": "$city" },
        "pop": { "$sum": "$pop" }
      }
   },
   { "$sort": { "pop": 1 } },
   { "$group":
      {
        "_id" : "$_id.state",
        "biggestCity":  { "$last": "$_id.city" },
        "biggestPop":   { "$last": "$pop" },
        "smallestCity": { "$first": "$_id.city" },
        "smallestPop":  { "$first": "$pop" }
      }
   }]
x3=list(db.zipcode.aggregate(pipeline3))
print x3
