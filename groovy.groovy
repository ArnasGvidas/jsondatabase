package projektas
import groovy.sql.Sql
import groovy.json.JsonSlurper
import groovy.transform.CompileStatic

import javax.xml.soap.Text
import java.sql.Connection
import java.sql.DriverManager
import java.sql.PreparedStatement
import java.sql.SQLException
import java.sql.Statement

class App2 {


    static void main(String[] args) {
        println("Start")
        println(new Date())

        int batchSize = 20;

        // def dbUrl = "jdbc:postgresql://localhost/covid"
        // def dbUser = "postgres"
        // def dbPassword = "postgres"
        //   def dbDriver = "org.postgresql.Driver"

        //def sql = Sql.newInstance(dbUrl, dbUser, dbPassword, dbDriver)

        try(Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost/covid", "postgres", "postgres");
            Statement stmt = conn.createStatement();
        ) {
            // Execute a query
            //sql.execute(sqlstr);
            conn.setAutoCommit(false)
            File inputFile = new File("C:\\Users\\daiva\\projektas\\app\\src\\statistika.json")
            JsonSlurper json = new JsonSlurper()
            Object result = json.parseText(inputFile.text)

            System.out.println("JSON Parsed...");
            println(new Date())

            println(new Date())
            int dydis = result.records.size()
            println(dydis)

            System.out.println("Starting insert records into the table...");
            println(new Date())
            String sql2 = "INSERT INTO covid2(date,day,month,year,cases,deaths,countryterritory,geoid,territorycode,populationdata,continent,cumulnumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
            //def sql = 'INSERT INTO covid2(cases) VALUES (?);'

            //sql = 'INSERT INTO covid2(cases) VALUES (?);'
            PreparedStatement ps = conn.prepareStatement(sql2)
            for(int i = 0;i<dydis;i++) {

                String date = result.records[i].dateRep
                String day = result.records[i].day
                String month = result.records[i].month
                String year = result.records[i].year
                Integer cases = result.records[i].cases
                Integer deaths = result.records[i].deaths
                String countryterritory = result.records[i].countriesAndTerritories
                String geoid = result.records[i].geoId
                String territorycode = result.records[i].countryterritoryCode
                Integer populationdata = result.records[i].popData2019
                String continent = result.records[i].continentExp
                String cumulnumber = result.records[i].Cumulative_number_for_14_days_of_COVID19_cases_per_100000



                ps.setString (1,date);
                ps.setString (2,day);
                ps.setString (3,month);
                ps.setString (4,year);
                ps.setInt (5,cases ?: 0);
                ps.setInt (6,deaths ?: 0);
                ps.setString (7,countryterritory);
                ps.setString (8,geoid);
                ps.setString (9,territorycode);
                ps.setInt (10,populationdata ?: 0);
                ps.setString (11,continent);
                ps.setString (12,cumulnumber);




                ps.addBatch();

                if (i % batchSize == 0) {
                    ps.executeBatch();

                }

                //ps.executeUpdate()

            }
            ps.executeBatch();
            conn.commit()
            conn.close()
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println("Inserted records into the table...");
        println(new Date())


    }

}
