from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
#均线计算函数
#传入参数：_list:列，_days:所求的均线个数
#例如传入值为['1','2','3','4','5'](_list),计算3位(_days)均线
# a = moving_average_calc(['1', '2', '3', '4', '5'],3)
#返回值为：[1.0, 1.5, 2.0, 3.0, 4.0]
"""均线计算函数,传入值list,int,传出值list"""
def moving_average_calc(_list,_days):
    return_result = []
    for wei in range(len(_list)):
        result = 0
        _days_code = float(_days)
        if wei <_days:
            _days_code = wei+1
        else:
            pass
        for i in range(int(_days_code)):
            result = result + float(_list[wei - i])
        return_value = round(float(result) / float(_days_code),2)
        return_result.append(return_value)
    return return_result


# \\日均线计算函数\\
# 该函数输入dict，几日日均线days，输出输入dict的内所存在的所有日期的days日日均线
# 输入数据格式：
# {'1310486400000': {'y': 1.0, 'equityReturn': 0, 'unitMoney': ''},
# '1310659200000': {'y': 1.0, 'equityReturn': 0.0, 'unitMoney': ''}}
# 返回值为按照dict的keys()对应list的日均线值
"""\\天天基金日均线计算函数\\：传入值dict，传出值list"""
def daily_line_calc(_dict,days):
    a = _dict
    _list = a.keys()
    ACWorthTrend_list = []
    for key in _list :
        ACWorthTrend_list.append(a[key]['ACWorthTrend'])
    ACWorthTrend_daily_line = moving_average_calc(ACWorthTrend_list,days)
    return ACWorthTrend_daily_line,

#     \\日均线——字典拼装函数\\
#     传入值为天天基金数据的字典,该函数可以将计算得到的日均线值放入到
#     原来的字典内，添加在原字典的后面添加键值对{'20dailyLine': -0.1002}
#     传入的_dict被修改为添加了日均线键值对的_dict

#     _variable_value为list，一般为日均线计算函数传出的同_dict的计算值
#     days为int型，一般为 日均线计算函数 传入的同days值
#
#     该函数自动将写好的日均线拼装进原函数中
"""\\天天基金[累计净值走势]日均线——字典拼装函数\\"""
def daily_line_dict_assembly_ACWorthTrend(_dict,days):
    a = _dict
    # a=eval(cut_Data_ACWorthTrend(a))
    ACWorthTrend_list = []
    for key in a :
        ACWorthTrend_list.append(a[key]['ACWorthTrend'])
    ACWorthTrend_daily_line = moving_average_calc(ACWorthTrend_list,days)
    # print("ACWorthTrend_daily_line",ACWorthTrend_daily_line)#——计算日均线，
    # 拼装
    _dict_assembly = ''
    i_plusplus_code = 0
    _list_assembly = []
    _name = str(days)+'dailyLine'#————————
    i_code = 0
    for key in a:
        _string = "'"+str(key)+"':{'"+_name+"':"+str(ACWorthTrend_daily_line[i_code])+"},"
        _list_assembly.append(_string)
        i_code = i_code+1
    _list_2_dict = ''
    for i in range(len(_list_assembly)):
        _list_2_dict = _list_2_dict+str(_list_assembly[i])
    _string = "{"+str(_list_2_dict)+"}"
    _string = _string.replace("},}","}}")
    # print(_string)
    _string = eval(_string)
    return _string

if __name__ == '__main__':
    _dict = singleness_fund_inquire('002001')
    _dict = cut_Data_ACWorthTrend(_dict)
    a= daily_line_dict_assembly_ACWorthTrend(_dict,3)
    print(type(a),a)



