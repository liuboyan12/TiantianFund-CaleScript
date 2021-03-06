"""
天天基金数据处理
适用于天天基金数据接口传入的数据
***************************************
[基金详细信息：]
http://fund.eastmoney.com/pingzhongdata/[基金代号].js?v=20160518155842
[所有基金名称列表代码：]
http://fund.eastmoney.com/js/fundcode_search.js
"""
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.base_request import base_request
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.adjust_string import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
# 数据传入封装
def singleness_fund_inquire(fund_code_inquire):
    c = fund_code_inquire
    a = base_request('http://fund.eastmoney.com/pingzhongdata/' + c + '.js?v=20160518155842')
    return a
"""
天天基金接口传出数据切分与处理:

\\基金股票持仓数据\\
cut_stock_date()
    传入值：天天基金传出所有数据
    返回值：list，list值为基金持有股票的值
    例：['3452313','1234123','2313414']

\\基金债券持仓数据\\
cut_bond_date()
    传入值：天天基金传出所有数据
    返回值：list，list值为基金持有债券的值
    例：['1234123','2313414']

\\单位净值走势\\
cut_trend_date()
    传入值：天天基金传出所有数据
    返回值：dict，dict值为
    例：
    {'unix时间':
        {
            "y":1.0,"equityReturn":0,"unitMoney":""
        }
    }
\\累计净值走势\\
cut_Data_ACWorthTrend()
传入天天基金全部数据，返回累计净值走势
{'1310486400000':{'ACWorthTrend':1.0}}

"""



def cut_stock_date(fund_date):  # 基金持仓股票代码
    """
    # 基金持仓股票代码
    # ['1280282']
    :param fund_date:
    :return:
    """
    a = find_and_cut(str(fund_date), 'var stockCodes=', '/*基金持仓债券代码*/')
    a = format_removeal(a)
    def Data_stockThrend(return_value):
        return_value = return_value.replace(' ', '').replace('"', "'").replace(';', '').replace('[', '').replace(';', '')
        return_value = eval('['+return_value)
        return return_value
    a = Data_stockThrend(a)
    return a



def cut_bond_date(fund_date):  # 基金持仓债券代码
    """
    # 基金债券持仓代码
    # ['1280282']
    :param fund_date:
    :return:
    """
    a = find_and_cut(str(fund_date), 'zqCodes=', '/*收益率*/')
    a = format_removeal(a)
    def Data_bondThrend(return_value):
        return_value = return_value.replace(' ', '').replace('"', "").replace(';', '').replace('[', '').replace(']', '')
        target_list = [i for i in return_value.split(',')]
        return target_list

    a = Data_bondThrend(a)
    return a


def cut_trend_date(fund_date):  # 单位净值走势
    """
    # 单位净值走势
    # {'1310486400000': {'y': 1.0, 'equityReturn': 0, 'unitMoney': ''}}
    :param fund_date:
    :return:
    """
    a = format_removeal(fund_date)
    a = find_and_cut(a, 'varData_netWorthTrend=', '/*累计净值走势*/')
    a = format_removeal(a)
    def Data_netWorthTrend(return_value):
        p = return_value.replace('},{"x":', '},')
        p = p.replace('{"x":', '').replace(',"y"', ':{"y"').replace(']', '}').replace('[', "{'").replace('"',"'").replace("},", "},'").replace(":{'y'", "':{'y'").replace(";", "")
        p = eval(p)
        return p
    fund_date_result = Data_netWorthTrend(a)
    return fund_date_result



def cut_Data_ACWorthTrend(fund_date):
    """
    /*累计净值走势*/
    传入天天基金全部数据，返回累计净值走势
    {'1310486400000':{'ACWorthTrend':1.0}}
    :param fund_date:
    :return:
    """
    a = format_removeal(fund_date)
    a = find_and_cut(a, "/*累计净值走势*/", "/*累计收益率走势*/")
    a = find_and_cut(a, "varData_ACWorthTrend=", ";")
    def Data_ACWorthTrend(return_value):
        return_value = return_value.replace("[[", "[['").replace(",", "',").replace("',[", ",['").replace(",", ":").replace("]:[","],[").replace("[", "{").replace("]", "}")
        return_value = return_value.replace("}}", "}}}").replace(":", ":{'ACWorthTrend':").replace("},", "}},")
        return_value = return_value.replace("{{'", "{'").replace("}},", "},").replace(",{'", ",'").replace("}}}", "}}")
        return return_value
    a = eval(Data_ACWorthTrend(a))
    return a



def all_fundcode_2_list():
    """
    所有基金code
    传入地址http://fund.eastmoney.com/js/fundcode_search.js
    返回值为该地址内所有数据报出的基金代码
    :return:
    """
    backdate = base_request('http://fund.eastmoney.com/js/fundcode_search.js')
    backdate = format_removeal(str(backdate))
    backdate = find_and_cut(backdate, '﻿varr=', ';')
    backdate = backdate.replace('[[', '[').replace(']]', ']')
    whilecode = 1
    _list = []
    while (whilecode == 1):
        b = backdate.find('[')
        if b == -1:
            whilecode = 2
        else:
            b = b + 2
            c = b + 6
            result = backdate[b:c]
            _list.append(result)
            d = backdate.find('],[') + 2
            backdate = backdate[d:]
    return _list


def fund_trade_date(fundcode):
    """
    #基金交易日日期数据
    :param fundcode:
    :return:
    """
    backdate = singleness_fund_inquire(fundcode)
    AN_lib = cut_Data_ACWorthTrend(backdate)
    def changeUnixTime(_dict):
        result_dict = _dict
        time_list = _dict.keys()
        new_dict = {}
        for i in time_list:
            _string = ''
            datetime_num = str(msUnix_2_datetime(i))
            _string = "{'" + datetime_num + "':" + str(result_dict[i]) + "}"
            _part_dict = eval(_string)
            new_dict.update(_part_dict)
        return new_dict
    AN_lib = changeUnixTime(AN_lib)
    return list(AN_lib.keys())

def fund_name(fundcode):
    """
    基金名称
    :param fundcode:
    :return:
    """
    a = singleness_fund_inquire(fundcode)
    a=find_and_cut(a,'var fS_name = "','";var fS_code ')
    return a

if __name__ == '__main__':
    a = singleness_fund_inquire("163402")
    a= cut_Data_ACWorthTrend(a)
    print(a)
