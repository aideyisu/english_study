# read files 
'''
https://docs.python.org/3/library/csv.html
'''
import csv

with open("words.csv", 'r+') as file:
    all_data = csv.reader(file)

    for item in all_data:
        # print(', '.join(item))
        for j in item:
            print(eval(j))
    