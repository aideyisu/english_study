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
    with open("wrong.csv", 'a+', encoding='UTF-8') as file:
        result = {}
        print(wrong_word_dict)
        for item in wrong_word_dict:
            print(wrong_word_dict[item], wrong_word_dict[item] == '0')
            if wrong_word_dict[item] == '0':
                # 说明当前单词默错了 记录之
                # exercise_words[item] --- 数字 0 或者 1
                result[item] = exercise_words[item]
        print(result)
        file.write(json.dumps(result)+"\n")