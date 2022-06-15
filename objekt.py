from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()
from datetime import date
from sqlalchemy import create_engine
import psycopg2
import json
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/covid')

Base = declarative_base()

class Statistika(Base):
    __tablename__="covid"
    id=Column(Integer, primary_key=True)
    Date=Column(String)
    Day=Column(Integer)
    Month=Column(Integer)
    Year=Column(Integer)
    Cases=Column(Integer)
    Deaths=Column(Integer)
    CountryTeritory=Column(String)
    GeoID=Column(String)
    TerritoryCode=Column(String)
    PopulationData=Column(String)
    Continent=Column(String)
    CumulNumber=Column(String)
    def __repr__(self):
        return f"Statistika(id={self.id!r}, Date={self.Date!r}, Day={self.Day!r}, Month={self.Month!r}, Year={self.Year!r}, Cases={self.Cases!r}, Deaths={self.Deaths!r}, CountryTeritory={self.CountryTeritory!r}, GeoID={self.GeoID!r}, TerritoryCode={self.TerritoryCode!r}, PopulationData={self.PopulationData!r}, Continent={self.Continent!r}, CumulNumber={self.CumulNumber!r}"

myjsonfile=open("statistika.json")
jsondata=myjsonfile.read()
obj=json.loads(jsondata)
list=obj["records"]

Base.metadata.create_all(engine)
with Session(engine) as session:
    for i in range(len(list)):
        irasas= Statistika(
            Date=(list[i].get("dateRep")),
            Day=(list[i].get("day")),
            Month=(list[i].get("month")),
            Year=(list[i].get("year")),
            Cases=(list[i].get("cases")),
            Deaths=(list[i].get("deaths")),
            CountryTeritory=(list[i].get("countriesAndTerritories")),
            GeoID=(list[i].get("geoId")),
            TerritoryCode=(list[i].get("countryterritoryCode")),
            PopulationData=(list[i].get("popData2019")),
            Continent=(list[i].get("continentExp")),
            CumulNumber=(list[i].get("Cumulative_number_for_14_days_of_COVID-19_cases_per_100000")))
        session.add_all([irasas])
    session.commit()

#conn = engine.connect()
#for i in range(len(list)):
    #date=(list[i].get("dateRep"))
    #day=(list[i].get("day"))
    #month=(list[i].get("month"))
    #year=(list[i].get("year"))
    #cases=(list[i].get("cases"))
    #deaths=(list[i].get("deaths"))
    #CounTer=(list[i].get("countriesAndTerritories"))
    #GeoID=(list[i].get("geoId"))
    #CTCode=(list[i].get("countryterritoryCode"))
    #PopData=(list[i].get("popData2019"))
    #ContExp=(list[i].get("continentExp"))
    #CumulNumber=(list[i].get("Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"))
    #ins = covid2.insert().values(Date=date, Day=day, Month=month, Year=year, Cases=cases, Deaths=deaths, CountryTerritory=CounTer, GeoID=GeoID, TerritoryCode=CTCode, PopulationData=PopData, Continent=ContExp, CumulNumber=CumulNumber)
    #conn.execute(ins)





    