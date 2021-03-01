# Green House Management Software (DRAFT)

Jose Manuel Cortes
*February 25, 2020*

---

## Structure *(Current)* 

* **Inventory/Database**

    * SQL Server | mySQL Community
        * Greenhouse groups
        * Plant Inventory (Amount)
        * Store parameters/constraints of X plant
    * Data Manipulation
        * Create new Plant Entry
        * Delete Plant Entry
        * Modify contraints/parameters
        * Modify amount of X plant inventory
    * Data Storage
        * Timestamp incoming data from sensors
        * Store on local disk | (Looking for Viable Format | Potential CSV)
        * Storage limitations | Record per X day, Delete old data past X date, etc.
    * Data Analytics/Reports
        * Reports | time-sensitive interval, report abnormailities, possible recommmendations, provide data from time span
        *  Graphics of temp/humdity over time
        * Report issues | If plant conditions aren't meet


* **User Interface**
    * Report Views
        * Temp data for X interval
        * Humidity data for X interval
        * Suggestions
        * reporting periods of condition instability
    * Graphics of temperature/humidity *(Stretch)*
        * Line graph for Temp/Humidity
        * Display averages
    * Live temperature/humdity view *(Stretch)*
        * Cycle of avg. temp of each greenhouse 
    * Critical issue warnings | if X condition isn't meet during viewing program
    * Area for Data Manipuation *(In tandum with Internals)*


* **Hardware Components | Simulation**
    * Microcontroller (Most likely some type of Arduino or Derivative[s]) | Additional: Simulation substitute necessary
    * Generic Thermal probe 
    * Generic Humditiy probe


* **System Requirements**
    * Primary Language: Python
        * *Note: Best for current time span and easier workflow*
        * *Note: C++ may be used depending on time or program performance (Stretch)* 
    * Python Packages
        * Pandas
        * tkinter [https://docs.python.org/3/library/tkinter.html]
        * Matplotlib
        * OS
        * my-sql-pythonconnector [https://dev.mysql.com/downloads/connector/python/]
        * *Many items still under consideration*
    * Microcontroller IDE
        * ***Unknown***
    * Planned currently for Linux/Windows
        * *Justification:* Mostly since both are my daily drivers and easiest to work with in-terms of OS. 

---
## Notes
* Currently **NO** assumed priority has been created.
* Need to find specific hardware components to simulate
* Simulated Data requried for prototype
    * Potential datasource [https://www.appropedia.org/Pachube] | Credit to Imma!
* UI Prototyping needs to be placed into consideration