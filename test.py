from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num as find_double


def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            # print()


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

def cross_line(_dictA, _dictB):
    '''
    :param _dictA: 传入的第一个dict
    :param _dictB: 传入的第二个dict
    :return: dict焦点数据值
    焦点数据格式{焦点:{上/下穿线:[值1，值2]}}
    规则：
        焦点为dictA和dictB中的键值，但是此函数里面返回值是区间内的第几个焦点
        上穿线（A从上穿越B到下方）为1，下穿线（A从下方穿越B到上方）为-1
        值1与值2位穿越点相邻的两个键的值
    '''

    single_dict = made_single_data(_dictA, _dictB)
    return_dict = {}

    def changes_fuction(A):
        A = int(list(A.values())[0])
        return A

    def first_key_value(_dict1, _dict2):
        '''
        判断dictA和dictB哪个在上，A在B上为1，A在B下为-1
        '''
        firstdata = 1
        while 1 < 2:

            A = changes_fuction(find_double(_dict1, firstdata))
            B = changes_fuction(find_double(_dict2, firstdata))

            if A > B:
                value = 1
                return value
            elif A < B:
                value = -1
                return value
            else:
                firstdata = firstdata + 1

    AB_relation_first = first_key_value(_dictA, _dictB)
    jiaodianNo = 0
    AB_relation=AB_relation_first
    for i in range(len(single_dict)):
        i1=i+1

        ifcode = changes_fuction(find_double(single_dict, i1))
        print('ifcode:',ifcode,'i:',i)
        if ifcode == 0:
            continue
        else:

            try:
                def test(_dict, ix):
                    while 1 < 2:
                        jiangex = 1
                        a = changes_fuction(find_double(_dict, ix))
                        #
                        b = changes_fuction(find_double(_dict, ix + jiangex))
                        print('a,b', a, b)
                        axb = a * b
                        if axb == 0:
                            jiangex = jiangex + 1
                            # print('jiange1',jiange)
                        else:
                            break
                    return axb, i1, jiangex

                axb = test(single_dict, i1)[0]
                jiange = test(single_dict, i1)[2]
                # while 1 < 2:
                #     a = changes_fuction(find_double(single_dict, i1))
                #     #
                #     b = changes_fuction(find_double(single_dict, i1 + jiange))
                #     print('a,b',a,b)
                #     axb = a * b
                #     if axb == 0:
                #         jiange = jiange + 1
                #         # print('jiange1',jiange)
                #     else:
                #         jiange=1
                #         break



                if axb < 0:
                    jiaodianQ = str(list(find_double(single_dict, i1).keys())[0])
                    jiaodianH = str(list(find_double(single_dict, i1 + jiange).keys())[0])
                    print('jiaodianH:',jiaodianH)
                    # print('jiange2',jiange)

                    value1_value2 = ":['"+str(jiaodianQ)+"','"+str(jiaodianH)+"']}}"
                    '''print('在', jiaodianQ, jiaodianH, '之间存在一个焦点')'''
                    # print('AB_relation',AB_relation)
                    AB_relation = AB_relation * -1
                    chuanxian = "{'"+str(AB_relation)+"'"
                    '''if ifcode_chuanxian == 1:初始在上方的线自上而下穿线'''
                    '''if ifcode_chuanxian == -1:初始在上方的线自下而上穿线'''
                    jiaodianNo =jiaodianNo + 1
                    zuzhuangvalue = "{'"+str(jiaodianNo)+"':"+chuanxian+value1_value2
                    return_dict.update(eval(zuzhuangvalue))
                    # print(eval(zuzhuangvalue))

                # if
            except Exception as e:
                break
    return return_dict



if __name__ == '__main__':

    _dictA={'a':'3','b':'2','c':'5','d':'5','e':'4','f':'6','g':'6','h':'7'}
    _dictB={'a':'2','b':'3','c':'4','d':'5','e':'5','f':'6','g':'7','h':'8'}

    """
    single_dict函数，将两个离散的列转换为一个简单的位置关系
    """
    print(cross_line(_dictA, _dictB))





