# Reflection 5
Jose Manuel Cortes

*05/07/2021*

---

1. What have you accomplished this week? (Please list each accomplishment, and explain)


    * User Interface

      I currently have been able to connect Database functions to certain UI windows. The create entry and view inventory UI's have been nearly complete. They mostly require a check for the inputs as to make valid inputs and error handling. Furthermore, I got grid management pretty much up and running so UI creation is extremely streamlined in comparison to the previous weeks. I also created a multitude of buttons for many of the smaller "slave" UI windows that have actual functions and checks for certain inputs and so forth. I also cleaned up some of the UI code paticularly items that have many parameters so it was more human readable. I also been reformatting code to follow pep8 standards of Class & function formatting. I began making a scratch file to test out certain window configurations and functions so it would be easier to test certain UI elements/widgets as they get slowly implemented.

    * Backend

      Reformatted some of the code within the Database class to follow pep8 standards. Implemented a function to delete a Query depending on ID of plant from inventory. Most of this backend was clean up or implementing functions for certain button calls via the UI. The button would need to perform multiple functions and their commands can only be tried into one function so the solution is to create a function that executes a multitude of other functions. I finally also go refresh working for "View Inventory" whenever the database is modified via the program or deleted record.



2. What challenges or difficulties did you face? If you solved them, how? If not, what have you learned so far? Have you sought help or other resources?
   
   I believe my biggest issue this week so far was getting database to be viewed in my program since alot of other modules for displaying would create static tables that would accept a dataframe but nothing much beyond that. I had to implement a Treeview into tkinter to display a interactable table that rather accepting a straight dataframe needed to be itterated through to display the information appropriatly. Treeview was a blessing in disguse since now I can simply select the entry I want and a modify/edit window will open with appropriate information to modify. This will send appropriate information to DB and refresh inventory view as well. It was quite a learning experience and during entire process I ended up reading about multiprocessing/multi-threading, which could come in handy during further development.

3. What do you plan to accomplish in the following week? (Please list at least 3 concrete "S.M.A.R.T." goals, along with estimated number of hours to complete, or day to complete)
   
   * Database Class

     I need to implement try..except more into the functions or find more appropriate areas to implement those operators. That is mostly to handle errors such as disconnection or other general mySQL errors that it could throw for any number of reasons. I was reading more and more into the SQL module and there is a specific library made for MYSQL errors so there that the issue can be caught and dealt with appropriatly. I also need to implement same grab current sensor data functions since really I just need a grab data from X to X time span. I would need to import time and set the appropriate indexing of my sensor data both dummy and current functional data. I believe this should take me like 3 hours or so since mostly error catching and copy/past functions for diffrent DB/table.

   * UI Refreshing

     I didn't manage to get to this week beyond that of "View Inventory" with modifcation of current database. I have been reading quite a bit about multi-threading and multi-processing so I can run multiple functions within the same process. It doesn't seem paticularly difficult to start a thread and give it a function to execute. I need to see how friendly it would play with tkinter since I haven't done much in terms of multi-threading, expecially with Python. I think should take me around 6 hours to get something functional and I would hope for less since Python theorically is eaiser to work with than say C++ multi-threading.

   * UI Creation
     
    I wish to reorganize the Main UI window with grid and finally implement proper refesh graphics for the Main UI. The matplotlib is figure is already created so I might just need to have a continuous function to refresh the function/widget just like the section on "UI Refreshing" covered. I think this will be apart of the 6 hours of UI refreshing. Otherwise, any actual just normal UI work is gonna be like 2-3 hours since I managed to streamline it and more of a matter of tweaking exisiting code.
    
4. What resources will you use to accomplish your goals for the upcoming week? (please list out the resources)

    * Tkinter Docs
    * Matplotlib Docs
    * PythonThreading Docs
    * Ungodly amounts of Sleep