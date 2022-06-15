from datetime import date
import requests
import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    database="covid",
    user="postgres",
    password="postgres")

mycursor = conn.cursor()
# mycursor.execute("CREATE TABLE CovidOG (id serial PRIMARY KEY, Date VARCHAR(255), Day INT, Month INT, Year INT, Cases INT, Deaths INT, CountryTerritory VARCHAR(255), GeoID VARCHAR(255), TerritoryCode VARCHAR(255), PopulationData INT, Continent VARCHAR(255), CumulNumber VARCHAR(255))")

myjsonfile=open("statistika.json")
jsondata=myjsonfile.read()
obj=json.loads(jsondata)
list=obj["records"]
sqls= "SELECT countryterritory, sum(Cases) AS TOTAL_SCORE FROM covidog group by countryterritory order by countryterritory asc;"
# for i in range(len(list)):
#     date=(list[i].get("dateRep"))
#     day=(list[i].get("day"))
#     month=(list[i].get("month"))
#     year=(list[i].get("year"))
#     cases=(list[i].get("cases"))
#     deaths=(list[i].get("deaths"))
#     CounTer=(list[i].get("countriesAndTerritories"))
#     GeoID=(list[i].get("geoId"))
#     CTCode=(list[i].get("countryterritoryCode"))
#     PopData=(list[i].get("popData2019"))
#     ContExp=(list[i].get("continentExp"))
#     CumulNumber=(list[i].get("Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"))
#     sql = "INSERT INTO CovidOG (Date,Day,Month,Year,Cases,Deaths,CountryTerritory,GeoID,TerritoryCode,PopulationData,Continent,CumulNumber) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     var = (date,day,month,year,cases,deaths,CounTer,GeoID,CTCode,PopData,ContExp,CumulNumber)
mycursor.execute(sqls)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)





conn.commit()
conn.close()

    