# [GeoLocation Distance and Name Matching Tool](https://www.gospatic.com/)
A Problem statement from Spatic company which aims to Maximize revenue or profit share by leveraging location intelligence, geospatial and hyperlocal analytics, and AI/ML.

## Problem statement
* You are given a dataset which consists of entries with latitude, longitude, and name (link to the dataset file is given below along with some helpful materials).  Your task is to write a Python program that will identify entries which are within 200 meters of each other and have similar names i.e. strings that are similar, but not necessarily same

   
## For Example
* Bangalore and Bangaloore
* new delhi and NewDelhi  

## Similarity Criteria: 
1. Similar points should be within 200 meters distance from each other 
2. Maximum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other should be less than 5  

## Here are the requirements for the solution:
1. The program should be written in Python and use appropriate data structures to store the dataset.  
2. Output should be a csv file with all the entries which satisfy given criteria of similarity marked as True / 1 in a separate column named is_similar  
3. Submission files both python program and output csv file should be uploaded to a public github repository   

## [Input Dataset Link : ](https://drive.google.com/file/d/1fcfmdshOYn0A_X6D7hW49ioSL8VhYQby/view?usp=sharing)  
* Link : https://drive.google.com/file/d/1fcfmdshOYn0A_X6D7hW49ioSL8VhYQby/view?usp=sharing


**Sample Input data and Output data**  
![image](https://github.com/Sundar321/Spatic-/blob/main/sample%20input%20data%20and%20output%20data.png)


## My Approach for solving  
1. Modules  
```python
import csv
# for working with csv files
from geopy.distance import distance
# for caluculating the distance between two points of Latitude and longitude
from Levenshtein import distance as levenshtein_distance
# for finding levenshtein_distance distance using Levenshtein Module
import os
``` 
2. The given task is to identify entries that are within 200 meters of each other and have similar names. The Levenshtein distance is used to compare the similarity of the names. The maximum number of single-character edits required to change one word to the other should be less than or equal to 5. 
```python
# Calculating distance between the two points
            dist = distance((lat1, lon1), (lat2, lon2)).m
            # Calculating Levenshtein distance between the two names
            name_dist = levenshtein_distance(name1, name2)
            
            if dist <= 200 and name_dist <= 5:
                # If distance and name similarity criteria are met, mark both rows as similar
                rows[i].append(1)
                rows[j].append(1)
```    
3. The process starts by reading the data from the csv file using the csv module. The first row is skipped since it contains headers. The data is then stored in a list of lists, where each sub-list represents a row.    
4. Then, each pair of rows is compared for distance and name similarity criteria. If the criteria are met, both rows are marked as similar by adding a value of 1 to a new column named 'is_similar'. If the similarity criteria are not met, a value of 0 is added to the 'is_similar' column for that row. A flag variable is used to keep track of whether any similar entry was found for the current row or not. If no similar entry is found for a row, it is marked as 0 in the 'is_similar' column.   
5. The output data is written to a new csv file named 'output_data.csv'. The header row contains the column names 'name', 'lat', 'lon', and 'is_similar'. The updated rows are written to the output file using the writerows() method of the csv module.   
6. The Levenshtein distance is a string metric used to measure the difference between two sequences. It calculates the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. The geopy module is used to calculate the distance between two points using their latitude and longitude coordinates. 

7. Overall, the program reads the data from the csv file, compares each pair of rows for similarity, and writes the updated data to a new csv file with a new column named 'is_similar' indicating whether or not a row is similar to any other row in the dataset.    




## Author  
Bhanu Sundar Kunchala


