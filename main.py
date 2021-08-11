
import xlwt
from datetime import datetime
words = {"俺是第一个":"first",
        "俺是第二个":"second"}

# write xls

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
# 第一行 第零列
worksheet.write(1,0, label = 'this is test')

# 获取当前日期
# dd/mm/YY H:M:S
now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%Y-%m-%d")

# 保存
workbook.save(f'{dt_string}.xls')