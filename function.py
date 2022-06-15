from datetime import date
from itertools import count
import requests
import psycopg2
import json
from functools import reduce


def jsonopen(myjsonfile):
       
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        lists=obj["records"]
        return lists


def unique(lists):
        
        arrays = [] 
        for i in range(len(lists)):
                if lists[i].get("countriesAndTerritories") not in arrays:
                        arrays.append(lists[i].get("countriesAndTerritories"))     
        return arrays
        
def compare(lists):
       
        for a in range(len(lists)):
                       
                        if lists[a].get("countriesAndTerritories")== arrays[i]:
                                values.append(lists[a].get("cases"))
                                
        return reduce(lambda x, y: x+y, values)
        



myjsonfile=open("statistika.json")
lists=jsonopen(myjsonfile)
arrays=unique(lists)
for i in range(len(arrays)):
        values=[]
        print(arrays[i], "| CaseSum:", compare(lists))
        