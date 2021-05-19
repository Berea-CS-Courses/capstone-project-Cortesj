# Deliverable 5: Testing Plan and Documentation

Jose Manuel Cortes

May 19, 2021

---

## Which tests do I plan to conduct?

I have planned to conduct Functional Tests and a Heuristic Analysis.

Functional Tests will test individual components of my software for a multitude of functions and classes found within my software package. I will then conduct tests that would combine all the tested individual components into their respective pipline/communication channel and test multiple cases.

A Heuristic Analysis will conduct severe analysis and critique of the User Interface. This will involve a Markup of the UI & annotation. Furthermore, analyzing any potential pitfalls of the User Interface might have in terms of usability, logistics or limitations imposed on functionality. This will also include a portion dedicated on the recommended solutions of said analysis.

## How they will be the most useful tests to ensure the success of my system?

Functional Tests will be a useful test due to the fact of my development method. I tend to build individual components then tie them in with other components. In this case, I build a database class meant to handle SQL Querys and connections. This would then be tied into a User Interface Class that would essentially be a top layer that utilizes the Database class by inputing specific paramaters into the Database class.

Heuristic Analysis will be useful since one of my aims towards this program was to make it easy as possible to utilize the software for the average user. I wanted to make it dead-simple if possible which requires a specific mind-set. The analysis would allow a massive  critique on potential pitfalls of current UI design, so changes could be made in the future as need be. This would eventually lead to further analysis by other user's once a viable version of the UI is created and tested by the creator.

## Testing Objectives

* **Database**
  
  I think the Database python code is a extremely critical component and built in such a way that really you can execute all DB commands alone. Although, you would have to declare an object first! How I intend to test the Database is to Connect to the DB via a test file and simply excecute a mutiltude of different situations into a test database and let it post specific exceptions or passes depending on what I decide to use as input.

* **UI Elements**
  
  This is more difficult to display but I theoretically should be able to call every Window individually and they should function as intended. To showcase functionality I will post small GIFs displaying system functionality. Example being if I click X button does it open/perform X function.

---
## Functional Testing

For functional testing I broke it down mostly to Database functions requiring individual testing as UI testing is mostly a mixture of both individual testing and implemented testing.

* **Unit Testing**
    
    Database Test File Output. The test_db.py can be found within github repository. This tests multiple functions and their expected output given X parameters. It outlines the function with specific actions made. Along with expected output of success or failure depending on the use case. For individual functional tests this is fine but problems arise with integration since there is no checks on input and not all functions have appropriate exceptions.
  ```
    Database Connection (Valid Creds):
    Expected: Success
    Connection Success!

    Database Connection (Invalid Database):
    Expected: Does not Exist
    Database does not exist!

    Database Insert Plant (Valid):
    Expected: Function Passed
    Connection Success!
    Function Passed

    New Plant (Only Name)
    Expected: Function Passed
    Function Passed

    New Plant (No Name)
    Expected: Function Failed
    Function Failed

    New Plant (STR given to INT Param)
    Expected: Function Failed
    Function Failed

    Update Plant (Valid)
    Expected: Function Passed
    ERROR
    Function Passed

    Update Plant (STRING in INT/FLOAT Param)
    Expected: Function Failed
    ERROR
    Function Passed

    Grab Inventory
    Expected Output: Dataframe
    <class 'pandas.core.frame.DataFrame'>
                    name                                        description  stock  temp_min  temp_max  hum_min  hum_max
    id                                                                                                                   
    1        Creeping Fig  The creeping fig is an evergreen climbing spec...      6      55.0      75.0     50.0     85.0
    2   Beach Spider Lily  The Beach Spider Lily demands a large growing ...      7      40.0      90.0     40.0     90.0
    3          Calla Lily  Growing from a single rhizome, or bulb, this p...     54      55.0      75.0     30.0     80.0
    4    Christmas Cactus  The parent plant of the Christmas Cactus (this...      9      55.0      70.0     30.0     70.0
    8   Chinese Evergreen  There are many hybrid varieties of the Chinese...     19      60.0      80.0     30.0     90.0

    Week's worth of Sensor Data:
    Expected Output: Dataframe
    Connection Success!
    <class 'pandas.core.frame.DataFrame'>
                        temperature  humidity
    2021-05-16 00:00:06        70.52      69.7
    2021-05-16 00:00:16        70.52      69.7
    2021-05-16 00:00:27        70.52      69.6
    2021-05-16 00:00:37        70.52      69.7
    2021-05-16 00:00:48        70.52      69.7
  ```


* **Integration Testing**

