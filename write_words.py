# read files 
import json

# r+ 指针位于头部
# a+ 指针位于末尾
def write_new_words(c1,c2,c3,c4,e1,e2,e3,e4):
    with open("words.csv", 'a+', encoding='UTF-8') as file:
        A = {}
        A[c1] = e1
        A[c2] = e2
        A[c3] = e3
        A[c4] = e4
        file.write("\n"+json.dumps(A))


def write_wrong_words(wrong_word_dict, exercise_words):
    with open("words.csv", 'a+', encoding='UTF-8') as file:
        result = {}
        for item in wrong_word_dict:
            if wrong_word_dict[item] == 0:
                # 记录
                pass


            pass
        file.write("\n"+json.dumps(wrong_word_dict))