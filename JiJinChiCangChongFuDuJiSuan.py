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
    """
    code_list = ['002001','070001']
    result_list = []
    for i in code_list:        #002001
        passcode = 0
        while(passcode<1):
            try:
                _stock_list=stock_list(i)    #"['0008582', '0003332', '6011551', '0005682', '6038331', '6002761', '0020432', '0007862', '0009632', '6038161']"
                #{'002001':[]}
                _stock_list = "'"+i+"':"+str(_stock_list)+','

                passcode = 1
            except Exception as e :
                pass
        result_list.append(_stock_list)
        """
    #<urlopen error [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。>
    result_list = eval("{'002001':['0003332', '0008582'],'002002':[ '0003332', '6011551']}")
    # print(type(result_list)
    _dict_key = list(result_list.keys())
    # print(type(_dict_key))
    _result_dict = {}
    for i in _dict_key:
        ifcode  = _dict_key.index(i)
        if ifcode == 0:
            creat_list = result_list[_dict_key[1]]
            for i in creat_list:
                print(i)
                _string = str(i)+':1'
                print(_string)
                _result_dict.update(_string)
            print(_result_dict)

            # print(_result_dict)
        # print(_dict_key[i])
    #     # print(ifcode)
        # print(result_list[_dict_key[i]])



    # print(result_list[0])



    # print(_stock_list)
    #     stock_list =eval( "['0008582', '0003332', '6011551', '0005682', '6038331', '6002761', '0020432', '0007862', '0009632', '6038161']")
    # print(len(result_list))