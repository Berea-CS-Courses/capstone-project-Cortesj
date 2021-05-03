# Reflection 4
Jose Manuel Cortes

*04/30/2021*

---

1. What have you accomplished this week? (Please list each accomplishment, and explain)

    * Hardware

      I managed to fix the reconnection issue in which the hardware would be dropped from the network upon a network drop/reboot. I had implemented a function to check if network status was dropped or disconnected and to begin attempting a reconnection every 10 seconds till connection was established. All other functions would cease till connection was established. I also updated the comments on the C++ code to me transparent and descriptive of said code. I also moved around more user definable variables into a file called "settings.h" so if people can define network credentials, location/sensor number, etc... Testing has been successful so far and I believe hardware portion in my opinion to this point is complete for a initial release till more expansive setups could be created for further testing.

    * Database

      I cleared out the databases to continue testing with blank tables rather than constantly appending more current dummy data. I been working on cleaning up SQL files so I could use in a quick and easy setup file for the future. Most other things in terms of database is currently being handled by Python software since really just need to make queries for certain data or to remove/add entries.

    * Python Software

      I have been performing extensive streamlining of UI integration with my shift to grid formatting for tkinter and extensive testing for input of said UI windows. I implemented the inputs of all the create entry window and began working on view inventory window since that would be a bases for some other windows that require search functionalities. I have a scratch file with some view inventory concept prior to full class implementation

2. What challenges or difficulties did you face? If you solved them, how? If not, what have you learned so far? Have you sought help or other resources?
   
   Mostly learning how to use grid again since diffrent managers have diffrent requirements with their obvious pros and cons. I did my first iteration of UI with place which was good for prototyping but terrible for proper use.

3. What do you plan to accomplish in the following week? (Please list at least 3 concrete "S.M.A.R.T." goals, along with estimated number of hours to complete, or day to complete)
   
   * Database Class

     I again just want to further flesh out the functions in this class since I did implement a search function for both name and id but nothing else. Currently got it to take inventory database into a dataframe so it may be implemented into other aspect of the system. I think fleshing out would take around 3 hours to fully complete since mostly need to get UI to grab input so I can design function around said input.

   * UI Refreshing

     This components is still quite a troubling one since I need to get the graphs to update on the UI without some voodoo magic. I need to look into diffrent UI levels since I saw that you need to define the "level" on which it stays on a tkinter frame and run a function called after so periodically call a function to refresh said portion of a frame without exiting the main loop in some capacity. I do no know the exact timing this would take.

   * UI Retweaking
     
     I really wish to complete all the UI elements this week if possible but if no then I would like to get most major components involving its use of the database. I think it would take me around 6 hours to get all of the UI populated and properly functioning before I can begin the process of making it more user friendly. 

    

4. What resources will you use to accomplish your goals for the upcoming week? (please list out the resources)

    * Arduino Documentation (DHT22 & Wifi Libraries)
    * python3-mysql-connector documentation
    * tkinter documentation (For live graph update & Slave windows)
    * SQL Documentation (I use alot of tutorial point)
    * Coffee and a nap