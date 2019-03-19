import os
import sys
sys.path.append(os.getcwd())

import pytest

from read_data.read_data import read_data


def get_data():
    datas = read_data() #调用读yaml文件的函数，得到文件内的数据
    #解析数据，提取数据并构造成适合测试用例方法参数化的数据格式：列表嵌套
    #遍历datas.values()提取键值,提取键值内部的各键键值组成一个元组并添加到一个空列表中
    arrs = []
    for data in datas.values():
        arrs.append((data.get("a"),data.get("b")))
    # print(arrs)
    return arrs

class Test02():
    # 往测试用例方法里导入参数:("参数名",[(参数值)])
    @pytest.mark.parametrize("param1,param2",get_data())
    def test01(self,param1,param2):
        print("参数1：",param1)
        print("参数2：", param2)
        print("两个参数之和：", param1 + param2)

#     def test01_debug(self,param1,param2): #测试用例方法-本页中执行
#         print("参数1：",param1)
#         print("参数2：", param2)
#         print("两个参数之和：",param1+param2)
#
# if __name__ == '__main__':
#     get_data()
#     Test02().test01_debug(1,2)