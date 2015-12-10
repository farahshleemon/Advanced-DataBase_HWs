from mapreduce import MapReduce
#----------------------------------------
AlphaLetters=["A","B","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
class CharCount(MapReduce):
    def mapper(self, _, line):
        global AlphaLetters;
        for char in line:
            if char not in AlphaLetters:
                continue         
            ch=char.upper()
            yield (ch,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

#----------------------------------------
#main code
print "This code have been created by Farah Kamw for HW#10 for map reduce"
print "------------------------------------------------------------------"
input = open("alice.txt").readlines()
output = CharCount.run(input)
for item in output:
    print item

