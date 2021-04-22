-- create databases
CREATE SCHEMA inventory_test;
CREATE SCHEMA sensor_data_test;

-- create a table | sensor_data_test
CREATE TABLE sensor_data.sensor_1 (
  time DATETIME NOT NULL,
  temp FLOAT NULL,
  humidity FLOAT NULL,
  PRIMARY KEY (time));

-- create a table | inventory
CREATE TABLE inventory.inventory (
  id INT NULL,
  name TEXT NULL,
  description TEXT NULL,
  price FLOAT NULL,
  stock INT NULL,
  PRIMARY KEY (id));

CREATE TABLE inventory.temp_humidity (
  id INT NULL,
  temperature FLOAT NULL,
  humidity FLOAT NULL,
  PRIMARY KEY(id);
  FOREIGN KEY (id) REFERENCES inventory(id));