A showcase of button functionality of the Main Window and it's subsequent opening of all Windows. This includes windows currently completed and that of unfinished windows.
![](https://i.imgur.com/bhYgauo.gif)

Showcase of a known issue that doesn't check for duplicate windows within any given UI instance.
![](https://i.imgur.com/uTcYnof.gif)

Visual showcase's test inventory manipulation by opening the Database, clicking a entry to modify and showcasing the subsequent change to Database.

Furthermore, it also shows the removal of a random entry and its subsequent change to the Database.

![](https://drive.google.com/uc?export=view&id=1xrTsFTBtVv8zyNvjvOi-Hg8LUVNluDou)

Lastly, a testing of inserting a new inventory entry into the Database.

![](https://drive.google.com/uc?export=view&id=1gHECFzcm8eglTFcU4xD19al7n4CimdQe)

* **Reflection & Interpretation**

   Currently the most noticable bug is the seemingly infinite windows as documented within Integrated testing. I didn't get to test everything I initially thought I could since how certain functions were integrated or because lack of development time. In terms of actual functionality, Everything else seemed to work as intended and didn't run into anything I would call unexpected. I think what happens mostly is I get inconsistant on where I implement certain functions making it more difficult to test at this current stage. I think one of my major difficulties will be seeing where to implement what. Do I implement checks in Database class or the UI class or make an entire class on its own to check input of certain items for certain functions.

   I know I can do massive improvements to both the Database and UI as a whole. One of the major planned features that I haven't managed to start was input checks. For example, there is no check to see if stock is actually a integer so if you input a string or float the UI will act as if Query was posted and self-terminate. Although, the backend of the Database class rejected the Query since it couldn't even process it and simply output's a string into console saying "Error". The UI also needs more rework obviously since formatting can always be improved and again the check for multiple window instances. There also should be more Confirm or yes/no dialog boxes for errors and confirmations as to protect the database from any potential harm. 

   Otherwise, I wanted to see how to test hardware functionality but couldn't think of an appropriate way of testing that. All the hardware does is connect to a network and post data into a database.

---

## Heuristic Analysis

### Marked up Windows/Pages
1. Main Window
![](https://i.imgur.com/fSKeK0t.jpg)
2. Add Inventory Window
![](https://i.imgur.com/apvsjbz.jpg)
3. Settings Window
![](https://i.imgur.com/CLrg7ZU.jpg)
4. View Inventory Window
![](https://i.imgur.com/QFxNtVf.jpg)
5. Modify Entry Window
![](https://i.imgur.com/B21k40N.jpg)

### Analysis of User Interface
![](https://i.imgur.com/ivzh3qC.png)
![](https://i.imgur.com/J9rp3qF.png)

### Reccomended Solutions
Solutions for each individual problem that I have so far identified are listed alongside the critique and indidual severity rating. It appears alot of the problems I have identified is mostly backend related issues that also require some form of communication to the user. 

An example being if I wanted to create a new inventory item and input "A" into the Stock input it should have a backend check to see if the input is an integer then report back a small dialog box or highlight the inputbox red to signify some type of error. I think that would be general solution for many of issues involving input boxes.

Futhermore, I would also need to have some updating of cosmetics and formatting of windows. Alot of small issues such as no destinctive units on Temperature and Humidity make it profoundly confusing to the user. The Main window also doesn't have best formatting in-terms of coloring of buttons/text along with graphs being unncessarily busy for the home window. I would probably have to change alot of overall UI in the program to make them consistent as well. Graphs require alot more thinking since it would be nice to give more of a general/minimalistic view as well as have some clear indication that say if you click the graph it would open or rerender it to have more detail. 

In my opinion, if I decide to further develop from this stage on. I might consider using a web UI  due to some other promising features I wanted to test out. There is also the option of me making this a sort of Admin or local UI incase their was ever some networking issues. That is if I decide to further pursue this specific version of the project.

### Reflection
![](https://i.imgur.com/RFB7oC4.png)

Again, mostly alot of backend checks and being able to present information to the user effectively. I included some issues about cosmetics and reformatting UI, but at this point of time it's expected to still be quite rough but I think this analysis really put into perspective all the potential pitfalls.

This definitly make my eyes open up on how difficult it is to design free-end. I have been more experienced with back-end and so UI design was never something I really had to focus on beyond straight functionality. This helps in the fact that I want to continue some form of this project in the near future and has me thinking already of how I can design such a UI. This could be either remaking UI in entire a new toolset or seeing what I can change with what I have now and go from there. This definitly gave me quite a bit of insight into the mind of a user and made me question alot of previous design decisions.

In conclusion, front-end is hard.