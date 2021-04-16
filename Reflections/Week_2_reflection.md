# Reflection 2
Jose Manuel Cortes

*04/16/2021*

---

1. What have you accomplished this week? (Please list each accomplishment, and explain)

    * Restructure of Code
         
      I managed to reorganize all the existing demo code and removed all the accompanying files with old demo. Commented alot on newly rewritten/organized code so there is an explaination on exact specifics of said code. Current config class has been created with function to test of settings.json is missing. 

    * Hardware

      Arduino Nano arrived and was tested for any hardware faults since day it arrived it was raining when delieved. The DHT22 sensor got lost in shipping requiring the purcahse of another sensor that arrived barely as of the writing of this reflection. I have been playing around with the Arduio for quite a bit and got all the necessary libraries (WifiNINA & DHTxx Sensor) for intended use of hardware. Managed to get arduino connected to local network and assigned it a static IP via my router's built-in DCHP server. Currently working on code to get dummy data/sensor data to a test SQL database.

    * Database

      MySQL server currently running on local machine with user's (root, myphpadmin, arduino). The DB is bound to be only accepted by LOCALHOST at the moment. Created 3 internal DB's/Schemas for inventory, sensor data and testing. I got rough outline of how the tables need to be setup and what specifically will access what depending on task at hand. Because of need to keep IP's static I also setup a static DCHP ip on my local machine for ease of access. I have very basic scripts for DB setup on hand since I reset the entire DB due to some errors I caused during modification of certain server files.

2. What challenges or difficulties did you face? If you solved them, how? If not, what have you learned so far? Have you sought help or other resources?
   
   The most drastic challenge so far really came from the hardware software. I didn't get the sensor in time which delayed on I needed to setup some of the testing which would affect the communication of the Hardware to software. I got the sensor now so I get the play around with the invidual DHTxx library now. Database was confusing because need to dust off old SQL knowledge so I can manipulate the DB and create test queries for code and Hardware connections. Otherwise, everything else has been fine so far.

3. What do you plan to accomplish in the following week? (Please list at least 3 concrete "S.M.A.R.T." goals, along with estimated number of hours to complete, or day to complete)
   
   * Implement Database

     I want to move further along a get the database fully setup and implemented. I have the idea of dataflow and been successful in connection with Database from internal sources so matter of getting it all tested and see how to decrease some complexity with hardware. I don't know how long this will take since I might comeup with diffrent idea of how to work something out.

   * Hardware

     Get hardware up and running so it can set data to the DB so it can be parsed and used for functions within the python software. I want to get the ino file for the hardware compelted with all the datapins and proper output setup. I think this is quite feasable and only take a few hours since I have been itterating and testing thoughout the week.

   * UI Retweaking

     Same as the week before*
     Sort of a low priority at the moment since I think there is a better method I can show items in my rough UI. I think it will take around an hour or 2 to reformat and restructure some UI elements and backend.

4. What resources will you use to accomplish your goals for the upcoming week? (please list out the resources)

    * Arduino Documentation (DHT22 & Wifi Libraries)
    * python3-mysql-connector documentation
    * Massive amounts of time
    * Coffee and a nap