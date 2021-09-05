'''

    read files 
    and config.ini many different config

'''
import json 
import configparser

def get_lines():
    with open("words.csv", 'r+',encoding='UTF-8') as file:
        return len(file.readlines())
 
def get_new_words():
    with open("words.csv", 'r+',encoding='UTF-8') as file:
        return json.loads(file.readlines()[-1])

# 1-2-5-7-14 days to review
def get_review_words():
    result = json.loads("{}")
    with open("words.csv", 'r+',encoding='UTF-8') as file:
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


def get_exercise_words(days):
    with open("exercise_words.csv", 'r+',encoding='UTF-8') as file:
        all_data = file.readlines()
        return json.loads(all_data[days-1]) if days != -1 else json.loads(all_data[-1])

def get_config(big, small):
    cf = configparser.ConfigParser()
    cf.read("config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
    return cf.get(f"{big}", f"{small}")  # 获取[big]中small对应的值

