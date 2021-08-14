# read files 

import json 

def get_new_words():
    result = {}
    with open("words.csv", 'r+') as file:

        all_data = file.readlines()
        for item in all_data:
            result = json.loads(item)
            # TODO 等待优化
            break
    return result

def get_review_words():
    result = {}
    with open("words.csv", 'r+') as file:
        all_data = file.readlines()
        for item in all_data:
            result = json.loads(item)
            # TODO 等待优化
            break
    return result


A = get_new_words()
print(A)