# Deliverable 4: Midterm Documentation

Jose Manuel Cortes

March 24, 2021

---

## Proof of Concept

![](https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-Cortesj/Deliverable-4/Deliverables/D4_Images/ROUGH_GUI.jpg)

*Rough GUI with non-functional buttons and emmended graphs from example data*


![](https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-Cortesj/Deliverable-4/Deliverables/D4_Images/DEV_ENVIORMENT.jpg)

*View of Development enviorment with snapshot of WIP code*

![](https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-Cortesj/Deliverable-4/Deliverables/D4_Images/ROUGH_STRUCTURE.jpg)

*Extremely Rough outline of some files and their sturcture*

![](https://raw.githubusercontent.com/Berea-CS-Courses/capstone-project-Cortesj/Deliverable-4/Deliverables/D4_Images/CSV_EXAMPLE.jpg)

*View of dummy data CSV and I expect to have it formatted*

---
## Concept Documentation

1. *What external software or tools are needed to run your proof-of-concept?*

    Current proof-of-concept has dependencies mostly pertaining to Python. Specifically, Python3 (Version 3.8+ | Current) with external modules of tkinter/tcl and python3-mysql-connector. The main skew that I am currently working on runs theoretically on most Unix/Linux kernel based operating systems. Proof-of-concept would need access to a Local Area Network (LAN) to communicate to a SQL database and Arduinos with temperature and humidity sensors. SQL database will be using mysql-server (8+ | Community Edition) as it's main intended SQL database. In terms of Integrated Development Enviorment (IDE), I am using VSCode with Python, pythonlinter, and various other extensions. Arduino IDE would need to be utilized once hardware is obtained.

    **List View**
    * Linux/Unix Operating System
    * Python3 (3.8+ | Current version being built upon)
    * Visual Studio Code (VSCode)
      * Python Extension
      * Jupyter Notebook
      * Markdown All in One
    * Arduino IDE
    * Python Packages
      * Tkinter/Tcl
      * matplotlib
      * OS
      * panadas
      * pip3 (Package Manager)
      * python3-mysql-connector
    * MySQL Server (8+) | Community Edition
    * LAN Access/Router Access
    * Arduino Board
      * Temperature Sensor(s)
      * Humidity Sensor(s)
      * Modem(Extremely dependent on board)
    * Bash Scripting | Execution of Python/Setup


2. *What would need to be taken to run your proof-of-concept?*

    For the moment Python3 and all its accompanying modules listed above. Futheremore, the operating system it is running on is a Debian based Linux. From how it appears the GUI took priority over complete backend development since there needed to be a centeral hub to connect the various functions and give a launching platform for said various functions.

3. *What is current functionality of the proof of concept as you have submitted?*

    Current functionality has a rough approximation GUI shown within previous documentation and has extremely barebone stucture of certain files and classes I will be implemented. Currently GUI is most functional unit and setup of mysql-server is still in progress. Settings functions is also in works for SQL connection and interval timing. There is a onetime snapshot of how a CSV of data would be read into the software and displayed on main GUI. Formatting for said graphs are nowhere near complete.

4. *Are there any components of the code or systems you have submitted that you did not create? If so, document them here alongside their source or reference?*

    I primarily based alot of the current demo/proof-of-concept code on reference material and portion of matplotlib embedded example. I mostly been using previous assignment code as reference for GUI and class creation. 

   * Matplotlib embedded within Tkinter | https://datatofish.com/matplotlib-charts-tkinter-gui/
   * Tkinter Documenation | https://tkdocs.com/tutorial/index.html
   * python3-mysql-connector | https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html


## Updates

There has been no radical changes to the project mostly the development of more detail. Settings being an ini file for simple configuration of certain aspects of program is perhaps the biggest update on new details. Futhermore, current thinking is having a seperate json/ini file to specify grouping of Greenhouses and companying IPs to ping for data. Futhermore, using said file to generate any SQL entries involving Greenhouses. That is current thought but is still to see a type of implentation. 

There would be more updates as we enter full development of said projects and view the limitations of languages or current time crunch.

## Reflection
1. How confident do you feel about your project now that you have created a working proof-of-concept?
    
    I am feeling farely confident as I slowly begin development of a proof-of-concept. Python is farily easy to work with and yet has a set complexity to it if you dig enough into it. I wanted to do it with C++ from very beginning to gain a better handling of the language but I do not think this would be the best place to attempt to do so. I feel though most of my trouble will come from networking to Hardware sensors requesting data and probably error exceptions/handlers. Otherwise, I think it will turn out well and excited to see how far I can get with this project.

2. Have you faced any significant challenges in the creation of your project so far? If so, what are they?

    Probably mostly getting certain modules to function since my first attempt on getting python3 to coperate ended in a 2 hour session of backing up my OS and resetting the entire system. Otherwise, I haven't gotten suck in any paticular thing mostly after a good bit of reading reference material or seeing examples I am able to overcome most of the small issues I had.

3. What do you need from instructors and teaching assistants to better help you implement, understand, or otherwise think about your project?
   
   I really do not know. I am fairly independent and so have a terrible habit of not asking for anything. Otherwise, I think the constant small check-ins is good since forces one to finally speak one's ideas or thoughts. I am sure if I have any serious problems I will have questons.  