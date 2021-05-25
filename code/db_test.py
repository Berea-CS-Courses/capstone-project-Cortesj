# ##################################Imports################################## #
from database import *
from config import *
from graphic_interface import *
# ########################################################################### #

# #############################Database Test################################# #

# Valid Database Test
print("\nDatabase Connection (Valid Creds):")
print("Expected: Success")
DB_Obj = Database(
    user='root',
    password='root',
    host='localhost',
    port='8080',
    database='inventory'
)

DB_Obj.connect()

# Invalid Database Test
print("\nDatabase Connection (Invalid Database):")
print("Expected: Does not Exist")
DB_Obj = Database(
    user='root',
    password='root',
    host='localhost',
    port='8080',
    database='Junk111111111'
)

DB_Obj.connect()


# New Plant Test
print("\nDatabase Insert Plant (Valid):")
print("Expected: Function Passed")
DB_Obj = Database(
    user='root',
    password='root',
    host='localhost',
    port='8080',
    database='inventory'
)

DB_Obj.connect()

try:
    DB_Obj.new_plant(
        name="Test Plant",
        desc="Test Desc",
        stock=100,
        temp_min=50,
        temp_max=100,
        hum_min=50,
        hum_max=100
    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")


# New Plant (Only Name)
print("\nNew Plant (Only Name)")
print("Expected: Function Passed")
try:
    DB_Obj.new_plant(
        name="Name Alone",
    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")


# New Plant (No name parameter)
print("\nNew Plant (No Name)")
print("Expected: Function Failed")
try:
    DB_Obj.new_plant(

    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")


# New Plant (STR given to INT Param)
print("\nNew Plant (STR given to INT Param)")
print("Expected: Function Failed")
try:
    DB_Obj.new_plant(
        name="Test Plant",
        desc="Test Desc",
        stock="STRING",
        temp_min="STRING",
        temp_max="STRING",
        hum_min="STRING",
        hum_max="STRING"
    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")


# Update Plant
print("\nUpdate Plant (Valid)")
print("Expected: Function Passed")
try:
    DB_Obj.update_plant(
        id=21,
        name="bruh",
        desc="Test Desc",
        stock=100,
        temp_min=50,
        temp_max=100,
        hum_min=50,
        hum_max=100
    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")


print("\nUpdate Plant (STRING in INT/FLOAT Param)")
print("Expected: Function Failed")
try:
    DB_Obj.update_plant(
        id=21,
        name="bruh",
        desc="Test Desc",
        stock="STRING",
        temp_min="STRING",
        temp_max="STRING",
        hum_min="STRING",
        hum_max="STRING"
    )
    print("Function Passed")
except Exception as e:
    print("Function Failed")

#View Plants
print("\nGrab Inventory")
print("Expected Output: Dataframe")
db_df = DB_Obj.view_plants()
print(type(db_df))
print(db_df.head())


#Grab plant sensor data (Week Worth)
print("\nWeek's worth of Sensor Data:")
print("Expected Output: Dataframe")
DB_Obj_sensor = Database(
    user='root',
    password='root',
    host='localhost',
    port='8080',
    database='test_db'
)
DB_Obj_sensor.connect()

temp = DB_Obj_sensor.grab_sensor()
print(type(temp))
print(temp.head())
