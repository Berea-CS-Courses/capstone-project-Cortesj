# Reflection 6
Jose Manuel Cortes

*05/014/2021*

---

1. What have you accomplished this week? (Please list each accomplishment, and explain)


    * User Interface

      UI has been completely switched to utilizing Grid manager within Tkinter library. Futheremore, I have reorganized the main window and placed the appropriate spacing for the graphic widget. I also allowed resizing from the x-axis and changed the resoltion to better fit all the widgets and allow for an increased ease of use. Another major change was the live-updating graphs to display temperature/humidity from the sensor. It displays data from everyweek starting on Sunday. The refresh interval refresh is user definable as to either help with performance or upon a user's preference for update. Furthermore, I added a royalty-free icon to the program and populated the Settings UI with all appropriate elements and save functionality. 

    * Backend

      Performed another code clean up to remove any un-necessary imports and random bits of code that performed essentially nothing. I also updated code to follow the pep8 formatting to make it more human readable. Docstrings were added to the majority of all functions as to provide a brief description and define any parameters and return's uses. I added a function to save settings from the UI menu and implemented the use of settings.json into user definable fields found within the main UI class. I also updated some naming convention within the variables to keep it more consistant and make it a less confusing experience, if code is to be revisited. Function to grab current week's sensor data was also implemented as simply query that grabs today's date and then contructs a query asking for the week's data based on today's date. More backend details found within GIT.



2. What challenges or difficulties did you face? If you solved them, how? If not, what have you learned so far? Have you sought help or other resources?
   
   I think the most challenging was getting the refreshing graphics to function since my first intention was to utilize threading. I managed to find a built-in function within matplotlib that updates the graphics with a set interval. It handles all of it's own threading and memory. Hence, it made my inital issue trivial. Furthermore, I also began having issues with getting the current week's data and I attempted to grab the current week via Python, but then again remembered SQL had built-in functions to grab certain time-sensitive data without requiring external libraries or loops. Again, making a seemingly difficult or annoying task quite trivial.

3. What do you plan to accomplish in the following week? (Please list at least 3 concrete "S.M.A.R.T." goals, along with estimated number of hours to complete, or day to complete)
   
   * Reports

     I need to implement all the reporting functions and checks to see if "X" plant is not being kept in optimal condition. This I don't think should take long. I would say around 2-3 hours sometime in the weekend since I knew that area would involve simply threading for certain functions to periodically check if current temperature conflicts with anything in my inventory Database. Reports should just be a Tabular view as shown in 'View Inventory' and so isn't terribly difficult to implement.

   * Input Checks

     I need to implement checks to see if inputs to entry boxes are valid. That isn't difficult and more of a time confusing practice of implementing if statements to see if "X" input needs to be int, otherwise spit mean error box saying try again. I think this should not take more than 1 hour if I really sit down and do it.

   * Testing/Analysis
     
    My current plan is to do Unit Testing and Heuristic analysis with intended user. I think for Unit testing either I will create a testing script or implement a sort of debug mode that outputs to debug logs via the logging module. I built some portions of my program to be more testable than others, so we will see how this goes. Furthermore, I will be doing a Heuristic to exam all my UI and its potential pitfalls or current pitfalls. I will be in contact with main user so they can assist me during this process as they might have some great insight on potential further itterations. I think this should take around 6 hours since I really want to  give myself time to really get all this completed and solid. 
    
4. What resources will you use to accomplish your goals for the upcoming week? (please list out the resources)

    * Tkinter Docs
    * Matplotlib Docs
    * PythonThreading Docs
    * Ungodly amounts of Sleep