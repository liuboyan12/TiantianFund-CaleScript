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

#截取传入key的前半段或者后半段
#前半段left后半段rignt
#{.........left........|........right..........}
def dict_JieQuBanDuan(_dict,key,diction='right'):
    in_time = key
    _list = list(_dict.keys())
    a = _list.index(in_time)
    final_dict = {}
    if diction == 'left':
        for i in range(a + 1):
            value = _dict[_list[i]]
            assembly_dict = eval("{'" + str(_list[i]) + "':" + str(value) + "}")
            final_dict.update(assembly_dict)
    elif diction == 'right':
        _list_right = _list[a:]
        for i in _list_right:
            value = _dict[i]
            assembly_dict = eval("{'" + str(i) + "':" + str(value) + "}")
            final_dict.update(assembly_dict)
    else:
        print('参数错误')
    return final_dict

def value_2_key(_dict={},_value=''):
    a1 = list(_dict.keys())[list(_dict.values()).index(_value)]
    return a1

if __name__ == '__main__':
    _list = list("[ 0.03, 0.03, 0.003, 0.002, 0.009, 0.028, 0.026, 0.061, 0.073, 0.07, 0.086, 0.075, 0.091, 0.099, 0.095, 0.076, 0.084, 0.085]")
    print(type(_list))
    _geshu = 3
    _return_list = []
    if len(_list)<=_geshu:
        print("传入长度小于取值个数")
    else:
        for i in range(_geshu):
               return_value = max(_list)
               _list.remove(return_value)
               _return_list.append(return_value)
    print(_return_list)
