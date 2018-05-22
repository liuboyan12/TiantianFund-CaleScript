"""
批量均线分析脚本：

1.离20日均线远逢高卖出部分（展示离日均线比率）
2.三次达到20日均线卖出一半提示
3.跌破60清仓提示
4.高于买入价格百分之20减仓提醒
阻力点/支撑点——股票回调或者反弹的点的切线


"""
def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()

from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import *


def Dailyline_20_forecast(fundcode,dailyline = 20):
    _dict = singleness_fund_inquire(fundcode)
    result_dict = cut_Data_ACWorthTrend(_dict)

    # 将最上面字典里面的unix时间戳转换为2018-06-03的格式
    def changeUnixTime(_dict):
        time_list = _dict.keys()
        new_dict = {}
        for i in time_list:
            _string = ''
            datetime_num = str(msUnix_2_datetime(i))
            _string = "{'" + datetime_num + "':" + str(result_dict[i]) + "}"
            _part_dict = eval(_string)
            new_dict.update(_part_dict)
        return new_dict

    # 获得基金趋势值
    _self_dict = changeUnixTime(result_dict)
    latest_kv = getLastDict(_self_dict)[1]
    latest_kv_value = latest_kv['ACWorthTrend']
    # 比较最新时间是否与取到的数据一致
    # 今日的及时数据获取
    latest_date1 = request_part(fundcode)
    c = made_date(latest_date1)
    # 今日预期净值
    latest_date = latest_kv_value * (1.0 + float(c[2]) / 100)
    # 今日预期净值拼装到净值dict后
    made_dict = eval("{'" + str(c[4]) + "':{'ACWorthTrend':" + str(round(latest_date,4)) + "}}")
    _self_dict.update(made_dict)
    # 预测今日日均线
    forecast_daily_line = daily_line_dict_assembly_ACWorthTrend(_self_dict, dailyline)
    forecast_daily_line = getLastDict(forecast_daily_line)
    forecast_daily_line = eval("{" + str(forecast_daily_line).replace("(", "").replace(")", "").replace(",", ":") + "}")
    # 今日预期值
    forecast_ACWorthTrend = made_dict
    # 超出今日预测20日均线比率
    today_date = c[4]
    a = forecast_ACWorthTrend[today_date]['ACWorthTrend']
    second_key = str(dailyline)+'dailyLine'
    b = forecast_daily_line[today_date][second_key]
    rate = round((a - b) / b, 3) * 100
    result1=round(rate,4)
    result2=round(a-b,4)
    result3= c[0] + '  今日预测值与二十日日均线差距比例为' + str(round(rate,4)) + '%'
    return result1,result2,_self_dict,result3


def Dailyline_60_warning(fundcode):
    warning_60 = Dailyline_20_forecast(fundcode,60)[0]
    if warning_60<=0:
        print("本基金已经跌破60日均线")
    # print(warning_60)

def MaiRuZhi_20percent_warning(fundcode,in_time='2018-01-02'):
    MaiRuZhi_20 = Dailyline_20_forecast(fundcode)[2]
    in_time_price = MaiRuZhi_20[in_time]['ACWorthTrend']
    # print('买入价值：'+str(in_time_price))
    now_prices=eval(str(getLastDict(MaiRuZhi_20)[1]))['ACWorthTrend']
    # print('最新预期：'+str(now_prices))
    warning_line = (now_prices-in_time_price)/in_time_price
    if warning_line>=0.2:
        print(str(fundcode)+' 基金已经超越买入时累计净值的百分之20，减仓提醒')

"""
组合使用方法，把上面的东西综合起来用
"""
def comprehensive_fundition(fundcode,in_time):
    a = Dailyline_20_forecast(fundcode)[3]
    b = Dailyline_20_forecast(fundcode)[1]
    print(a)
    print("差值：",b)
    Dailyline_60_warning(fundcode)
    MaiRuZhi_20percent_warning(fundcode, in_time)

# def dailyline_ACWorthTrendLine_cross(fundcode,in_time='2018-01-02'):





if __name__ == '__main__':

    fundcode = '002001'
    in_time = '2018-04-10'
    # diction = 'left'
    diction = 'right'
    _dict = Dailyline_20_forecast(fundcode)[2]
    a=dict_JieQuBanDuan(_dict,in_time)
    print(a)





    # tprint(final_dict)








