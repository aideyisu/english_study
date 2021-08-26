import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，
                        # 每个section由[]包裹，即[section])，并以列表的形式返回
print(secs)

options = cf.options("Email")  # 获取某个section名为Mysql-Database所对应的键
print(options)

items = cf.items("Email")  # 获取section名为Mysql-Database所对应的全部键值对
print(items)

host = cf.get("Email", "username")  # 获取[Mysql-Database]中host对应的值
print(host)