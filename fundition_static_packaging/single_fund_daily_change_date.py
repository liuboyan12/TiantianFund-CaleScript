"""
#单一基金日收益查询
# daily_change_date(fund_code,start_time,end_time)
"""

from common_module_and_fuction.base_request import *
from fundition_static_packaging.change_Tiantian_return_value_2_usable import *
from common_module_and_fuction.time_exchange import *

# 传入参数fund_code:6位基金代码,start_time:开始时间,end_time:结束时间
# 开始时间和结束时间接受非交易日时间自动查找时间内时间
# 时间格式为str'2018-01-01'
def daily_change_date(fund_code,start_time,end_time):

    c = str(fund_code)
    a = base_request('http://fund.eastmoney.com/pingzhongdata/' + c + '.js?v=20160518155842')
    a = a[a.find('/*单位净值走势 equityReturn-净值回报 unitMoney-每份派送金*/')+len('/*单位净值走势 equityReturn-净值回报 unitMoney-每份派送金*/'):a.find('/*累计净值走势*/')]
    a = a[a.find('var Data_netWorthTrend = [')+25:a.find(']')+1]
    a = Data_netWorthTrend(a)#直接转成字典的方法
    list1 = list(a.keys())
    import_start_datetime = str(start_time)
    starttime_2_unix = str(datetime_2_msUnix(str_2_datetime(import_start_datetime)))
    import_end_datetime = str(end_time)
    endtime_2_unix = str(datetime_2_msUnix(str_2_datetime(import_end_datetime)))
    out_put_list = {}
    for i in range(int((float(endtime_2_unix)-float(starttime_2_unix))/86400000)):
        try_code = 2
        try:
            null_value = list1.index(str(starttime_2_unix))
        except ValueError:
            try_code = 1
        if try_code != 1:
            out_put_value = eval('{'+starttime_2_unix+':'+str(a[starttime_2_unix])+'}')
            out_put_list.update(out_put_value)
        starttime_2_unix = str(int(starttime_2_unix)+86400000)
    return out_put_list


if __name__ == '__main__':
    a= daily_change_date('377240',"2018-01-01","2018-04-04")
    print(a)