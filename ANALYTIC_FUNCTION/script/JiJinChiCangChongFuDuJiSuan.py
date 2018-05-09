from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *

"""
传入值
"""
"""
获取股票数据，输入基金code，该基金目前的股票数据
"""
def stock_list(fundcode):
    _date = singleness_fund_inquire(fundcode)
    _result = cut_stock_date(_date)
    return _result


""""传入基金6位代码list，计算天天基金接口下的股票重复度"""
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

def ChongFuDuQuanZhong(_list=[],_dict={}):
    for i in _list:
        ifcode = _dict.get(i)
        _string = ''
        if ifcode == None:
            _string ="{'"+i+"':1}"
            ready_dict = eval(_string)
            _dict.update(ready_dict)
            # print(ready_dict,type(ready_dict))
        else:
            _dict[i]=_dict[i]+1
    return _dict


from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *
import os
if __name__ == '__main__':

    # pwd = os.getcwd()
    # pwd = pwd.replace(":\\", ':\\\\')
    # filepath_all = pwd + '\INFORMATION_AND_ATTACHMENT\基金文件\\'
    # filename=['个人基金.txt','媳妇基金.txt']
    # filepath = [filepath_all + filename[0], filepath_all + filename[1]]
    # rfi_list = []
    # for file_i in filepath:
    #     rfi = read_file_inline(file_i)
    #     for i in range(int(len(rfi)/6)):
    #         result = rfi[i*6:i*6+6]
    #         rfi_list.append(result)
    # print(type(rfi_list),rfi_list)
    # result = ChongFuDuQuanZhong(rfi_list)
    # print(result)
    print()
