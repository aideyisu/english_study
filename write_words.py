# read files 
'''
https://docs.python.org/3/library/csv.html
'''
import csv

# r+ 指针位于头部
# a+ 指针位于末尾
with open("words.csv", 'a+') as file:
    all_data = csv.reader(file)

    for item in all_data:
        # print(', '.join(item))
        for j in item:
            print(eval(j))