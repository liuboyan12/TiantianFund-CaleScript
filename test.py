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

if __name__ == '__main__':

    _dictA={'a':'3','b':'2','c':'5','d':'5','e':'4','f':'6','g':'6','h':'7'}
    _dictB={'a':'2','b':'3','c':'4','d':'5','e':'5','f':'6','g':'7','h':'8'}

    """
    single_dict函数，将两个离散的列转换为一个简单的位置关系
    """
    single_dict = made_single_data(_dictA,_dictB)
    tprint(single_dict)
    def changes_fuction(A):
        A = int(list(A.values())[0])
        return A
    def first_key_value(_dict1,_dict2):
        '''
        判断dictA和dictB哪个在上，A在B上为1，A在B下为-1
        '''
        firstdata=1
        while 1<2:

            A = changes_fuction(find_double(_dict1,firstdata))
            B = changes_fuction(find_double(_dict2,firstdata))

            if A>B:
                value =1
                return value
            elif A<B:
                value = -1
                return value
            else:
                firstdata = firstdata+1

    AB_relation =  first_key_value(_dictA,_dictB)
    # tprint(AB_relation)


    for i in range(len(single_dict)):
        ifcode = changes_fuction(find_double(single_dict,i))
        if ifcode == 0:
            continue
        else:
            jiange = 1
            try:
                while 1<2:
                    a=changes_fuction(find_double(single_dict,i))
                    b=changes_fuction(find_double(single_dict,i+jiange))
                    axb =  a*b
                    if axb == 0:
                        jiange=jiange+1
                    else:
                        break
                if axb<0:
                    jiaodianQ =str(list(find_double(single_dict,i).keys())[0])
                    jiaodianH =str(list(find_double(single_dict,i+jiange).keys())[0])
                    print('在',jiaodianQ,jiaodianH,'之间存在一个焦点')

                    ifcode_chuanxian  = AB_relation*-1
                    if ifcode_chuanxian ==1:
                        print('初始在上方的线自上而下穿线')
                    if ifcode_chuanxian ==-1:
                        print('初始在上方的线自下而上穿线')
                # if
            except Exception as e:
                break
            print(axb)
            print()






