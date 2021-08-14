
import xlwt
from datetime import datetime
import get_words

# 获取当前日期
# dd/mm/YY H:M:S
now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%Y-%m-%d")

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
# 第一行 第零列 
# TODO 等待被合并
worksheet.write(0,0, label = f'{dt_string} english')
worksheet.write(1,0, label = 'new')


# write xls

# 读取新单词
new_words = get_words.get_new_words()

# 写入单词
y_start = 1
for item in new_words:
    worksheet.write(y_start,1, label = f'{item}')
    y_start += 1

# 获取需要复习的单词
revire_words = get_words.get_review_words()



# 保存至表格
workbook.save(f'{dt_string}.xls')