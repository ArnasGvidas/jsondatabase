from datetime import date
from itertools import count
import requests
import psycopg2
import json
from functools import reduce


def jsonopen(myjsonfile):
       
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        return obj["records"]


def unique(lists):
        
        array = [] 
        for i in range(len(lists)):
                if lists[i].get("countriesAndTerritories") not in array:
                        array.append(lists[i].get("countriesAndTerritories"))     
        return array
        
def compare(lists,array):
       
        for a in range(len(lists)):
                       
                        if lists[a].get("countriesAndTerritories")== array[i]:
                                values.append(lists[a].get("cases"))
                                
        return reduce(lambda x, y: x+y, values)
        




arrays=unique(jsonopen(open("statistika.json")))
for i in range(len(arrays)):
        values=[]
        print(arrays[i], "| CaseSum:", compare(jsonopen(open("statistika.json")),unique(jsonopen(open("statistika.json")))))
