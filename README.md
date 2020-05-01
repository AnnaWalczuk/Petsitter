
This is a database for a dog hotel named “Petsitter”.


### Introduction

After connecting to the database there’s a menu.

Employees can view dogs that are currently in hotel (filtering by name or all records) and save dogs’ register to a txt file. The can also check which dog they should take for a walk and for how long (view, inner join). Finally, they can visualise a plot showing how many dogs there are currently in the hotel by age and by sex.

The owner of the dog hotel (admin) can add or remove dogs from database. Removing a dog from “dogs” table triggers removing it from “walks” table. The owner can assign an employee to a dog he should take for a walk. He can also fetch information about dog food prices from several websites and visualise them in one table.



### Technologies
```bash
Project has been created with
```
Python 3.7  
PyCharm 2019.1.4 Community Edition  
MySQL Workbench 6.3 Community  



### Setup
```bash
To run this project, install these Python libraries:
```
import pymysql  
import os  
import requests  
from bs4 import BeautifulSoup  
import matplotlib.pyplot as plt  
import numpy as np  
import pandas as pd  
import datetime  



### Launch

Run the project using “Menu.py”
