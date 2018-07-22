def tprint(obj, except_word=""):
    """
    #脚本编辑打印辅助工具
    ┏━━━━┳━━┓
    ┃传入值  ┃类型┃
    ┣━━━━╋━━┫
    ┃任何变量┃ all┃
    ┗━━━━┻━━┛
    #要复制到编写的函数中使用，不可跨py使用
    """
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()

def if_differ_str(_first, _second):
    """
    #传入两个值将两个值转换为str进行对比
    #如果两个是一致的那么返回值1，如果两个值不同返回0
    :param _first: 第一个字符串
    :param _second: 第二个字符串
    :return: 比较结果
    """
    _first=str(_first)
    _second=str(_second)
    if _first == _second:
        return_value = 1
    else:
        return_value = 0
    return return_value


def getLastDict(_dict):
    """
    将字典里面的最后一个键值对取出
    :param _dict: 要被取出的字典
    :return: 最后的一对键值对
    """
    _list = list(_dict.keys())
    length = len(_list)
    dict_key = _list[length - 1]
    result_value = _dict[dict_key]
    return dict_key, result_value

def dict_JieQuBanDuan(_dict,key,diction='right'):
    """
    #截取传入key的前半段或者后半段
    #前半段left后半段rignt
    #{.........left........|........right..........}
    :param _dict: 要被截取的dict
    :param key: 要截取段中的键值
    :param diction: 方向，截取方向，向后或者向前（left/right）
    :return: 截取到的dict
    """
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



def value_2_key(_dict,_value):

    """
    #传入字典和字典内存在的value，返回其value的key值
    知道value反推可以，尽量保证value单一
    :param _dict: 被筛选的dict
    :param _value: 要找到的value值
    :return: key值
    """
    try:
        a1 = list(_dict.keys())[list(_dict.values()).index(_value)]
    except Exception as e:
        print('value 2 key出错')
        print(e)
    return a1



def find_max_or_min_in_list(_list=[],_geshu=1,max_or_min='max'):
    """
    返回list中最大的几个值，或者最小的几个值
    :param _list: 要进行比较的list
    :param _geshu: 取出最值的个数
    :param max_or_min: 输入为"max"或者是"min"表示要取出的是最大还是最小
    :return: 取出的几个最值
    """
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


def find_dict_key_and_fetch_value_to_list(_dict={},_key_list=[]):
    """
    遍历字典将list中的值对应字典中的key的值取出
    :param _dict: dict数据
    :param _key_list: 要取出的键的列表
    :return: 取出的dict
    """
    return_list = []
    for i in _key_list:
        return_list_value = _dict[i]
        return_list.append(return_list_value)
    return return_list



def dict_cut_out_piece_in_sequence(_dict,start_position,end_num=1):
    """
    从字典中选择一个起始位置向后截取end_num个键值对并返回
    start_position为dict中想要开始截取的起始未知的key
    :param _dict:  要被截取的dict
    :param start_position: 起始位置（该位置的键值）
    :param end_num: 截取到该位置后的第几个
    :return: 返回截取的dict段
    """
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

def fetch_dict_by_num(_dict, num):
    """
    取出字典中顺序的第num个
    :param _dict: 要取出的字典数据
    :param num: 要取第num个
    :return: 第num个键值对
    """
    _dict = _dict
    _list = list(_dict.keys())
    i = _list[num - 1]  # num-1
    i_value = _dict[i]
    strings = "{'" + str(i) + "':" + str(i_value) + "}"
    return_dict = eval(strings)
    return return_dict

def abandon_front_section_dict(dict={},num=1):
    """
    舍弃掉list中前几个键值对，如果舍弃个数大于整个dict的键值对个数将会报错
    :param dict: 将要被舍弃的dict
    :param num: 舍弃前面键值对的个数
    :return: 被舍弃后的dict
    """
    _keylist=list(dict.keys())
    if num>len(_keylist):
        print("舍弃个数长于字典键值对个数")
    else:
        abandonlist = []
        while 1<2:
            if num>0:
                value = _keylist[num-1]
                abandonlist.append(value)
                num=num-1
            else:
                break
        for i1 in list(abandonlist):
            dict.pop(i1)
    return dict

def fetch_maxormin_key_pairs(indict={},maxormin='max',num=1):
    """
    取出最大或者最小的键值对
    :param dict: 要处理的字典
    :param maxormin: 输入为最大或者最小max,min
    :param num: 取多少个
    :return: 返回值为取出最大/最小的键值对的字典
    """
    dict = indict
    controlnum = 1
    while 1<2:
        returndict={}
        if len(dict)<=num:
            print('取出个数太多，请调整个数')
        else:
            keylist = list(dict.keys())
            dict_value = 0
            for i in keylist:
                dict_key = i
                if maxormin==max:
                    if dict_value<=float(dict[i]):
                       dict_value=float(dict[i])
                       madedict='{"'+i+'":"'+str(dict_value)+'"}'
                elif maxormin==min:
                    if dict_value>=float(dict[i]):
                       dict_value=float(dict[i])
                       madedict = '{"' + i + '":"' + str(dict_value) + '"}'
                else:
                    print('请输入正确的取值,max/min:')
                    maxormin=input()
                    continue
            returndict.update(madedict)
            dict.pop(i)
        controlnum=controlnum+1
        if controlnum>num:
            return returndict
            break

def Erase_delete_corresponding_value(dict,value):
    """
    遍历dict删除对应value值的键值对
    :param dict:待处理字典
    :param value:要去掉的value值
    :return:处理完成的字典
    """
    keylist=list(dict.keys())
    for i in keylist:
        ifcode = dict[i]
        if ifcode == value:
            dict.pop(i)
        else:
            pass
    return dict





if __name__ == '__main__':
    _dict = {'a':3,'b':2,'c':3,'d':4}