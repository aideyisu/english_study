
import json
import xlwt
# 单词乱序
import random 
from datetime import datetime

from side import site_write_line_style
import get_words


# 获取当前日期
# dd/mm/YY H:M:S
def get_datetime():
    return datetime.now().strftime("%Y-%m-%d")


# 保存当日全部单词
def save_today_words(word_dict):
    with open("exercise_words.csv", "a+") as file:
        file.write(json.dumps(word_dict)+'\n')


def output_today_exercise():
    # 备份
    today_word_list = {}
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    font = xlwt.Font() # Create Font
    # font.bold = True # Set font to Bold
    style = xlwt.XFStyle() # Create Style
    style.font = font # Add Bold Font to Style
    # 居中设置 
    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style.alignment = al
    worksheet.write_merge(0, 0, 0, 7, f'{get_datetime()}       english', style)
    worksheet.write_merge(1, 3, 0, 0, f'new', style) 
    worksheet.write_merge(5, 7, 0, 0, f'review', style) 

    # 读取新单词
    new_words = get_words.get_new_words()

    # 写入单词
    y_start = 1
    x_site = 1
    new_word_keys = list(new_words.keys())
    random.shuffle(new_word_keys)
    for word_key in new_word_keys:
        today_word_list[word_key] = new_words[word_key]
        # worksheet.write(y_start,x_site, label = f'{item}')
        style = site_write_line_style()
        worksheet.write(y_start,x_site, f'{word_key}', style)
        worksheet.write(y_start,x_site+1, ' ', style)
        worksheet.write(y_start,x_site+2, ' ', style)
        y_start += 1

    # 需复习的单词
    review_words = get_words.get_review_words()
    y_start = 5
    x_start = 1
    for one_day in review_words:
        oneday_review_word_keys = list(review_words[one_day].keys())
        random.shuffle(oneday_review_word_keys)

        for review_word in oneday_review_word_keys:
            today_word_list[review_word] =review_words[one_day][review_word]
            style = site_write_line_style()
            worksheet.write(y_start,x_start,  f'{review_word}', style)
            worksheet.write(y_start,x_start+1, ' ', style)
            worksheet.write(y_start,x_start+2, ' ', style)
            y_start += 1

        if y_start == 13:
            y_start = 1
            x_start = 5

    # 设置单元格宽度
    for number in range(0, 8):
        worksheet.col(number).width = 4200

    for number in range(0, 13):
        worksheet.row(number).height_mismatch = True
        worksheet.row(number).height = 775
    # 单例保存
    save_today_words(today_word_list)
    
    # 保存至表格
    workbook.save(f'{get_datetime()}.xls')

def output_today_exercise_answers():
    # TODO
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Answers')
    font = xlwt.Font() # Create Font
    # font.bold = True # Set font to Bold
    style = xlwt.XFStyle() # Create Style
    style.font = font # Add Bold Font to Style
    # 居中设置 
    al = xlwt.Alignment()
    al.horz = 0x02      # 设置水平居中
    al.vert = 0x01      # 设置垂直居中
    style.alignment = al
    worksheet.write_merge(0, 0, 0, 7, f'{get_datetime()}       english', style)
    worksheet.write_merge(1, 3, 0, 0, f'new', style) 
    worksheet.write_merge(5, 7, 0, 0, f'review', style) 

    # 读取新单词
    new_words = get_words.get_new_words()

    # 写入单词
    y_start = 1
    x_site = 1
    new_word_keys = list(new_words.keys())
    random.shuffle(new_word_keys)
    for word_key in new_word_keys:
        # worksheet.write(y_start,x_site, label = f'{item}')
        style = site_write_line_style()
        worksheet.write(y_start,x_site, f'{word_key}', style)
        worksheet.write(y_start,x_site+1, ' ', style)
        worksheet.write(y_start,x_site+2, ' ', style)
        y_start += 1

    # 需复习的单词
    review_words = get_words.get_review_words()
    y_start = 5
    x_start = 1
    for one_day in review_words:
        oneday_review_word_keys = list(review_words[one_day].keys())
        random.shuffle(oneday_review_word_keys)

        for review_word in oneday_review_word_keys:
            style = site_write_line_style()
            worksheet.write(y_start,x_start,  f'{review_word}', style)
            worksheet.write(y_start,x_start+1, ' ', style)
            worksheet.write(y_start,x_start+2, ' ', style)
            y_start += 1

        if y_start == 13:
            y_start = 1
            x_start = 5

    # 设置单元格宽度
    for number in range(0, 8):
        worksheet.col(number).width = 4200

    for number in range(0, 13):
        worksheet.row(number).height_mismatch = True
        worksheet.row(number).height = 775

    
    # 保存至表格
    workbook.save(f'{get_datetime()}.xls')

