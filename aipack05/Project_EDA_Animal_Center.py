'''
DataAnalytics Project: EDA Animal Care Center
--------------------------------------------
Project Task-01: Print the shape of the dataset

Project Task-02: Which column has null values?

Project Task-03: Remove the duplicate rows from intake dataset.

Project Task-04: Rename to column names as follows:-
1) 'Old Column Name' = 'New Column Name'
2) 'Animal ID'        =  'id',
3) 'DateTime'         =  'date_time',
4) 'MonthYear'        =  'month_year',
5) 'Found Location'   = 'found_location',
6) 'Intake Type'      = 'intake_type',
7) 'Intake Condition' = 'intake_condition',
8) 'Animal Type'      = 'animal_type',
9) 'Sex upon Intake'  = 'sex_upon_intake',
10) 'Age upon Intake' = 'age_upon_intake',
11) 'Breed'           =  'breed'

Project Task-05: Remove Monthyear column because it is similar to Datetime column.

Project Task-06: Extracting month and year from Datetime column

Project Task-07: Which month,year has most animal intakes ?
         Draw a pie chart representing year wise animal intake from year 2014 to 2021.

Project Task-08: Create a bar chart to represent month wise animal intake.
         Which month has heighest animal intake?

Project Task-09: Create a bar chart to represent animal intake methods wise counting.
         What are the animal intake methods ? Print their names?

Project Task-10: What are the conditions of animals which are taken into the shelter?

Project Task-11: How many types of animals are taken into shelter and what is their total count?

Project Task-12: what are the top 10 breeds in the animal shelter?
         Draw a breed wise bar plot.

Project Task-13: What are top 20 common names of animals in animal shelter?
         Draw a bar char reprsenting name wise count of the animals.

Project Task-14: Draw a bar char representing the "Outcome Type" wise count of animals using the dataset of Animal_Center_Outcomes.csv.

'''

import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns
from IPython.core.pylabtools import figsize

pd.set_option('display.max_column',None)
pd.set_option('display.width',1000)

intake=pd.read_csv('DataSet_Animal_Center_Intakes.csv')
outcome=pd.read_csv('DataSet_Animal_Center_Outcomes.csv')

print("\nintake.shape = ",intake.shape)
print("\noutcome.shape = ",outcome.shape)

print(intake.head())
plt.subplots(figsize=(8,6))
sns.heatmap(intake.isnull())
plt.show()