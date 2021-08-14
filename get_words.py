# read files 
import json 

def get_new_words():
    with open("words.csv", 'r+') as file:
        all_data = file.readlines()
        return json.loads(all_data[-1])

# 1-2-5-7-14 dats to review
def get_review_words():
    result = {}
    with open("words.csv", 'r+') as file:
        all_data = file.readlines()
        try:
            result['1'] = json.loads(all_data[-2])
        except:
            result['1'] = {"hello":"asd","he2":"a2","he3":"3","he4":"a4"}

        try:
            result['2'] = json.loads(all_data[-3])
        except:
            result['2'] = {"hello":"asd","he2":"a2","he3":"3","he4":"a4"}

        try:
            result['5'] = json.loads(all_data[-6])
        except:
            result['5'] = {"hello":"asd","he2":"a2","he3":"3","he4":"a4"}

        try:
            result['7'] = json.loads(all_data[-8])
        except:
            result['7'] = {"hello":"asd","he2":"a2","he3":"3","he4":"a4"}

        try:
            result['14'] = json.loads(all_data[-15])
        except:
            result['14'] = {"hello":"asd","he2":"a2","he3":"3","he4":"a4"}
    return result


# A = get_new_words()
# print(A)
# B = get_review_words()
# print(B)