from collections import namedtuple
# We are building a city object consisting of a number of properties.

city = namedtuple('Town','name population cases hospital')  #This is the blueprint of how a city object should look like
talegaon = city('Talegaon','1,00,000',806,True)
lonavala = city('Lonavala','5,00,000',507,False)
#Display
print(talegaon)
print(lonavala)
#Iterable
print(talegaon[0])
print(lonavala[3])
#Dictionarable
print(lonavala._asdict())
for key,values in lonavala._asdict().items():
    print(key,values)
