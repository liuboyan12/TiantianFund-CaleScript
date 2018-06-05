from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num as find_double


def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()


#把原有数列变成大小关系表示的单一数列
#_dict={'a':'1','b':'2','c':'3','d':'4'}——A
#_dict1={'a':'2','b':'1','c':'4','d':'5'}——B
#上面两个变为
#{'a': -1, 'b': 1, 'c': -1, 'd': -1}
def made_single_data(_dict1,_dict2):
    _list_dict_key = list(_dict1.keys())
    back_dict = {}
    for i in _list_dict_key:
        fi = _dict1[i]
        gi = _dict2[i]
        if fi > gi:
            re_code = 1
        elif fi < gi:
            re_code = -1
        else:
            re_code = 0
        pz_string = eval("{'" + str(i) + "':" + str(re_code) + "}")
        back_dict.update(pz_string)
    return back_dict

#将1/-1/0的简单数列进行整理计算，辅助made_single_data形成判断数据
def single_date_trade(_dict1,_dict2,single_dict):
    #默认A在B上为1，那么A在B下为-1
    AupBcode = list(find_double(single_dict,1).values())[0]
    print(AupBcode)

    #数据操作
    _list = list(single_dict.values())
    print(_list,'\n')
    #拼装list
    string = ''
    for i in _list:
        string = string+str(i)
    print(string,'\n')

    index_in_string_list = []
    # while 1<2:
    index_in_string = string.find('-11')
    if index_in_string!=-1:
        index_in_string_list.append(index_in_string+1)
        print('出现交叉位置为：', index_in_string + 1, index_in_string + 2, '\n')
        string = string[index_in_string+len('-11'):]
        print(string)
    else:
        break



    # a = find_double(_dict1, index_in_string + 1)
    # a_key = a.keys()
    # b = find_double(_dict1, index_in_string + 2)
    # b_key = b.keys()
    # print(a_key, b_key)





    # returnA = find_double(_dict1,index_in_string)
    # returnB = find_double(_dict2,index_in_string)
    # print(returnA)
    # print(returnB,'\n')

if __name__ == '__main__':
    # Aline：————
    # Bline：————

    # A穿越B到下方 X ：1-1    （-11）
    # B穿越A到上方 X ：-11    （1-1）
    # A穿越B到下方 X ：10-1    （-101）
    # B穿越A到上方 X ：-101	 （10-1）

    _dict={'a':'1','b':'2','c':'3','d':'4'}
    _dict1={'a':'2','b':'1','c':'4','d':'5'}
    """type1"""
    single_dict = made_single_data(_dict,_dict1)
    tprint(single_dict)
    single_date_trade(_dict,_dict1,single_dict)






#找到第一个
    # return_list = []
    # string = '-1010111001-01-010-10'
    # a = string.find('010')
    # return_list.append(a+len('010'))
    # print(string[:a])
    # print()
    # string = string[a+len('010'):]
    # tprint(string)