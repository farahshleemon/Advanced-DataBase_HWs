import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
conn = MongoClient()
db = conn.Project
CrimeTable = db.CrimeTable
'''def get_items(status = -1):
    if (status >= 0):
        items = db.CrimeTable.find({"status": status})
    else:
        items = db.CrimeTable.find()
    return items'''
    
def new_item(obj):
   csv=[]
   csv.append(obj['Id'])
   csv.append(obj['In'])
   csv.append(obj['date'])
   csv.append(obj['Bo'])
   csv.append(obj['Iu'])
   csv.append(obj['Pt'])
   csv.append(obj['De'])
   csv.append(obj['Ld'])
   csv.append(obj['Ar'])
   csv.append(obj['Do'])
   csv.append(obj['Be'])
   csv.append(obj['Di'])
   csv.append(obj['Wa'])
   csv.append(obj['Co'])
   csv.append(obj['Fb'])
   csv.append(obj['X'])
   csv.append(obj['Y'])
   csv.append(obj['Ye'])
   csv.append(obj['Up'])
   csv.append(obj['Lat'])
   csv.append(obj['Lon'])
   csv.append(obj['Loc'])
   

   eid = db.CrimeTable.insert_one({'ID':csv[0], 'Case Number':csv[1],'Date':csv[2],'Block':csv[3],'IUCR':csv[4],'Primary Type':csv[5],'Description':csv[6],'Location Description':csv[7],'Arrest':csv[8],'Domestic':csv[9],'Beat':csv[10],'District':csv[11],'Ward':csv[12],'Community Area':csv[13],'FBI Code':csv[14],
                                    'X Coordinate':csv[15],'Y Coordinate':csv[16],'Year':csv[17],'Updated On':csv[18],'Latitude':csv[19],'Longitude':csv[20],'Location':csv[21]}).inserted_id
     
'''def get_item(id):
    item = items = db.CrimeTable.find_one({"_id": ObjectId(id)})
    return item'''

def update_item(obj,eid):
   csv=[]
   csv.append(obj['Id'])
   csv.append(obj['In'])
   csv.append(obj['date'])
   csv.append(obj['Bo'])
   csv.append(obj['Iu'])
   csv.append(obj['Pt'])
   csv.append(obj['De'])
   csv.append(obj['Ld'])
   csv.append(obj['Ar'])
   csv.append(obj['Do'])
   csv.append(obj['Be'])
   csv.append(obj['Di'])
   csv.append(obj['Wa'])
   csv.append(obj['Co'])
   csv.append(obj['Fb'])
   csv.append(obj['X'])
   csv.append(obj['Y'])
   csv.append(obj['Ye'])
   csv.append(obj['Up'])
   csv.append(obj['Lat'])
   csv.append(obj['Lon'])
   csv.append(obj['Loc'])    
   db.CrimeTable.update({'_id': ObjectId(eid)},{'$set':{'ID':csv[0], 'Case Number':csv[1],'Date':csv[2],'Block':csv[3],'IUCR':csv[4],'Primary Type':csv[5],'Description':csv[6],'Location Description':csv[7],'Arrest':csv[8],'Domestic':csv[9],'Beat':csv[10],'District':csv[11],'Ward':csv[12],'Community Area':csv[13],'FBI Code':csv[14],
                                    'X Coordinate':csv[15],'Y Coordinate':csv[16],'Year':csv[17],'Updated On':csv[18],'Latitude':csv[19],'Longitude':csv[20],'Location':csv[21]}})

def discard_item(obj):
   
   CN=obj['CN']
   print CN
   db.CrimeTable.remove({'Case Number': CN})
   print CN

def find_item(obj):
   CN1=obj['CN']
   print CN1
   c=db.CrimeTable.find_one({'Case Number': CN1})
   return c

def Number_of_Crimes_each_year():
   crimeDict={}
   for ye in range(2001,2015):
      stye=str(ye)
      count1=db.CrimeTable.find({"Year": stye}).count()
      crimeDict[str(ye)]=str(count1)
   return crimeDict

def queryByYear(Year):
   print Year
   result=db.CrimeTable.find({"Year":str(Year)}).limit(30)
   
   
   list=[]
   for doc in result:
      doc1={}
      for key in doc:
         if key == "_id":
            continue
         doc1[str(key)]=str(doc[key])
         
      list.append(doc1)
   return list      
           
   m=db.CrimeTable.find({"Year":str(Year)}).count(); 

def Number_of_Arrest_each_year():
   crimeDict1={}
   for ye in range(2001,2015):
      stye=str(ye)
      count1=db.CrimeTable.find({ "Year": stye, "Arrest": "true" }).count()
      crimeDict1[str(ye)]=str(count1)
      
   return crimeDict1  
   
if __name__ == "__main__":
   print ('-----')
   Number_of_Arrest_each_year()

   '''c=db.CrimeTable.count()
    for c in db.CrimeTable.find():
       print c'''
    
    
