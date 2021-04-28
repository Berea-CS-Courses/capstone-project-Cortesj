# Reflection 3
Jose Manuel Cortes

*04/23/2021*

---

1. What have you accomplished this week? (Please list each accomplishment, and explain)

    * Hardware

      Got the sensor/arduino to post data into the Database. How it performs this is by calling a php script on a local apache2 server I had and allowing the php script to essentially perform all the local connections and authentication for the arduino. It increases complexity but since direct modules doesn't seem to be working due to some authentication issues involving the module I have currently placed that module idea in the back burner. I feel like the apache2 server will be useful later on if I feel like updating the UI to a more intuitive UI based interface way down the line if I continue with said project. Furthermore, I have encountered a bug in which if the network disconnects the arduino makes no attempt to reconnect. This should be an easy fix since involves having a check to see current network status.

    * Database

      I have Database setup for one sensor and inventory and currently accepted data as intended. The python software can also create a proper connection and both enter and modify entries per my use case. I have given the tables all the proper settings for each datatype it is accepting. I will need to set it up to accept specific intervals. Otherwise, I think MYSQL server itself is done for most part and might make modifications as need be.

    * Python Software

      I began work on the database class with some functions to modify entries in inventory and add entries to inventory. I also began expirementing with the UI and found tkinter functions to create slave windows that won't close the main window Object. I managed to find some tutorials on live updating graphs with mathplotlib that I am still reading and testing out for future implementation.

2. What challenges or difficulties did you face? If you solved them, how? If not, what have you learned so far? Have you sought help or other resources?
   
   The hardware was the most difficult since the original SQL module I planned to utilize was having errors constantly. It would connect to the SQL itself but then error out with authentication despite creating new user with full wildcard permissions and host connection.

3. What do you plan to accomplish in the following week? (Please list at least 3 concrete "S.M.A.R.T." goals, along with estimated number of hours to complete, or day to complete)
   
   * Database Class

     I want to complete all the database class functions that interact with the database so it can be tied into the UI. I have the create entry and modify entry complete. I need to create functions to parse both Arduino data and inventory data for search and graphics etc. Currently also looking into error handling incase connection to database is lost or certain query couldn't be parsed correctly. I think it will take around a few hours or so to complete since mostly defining queries and handling potential errors such as connection or invalid query entries.

   * Hardware

     I need to work out the bugs involving reconnection to wireless network and clean up arduino code so it has comments and remove fluff from initial programming phase. I need to create a blank form/template so you can flash said arduino with unique ID's and credentials as need be. I also want to create a more direct guide to installing/flashing the software to said arduino software. I think it should only take me around 2 hours since really its just adding a new check and testing of multiple situations with my network.

   * UI Retweaking

     I want to work on improving the general looks of the UI and populate all the slave windows with appropriate inputs and functions for their buttons. An example is the create entry window getting all the input boxes with their appropriate checks so submit to the database case functions. I think this would take me the longest since I have to work on the database class in tandem with the UI development.I don't know the exact timing since I think I was to work on it at the same time as certain database classes.

    

4. What resources will you use to accomplish your goals for the upcoming week? (please list out the resources)

    * Arduino Documentation (DHT22 & Wifi Libraries)
    * python3-mysql-connector documentation
    * tkinter documentation (For live graph update & Slave windows)
    * SQL Documentation (I use alot of tutorial point)
    * Coffee and a nap