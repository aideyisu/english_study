'''

    检查系统内文件是否完备

'''

from pathlib import Path
import os

basepath = os.path.dirname(__file__)  # 当前文件所在路径

file_list = []

for file in file_list:
    my_file = Path(f'{basepath}/analysis_result/asd')
    if not my_file.exists():
        # 检测是否存在id路径不存在
        os.makedirs(my_file)  # 只能创建单级目录 =.=对这个用法表示怀疑
        print(f'路径不存在 {my_file} 创建路径')