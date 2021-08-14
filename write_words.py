# read files 
'''
https://docs.python.org/3/library/csv.html
'''
import json
# r+ 指针位于头部
# a+ 指针位于末尾
with open("words.csv", 'a+') as file:
    A = {}
    A["1"] = "A"
    A["2"] = "B"
    A["3"] = "C"
    A["4"] = "D"
    file.write("\n"+json.dumps(A))