
import xlwt

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = 'Times New Roman' 
font.bold = True # 黑体
font.underline = True # 下划线
font.italic = True # 斜体字
style.font = font # 设定样式
worksheet.write(0, 0, 'Unformatted value') # 不带样式的写入

worksheet.write(1, 0, 'Formatted value', style) # 带样式的写入

# 设置单元格宽度
worksheet.col(0).width = 3333

workbook.save('formatting.xls') # 保存文件