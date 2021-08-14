# read files 
import json

# r+ 指针位于头部
# a+ 指针位于末尾
# with open("words.csv", 'a+') as file:
#     A = {}
#     A["1"] = "A"
#     A["2"] = "B"
#     A["3"] = "C"
#     A["4"] = "D"
#     file.write("\n"+json.dumps(A))

def write_new_words(c1,c2,c3,c4,e1,e2,e3,e4):
    with open("words.csv", 'a+', encoding='UTF-8') as file:
        A = {}
        A[c1] = e1
        A[c2] = e2
        A[c3] = e3
        A[c4] = e4
        file.write("\n"+json.dumps(A))
