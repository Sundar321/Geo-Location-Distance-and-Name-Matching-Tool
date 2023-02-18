import csv
from geopy.distance import distance
from Levenshtein import distance as levenshtein_distance
import os

# Reading data from the csv file
with open('assignment_data.csv', mode='r', newline='') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row
    rows = list(reader)

# Comparing each pair of rows
c=-1
for i in range(len(rows)):
    flag=True
    
    if(i==c):
        continue
    else:
        for j in range(i+1, len(rows)):
            name1=rows[i][0]
            lat1=rows[i][1]
            lon1 = rows[i][2]
            name2=rows[j][0]
            lat2=rows[j][1]
            lon2 = rows[j][2]
            
            # Calculating distance between the two points
            dist = distance((lat1, lon1), (lat2, lon2)).m
            # Calculating Levenshtein distance between the two names
            name_dist = levenshtein_distance(name1, name2)
            
            if dist <= 200 and name_dist <= 5:
                # If distance and name similarity criteria are met, mark both rows as similar
                rows[i].append(1)
                rows[j].append(1)
                #print(f"Similarity criteria met for rows {i} and {j}") Debugging code using print statements
                flag=False
                c=j
                break
    
        
        
            
        
    if(i!=c and flag==True):
        rows[i].append(0)
        

    # Writing updated data to a new csv file
    header = ['name','lat', 'lon', 'is_similar']
    output_file = os.path.join(os.getcwd(), 'output_data.csv')
    with open(output_file, mode='w', newline='') as f_update:
        writer = csv.writer(f_update)
        writer.writerow(header)
        writer.writerows(rows)
    
    
