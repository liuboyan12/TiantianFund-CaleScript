#脚本编辑打印辅助工具
#传入参数，打印参数名、参数值、参数类型
#要复制到编写的函数中使用，不可跨py使用
def tprint_save_version(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':', type(obj))
            print(obj)
            print()



#传入两个值将两个值转换为str进行对比
#如果两个是一致的那么返回值1，如果两个值不同返回0
def if_differ_str(_first, _second):
    _first=str(_first)
    _second=str(_second)
    if _first == _second:
        return_value = 1
    else:
        return_value = 0
    return return_value

#将字典里面的最后一个键值对取出
def getLastDict(_dict):
    _list = list(_dict.keys())
    length = len(_list)
    dict_key = _list[length - 1]
    result_value = _dict[dict_key]
    return dict_key, result_value

if __name__ == '__main__':
    b='1'

    # print(type(a),a)