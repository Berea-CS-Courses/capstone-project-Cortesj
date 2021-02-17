# Greenhouse Management Software
---
## Overview

The purpose of my project is to create software dedicated to monitoring, anaylzing and providing some form reccomendation/report for greenhouses. The software would have a hardware component to collect data from the greenhouses themselves. The software would be designed to run on a local server located on a local network with potential for certain automated actions, primarily revolved around maintaining certain conditions (temperature, humidity, etc...) when possible. 

## Concept 

The major features to be included would be an inventory system, data collection, analysis of said data for reports/appropriate actions and web/program GUI. The inventory system would keep a record of what is stored in the greenhouses and keep notes of a plant's perfered conditions. The data collection would be microcontrollers with sensors placed in specific locations to collect overall conditions of a greenhouse to be reported towards the main software component. The report/anaylsis component would check if greenhouse is within conditions for the plants and generate any reports/actions as need be or specificed by client. The web/program GUI would be direct interface with the system as it would allow the editing of inventory/database and being able to perform actions depending on how hardware is setup. Client might anticipate a API of some kind to connect to available shop fronts, but that might or might not be possible depending on if software would have internet access or time forbiding. 

## Requirements

### Functional
1. Enter/Edit/Delete Inventory entries
2. Collect Data from hardware sensors (Microcontrollers)
3. Analysis data to report potential enviormental issues with certain plants in inventory system
4. Report suggestions/programs or perform certain actions depending on client's preference

### Non-Functional
1. Software running on Linux
2. Software running on local network
3. Data collection handled by Microcontroller (Arduino/RasberryPi/Simulation)
4. Inventory system backend SQL (Currently Investigating)
5. Programmed in mixture of C++/Python
