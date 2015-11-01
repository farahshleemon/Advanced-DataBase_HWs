import sqlite3
import time
import matplotlib.pyplot as plt
import statistics

 

sqliteFile="chinook.db"
db = sqlite3.connect(sqliteFile)
# Get a cursor object
crs = db.cursor()
print "Tables Name"
# Query 0A:this is to show all the tables on the chinook.db
for r in crs.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print r[0]
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Quert 0B:this is to show all indexes on Album,Artist,track tables in  chinook database
print"=================================================================================================="
print "IndexesName"
indexesNames=["sqlite_autoindex_PlaylistTrack_1"]
for r in crs.execute("SELECT name FROM sqlite_master WHERE type == 'index'"):
    print r[0];
print 
# I dropped these indexes    
crs.execute("Drop INDEX IF EXISTS IFK_AlbumArtistId");
crs.execute("Drop INDEX IF EXISTS IFK_TrackAlbumId");
crs.execute("Drop INDEX IF EXISTS FFK_TrackAlbumId");
crs.execute("Drop INDEX IF EXISTS FEEK_TrackAlbumId");
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Query1:this is to see the result of joining three tables without query optimization 
print"=================================================================================================="
time_start = time.clock()
rows=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId ORDER BY Track.TrackId ASC;" )
print "time of the first query with more than 3000 itemes: ",(time.clock() - time_start)

# print and count the items in the query
count=0;
for r in rows:
    #print r
    count+=1;
print "Number of items in the first query is:",count;

#check the query plan
crs.execute("EXPLAIN QUERY PLAN SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId ORDER BY Track.TrackId ASC;" )
print (crs.fetchall())
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print"=================================================================================================="
#Query2:this is to filter the result of joining three tables to ten items without query optimization
time_start = time.clock()
rows1=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print "time of the second query 10 items without optimization : ",(time.clock() - time_start)
# print and count the items in the query
count1=0;
for r in rows1:
    #print r
    count1+=1;
print "Number of items in the second qyery is:",count1;

crs.execute("EXPLAIN QUERY PLAN SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print (crs.fetchall())

AverageTime1=0
Query1Time=[]
for i in range(0,100):
    time_start1 = time.clock()
    rows1=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
    #print "time of the second query : ",(time.clock() - time_start1)
    ComputationTime1=(time.clock() - time_start1);
    AverageTime1+=ComputationTime1;
    Query1Time.append(ComputationTime1);


print "The Average time for 100 queries without optimization is: ",AverageTime1/100;
print "The standared deviation of the time for 100 queries without optimization is: ",statistics.stdev(Query1Time);





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#(First Optimization : index with single coloumn)
# create index on table Album (ArtistId),and create index on table Track(AlbumId)
crs.execute("CREATE INDEX IFK_AlbumArtistId  ON Album(ArtistId);")
crs.execute("CREATE INDEX IFK_TrackAlbumId ON Track(AlbumId);")


print"=================================================================================================="

#Query2:this is to filter the result of joining three tables to ten items with query optimization 

time_start3 = time.clock()
rows1=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print "time of the second query with single column indexes: ",(time.clock() - time_start3)

crs.execute("EXPLAIN QUERY PLAN SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print (crs.fetchall())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#(Second Optimization : index with multiple coloumns)
# create index on table Track(AlbumId,Name)

crs.execute("CREATE INDEX FFK_TrackAlbumId ON Track(AlbumId,Name);")

print"=================================================================================================="


#Query2:this is to filter the result of joining three tables to ten items with query optimization 

time_start4 = time.clock()
rows1=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print "time of the second query with multiple columns indexes : ",(time.clock() - time_start4)

crs.execute("EXPLAIN QUERY PLAN SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
print (crs.fetchall())



AverageTime2=0
Query2Time=[]
for i in range(0,100):
    time_start2 = time.clock()
    rows2=crs.execute("SELECT TrackId,Track.Name,Album.AlbumId,Artist.Name from Track,Album,Artist WHERE Track.AlbumId=Album.AlbumId and Album.ArtistId=Artist.ArtistId and Album.ArtistId<11 GROUP BY Album.ArtistId ORDER BY Track.TrackId   ASC;" )
    #print "time of the second query : ",(time.clock() - time_start2)
    ComputationTime2=(time.clock() - time_start2);
    AverageTime2+=ComputationTime2;
    Query2Time.append(ComputationTime2);


print "The Average time for 100 queries without optimization is: ",AverageTime2/100;
print "The standared deviation of the time for 100 queries without optimization is: ",statistics.stdev(Query2Time);



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
db.close()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# plot Multiline graph to show the query optimization
#create some data
x_series = []
for i in range(0,100):
    x_series.append(i)

#plot the two lines

plt.figure()
plt.xlabel("Queries")
plt.ylabel("Computation time")
plt.title("Query Optimization Line Graph")
plt.ylim((0,0.01))
plt.plot(x_series, Query1Time, label="Query Without indexes")
plt.plot(x_series, Query2Time, label="Query With indexes")
 
plt.legend(loc="upper left")

plt.savefig("LineGraphQuery.png")
print "please see LineGraph.png for the visualization"
