# Green House Management Software 

Jose Manuel Cortes

*March 03, 2020*

---

General structure of program as of moment. There does appear to be small possible avenues of flexibility that I need to get ironed out soon. Mostly concerning connectivity of hardware since everything needs to be on a local network. I **DO NOT** intend to connect this to the internet in-case that keeps coming into question. General relation between items is quite evident but might need to be a tad more fleshed out. I hopefully can get some of the internals prototyped or atleast starting to see the potential issues/changes I will need to make.

---

## Structure 

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
    * System Settings | Interval checks/Storage limits

    > Note: Current plan is Desktop UI due to familiarity with tkinter module/language specifications.


* **Hardware Components | Simulation**
    * Microcontroller (Most likely some type of Arduino or Derivative[s]) 
    * Generic Thermal probe | LM35DZ (Promising model)
    * Generic Humditiy probe
    * Local network access (Possible access methods below)
        1. Bluetooth module
        2. Wifi module (Non-meshed method)
        3. Wifi Module (Mesh) | https://www.instructables.com/Simple-Arduino-Wireless-Mesh/ *Thanks Dr. Jones!

* **System Requirements**
    * Primary Language: Python
        * *Note: Best for current time span and easier workflow*
        > Note: C++ may be used depending on time or program performance (Stretch)* 
    * Primary programming platform : VSCode
        * Python Extension
        * Git Extension
        * Pip extensions (Package Manager)
    * Python Packages
        * Pandas
        * tkinter [https://docs.python.org/3/library/tkinter.html]
        * Matplotlib
        * OS
        * my-sql-pythonconnector [https://dev.mysql.com/downloads/connector/python/]
        * *Many items still under consideration*
    * Microcontroller IDE
        * **Arduino IDE** *(Most likely IDE)*
    * Planned currently for Linux/Windows
        * *Justification:* Mostly since both are my daily drivers and easiest to work with in-terms of OS. 

---
## Notes
* *Current* set priority | Internals/Database -> UI -> Hardware Components 
* Need to research specific hardware controllers and accompanying modules
* Simulated Data requried for prototype
    * Potential datasource [https://www.appropedia.org/Pachube] | Credit to Imma!
* UI Prototyping needs to be placed into consideration | figma.com
---