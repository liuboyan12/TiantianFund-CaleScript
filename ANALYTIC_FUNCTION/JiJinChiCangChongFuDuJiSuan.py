from fundition_static_packaging.TianTianJiJinShuJuChuLi import *

"""
传入值
"""
def stock_list(fundcode):
    _date = singleness_fund_inquire(fundcode)
    # _stock_date =cut_stock_date(_date)
    _result = cut_stock_date(_date)
    return _result





if __name__ == '__main__':

    # code_list = ['002001','070001']
    # result_list = []
    # for i in code_list:        #002001
    #     passcode = 0
    #     while(passcode<1):
    #         try:
    #             _stock_list=stock_list(i)
    #             #"['0008582', '0003332', '6011551', '0005682', '6038331', '6002761', '0020432', '0007862', '0009632', '6038161']"
    #             #{'002001':[]}
    #             _stock_list = "'"+i+"':"+str(_stock_list)+','
    #             passcode = 1
    #         except Exception as e :
    #             pass
    #     result_list.append(_stock_list)
    #     # print(result_list)
    # _dict_string = ''
    # for i in result_list:
    #     _dict_string = _dict_string+str(i)
    #
    # _dict_result_for_part_1 = eval('{'+_dict_string+'}')
    # #+++++++++++++++++part1-over++++++++++++++++++++++++++++
    # _dict = {}
    # for value_list in _dict_result_for_part_1.values():
    #     for i in value_list:
    #         get_value = _dict.get(i)
    #         # print(get_value)
    #         if get_value == None:
    #             wait_add = eval("{'"+str(i)+"':1}")
    #             # print(type(wait_add),wait_add)
    #             _dict.update(wait_add)
    #             # print(type(_dict),_dict)
    #         else :
    #             _dict[i]=_dict[i]+1
    # print(_dict)
    print(stock_list('002001'))
