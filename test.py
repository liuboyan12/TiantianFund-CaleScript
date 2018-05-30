def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()





if __name__ == '__main__':
    # _dict={'a':'1','b':'2','c':'3','d':'4'}
    # _dict1={'a':'2','b':'1','c':'4','d':'5'}
    # """type1"""
    # _list_dict_key = list(_dict.keys())
    # back_dict= {}
    # for i in _list_dict_key:
    #     fi=_dict[i]
    #     gi=_dict1[i]
    #     if fi>gi:
    #         re_code = 1
    #     elif fi<gi:
    #         re_code = -1
    #     else:
    #         re_code=0
    #     pz_string = eval("{'"+str(i)+"':"+str(re_code)+"}")
    #     back_dict.update(pz_string)
    # tprint(back_dict)
    # _list_back_dict_key=back_dict.values()
    # pz_string = ''
    # for i in _list_back_dict_key:
    #     pz_string=pz_string+str(i)
    # tprint(pz_string)
    # a = pz_string.find('-1-11-1')sd
    # tprint(a)


    return_list = []
    string = '-1010111001-01-010-10'
    a = string.find('010')
    print(string[:2])
    print(a)
    string = string[a+len('010'):]
    tprint(string)