"""
单只基金数据拆分脚本
适用于天天基金数据接口传入的数据
***************************************
[基金详细信息：]
http://fund.eastmoney.com/pingzhongdata/[基金代号].js?v=20160518155842
"""
from common_module_and_fuction.base_request import base_request
from common_module_and_fuction.adjust_string import *
from fundition_static_packaging.change_Tiantian_return_value_2_usable import *
import datetime

#数据传入封装
def singleness_fund_inquire(fund_code_inquire) :
    c = fund_code_inquire
    a = base_request('http://fund.eastmoney.com/pingzhongdata/'+c+'.js?v=20160518155842')
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
#基金持仓股票代码
#['1280282']
def cut_stock_date(fund_date):#基金持仓股票代码
    a = find_and_cut(str(fund_date), 'var stockCodes=', '/*基金持仓债券代码*/')
    a = format_removeal(a)
    a = Data_stockThrend(a)
    return a


# 基金债券持仓代码
# ['1280282']
def cut_bond_date(fund_date):#基金持仓债券代码
    a= find_and_cut(str(fund_date),'zqCodes=','/*收益率*/')
    a = format_removeal(a)
    a = Data_bondThrend(a)
    return a


#单位净值走势
#{'1310486400000': {'y': 1.0, 'equityReturn': 0, 'unitMoney': ''}}
def cut_trend_date(fund_date):#单位净值走势
    a = format_removeal(fund_date)
    a = find_and_cut(a, 'varData_netWorthTrend=', '/*累计净值走势*/')
    a = format_removeal(a)
    fund_date_result= Data_netWorthTrend(a)
    return fund_date_result


# /*累计净值走势*/
#传入天天基金全部数据，返回累计净值走势
#{'1310486400000':{'ACWorthTrend':1.0}}
def cut_Data_ACWorthTrend(fund_date):
    a= format_removeal(fund_date)
    a = find_and_cut(a,"/*累计净值走势*/","/*累计收益率走势*/")
    a = find_and_cut(a,"varData_ACWorthTrend=",";")
    # print(a)
    a=Data_ACWorthTrend(a)
    return a


#所有基金code
#传入地址http://fund.eastmoney.com/js/fundcode_search.js
#返回值为该地址内所有数据报出的基金代码
def all_fundcode_2_list():
    backdate = base_request('http://fund.eastmoney.com/js/fundcode_search.js')
    backdate = format_removeal(str(backdate))
    backdate = find_and_cut(backdate,'﻿varr=',';')
    backdate =backdate.replace('[[','[').replace(']]',']')
    whilecode = 1
    _list = []
    while(whilecode==1):
        b = backdate.find('[')
        if b == -1:
            whilecode = 2
        else:
            b=b+2
            c = b+6
            result = backdate[b:c]
            _list.append(result)
            d =backdate.find('],[')+2
            backdate=backdate[d:]
    return _list

if __name__ == '__main__':
    a = all_fundcode_2_list()
    print(a)
    print(len(a))