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

#打印传入的变量名、类型、值
def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()

#传入字典和字典内存在的value，返回其value的key值
def value_2_key(_dict={},_value=''):
    try:
        a1 = list(_dict.keys())[list(_dict.values()).index(_value)]
    except Exception as e:
        print('找value 2 key出错')
        print(e)
    return a1

#传入list，返回最大的几个值，或者最小的几个值
def find_max_or_min_in_list(_list=[],_geshu=1,max_or_min='max'):
    _return_list = []
    if len(_list)<=_geshu:
        print("传入长度小于取值个数")
    else:
        if max_or_min=='max':
            for i in range(_geshu):
                return_value = max(_list)
                _list.remove(return_value)
                _return_list.append(return_value)
        elif max_or_min=='min':
            for i in range(_geshu):
                return_value = min(_list)
                _list.remove(return_value)
                _return_list.append(return_value)
        else:
            print('未接收到最大/最小取值')
    return _return_list

#遍历字典将list中的值对应字典中的key的值取出
def find_dict_key_and_fetch_value_to_list(_dict={},_key_list=[]):
    return_list = []
    for i in _key_list:
        return_list_value = _dict[i]
        return_list.append(return_list_value)
    return return_list

#从字典中选择一个起始位置向后截取end_num个键值对并返回
def dict_cut_out_piece_in_sequence(_dict,start_position,end_num=1):
    try:
        _list = list(_dict.keys())
        num_s = _list.index(start_position)
        ifcode = len(_list)-(num_s+end_num)
        if ifcode<0:
            end_num = len(_list) - num_s
            e1 = '截取值溢出，修改截取值为最末位'+str(end_num)

        else:
            #pass
            num_e = num_s+int(end_num)
            _list = _list[num_s:num_e]
            return_dict = {}
            for i in _list:
                return_dict_update =eval("{'"+str(i)+"':'"+str(_dict[i])+"'}")
                return_dict.update(return_dict_update)
        return return_dict
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print()
