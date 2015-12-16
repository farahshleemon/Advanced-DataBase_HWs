import pymongo
from pymongo import MongoClient
import codecs
from bson.objectid import ObjectId
conn = MongoClient()
db = conn.Project
CrimeTable = db.CrimeTable
'''f = codecs.open('Crimes_-_2001_to_present.csv', encoding='utf-8')
next(f)
for line in f:
    line1=line.strip();
    csv=line1.split(',');
    eid = db.CrimeTable.insert_one({'ID':csv[0], 'Case Number':csv[1],'Date':csv[2],'Block':csv[3],'IUCR':csv[4],'Primary Type':csv[5],'Description':csv[6],'Location Description':csv[7],'Arrest':csv[8],'Domestic':csv[9],'Beat':csv[10],'District':csv[11],'Ward':csv[12],'Community Area':csv[13],'FBI Code':csv[14],
                                    'X Coordinate':csv[15],'Y Coordinate':csv[16],'Year':csv[17],'Updated On':csv[18],'Latitude':csv[19],'Longitude':csv[20],'Location':csv[21]}).inserted_id
    
'''    
print db.CrimeTable.count();
#db.CrimeTable.create_index([("Case Number", pymongo.ASCENDING)])
#db.CrimeTable.create_index([("Year", pymongo.ASCENDING)])
#db.CrimeTable.create_index([("Arrest", pymongo.ASCENDING)])

db.CrimeTable.create_index([
    ("Year", pymongo.ASCENDING),
    ("Arrest", pymongo.DESCENDING)
])
'''for ye in range(2001,2015):
    stye=str(ye)
    print db.CrimeTable.find({"Year": stye}).count()'''
