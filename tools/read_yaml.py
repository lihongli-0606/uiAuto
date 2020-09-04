import yaml
import os
from config import BASE_PATH


# 以下返回数据格式为列表嵌套字典：[{},{},...]
def read_yaml(filename):
    # 组装数据文件路径
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    # 定义空列表，用于返回数据
    arr = []
    # 打开文件流
    with open(file_path, 'r', encoding='utf-8') as f:
        for data in yaml.safe_load(f).values():
            # print(data)
            arr.append(data)
    return arr


# 以下返回数据格式为列表嵌套元组 [(),(),...]
# def read_yaml(filename):
#     # 组装数据文件路径
#     file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
#     # 定义空列表，用于返回数据
#     arr = []
#     # 打开文件流
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for data in yaml.safe_load(f).values():
#             # print(data)
#             arr.append(tuple(data.values()))
#     return arr


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))
