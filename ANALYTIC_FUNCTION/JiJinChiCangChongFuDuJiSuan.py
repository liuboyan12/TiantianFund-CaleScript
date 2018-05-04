from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *

"""
传入值
"""
def stock_list(fundcode):
    _date = singleness_fund_inquire(fundcode)
    _result = cut_stock_date(_date)
    return _result

def chongfudu_hanshu(fundcode_list):
    code_list = fundcode_list
    result_list = []
    for i in code_list:        #002001
        passcode = 0
        while(passcode<1):
            try:
                _stock_list=stock_list(i)
                _stock_list = "'"+i+"':"+str(_stock_list)+','
                passcode = 1
            except Exception as e :
                pass
        result_list.append(_stock_list)
    _dict_string = ''
    for i in result_list:
        _dict_string = _dict_string+str(i)
    _dict_result_for_part_1 = eval('{'+_dict_string+'}')
    #+++++++++++++++++part1-over++++++++++++++++++++++++++++
    _dict = {}
    for value_list in _dict_result_for_part_1.values():
        for i in value_list:
            get_value = _dict.get(i)
            if get_value == None:
                wait_add = eval("{'"+str(i)+"':1}")
                _dict.update(wait_add)
            else :
                _dict[i]=_dict[i]+1
    return _dict

from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
from os import *
if __name__ == '__main__':
    # os.getcwd()
    filepath = ["D:\\github\TiantianFund-CaleScript\INFORMATION_AND_ATTACHMENT\基金文件\个人基金.txt",'D:\\github\TiantianFund-CaleScript\INFORMATION_AND_ATTACHMENT\基金文件\媳妇基金.txt']
    rfi_list = []
    for file_i in filepath:
        rfi = read_file_inline(file_i)
        for i in range(int(len(rfi)/6)):
            result = rfi[i:i+6]
            rfi_list.append(result)
    print(rfi_list)
    _dict_string = ''
    for i in rfi_list:
        _dict_string = _dict_string + str(i)
    _dict_result_for_part_1 = eval('{' + _dict_string + '}')
    _dict = {}
    _list = []
    print(type(_dict))
    for value_list in _dict_result_for_part_1.values():
        for i in value_list:
            get_value = _dict.get(i)
            if get_value == None:
                wait_add = eval("{'"+str(i)+"':1}")
                _dict.update(wait_add)
            else :
                _dict[i]=_dict[i]+1
    print(_dict)