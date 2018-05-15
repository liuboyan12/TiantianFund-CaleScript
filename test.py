"""
批量均线分析脚本：

初期需求：获取最新数据，进行已有数据进行分析


"""
def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()


from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import *

if __name__ == '__main__':
    # _dict = singleness_fund_inquire('002001')
    # result_dict = cut_Data_ACWorthTrend(_dict)
    result_dict = eval("{'1525795200000': {'ACWorthTrend': 4.482}, '1525881600000': {'ACWorthTrend': 4.498}, '1525968000000': {'ACWorthTrend': 4.487}}")

    #将最上面字典里面的unix时间戳转换为2018-06-03的格式
    def changeUnixTime(_dict):
        time_list=_dict.keys()
        new_dict = {}
        for i in time_list:
            _string = ''
            datetime_num = str(msUnix_2_datetime(i))
            _string = "{'"+datetime_num+"':"+str(result_dict[i])+"}"
            _part_dict = eval(_string)
            new_dict.update(_part_dict)
        return new_dict


    _self_dict = changeUnixTime(result_dict)
    latest_kv = getLastDict(_self_dict)[1]
    latest_kv_value = latest_kv['ACWorthTrend']

    #比较最新时间是否与取到的数据一致
    # 今日的及时数据获取

    # latest_date = request_part('002001')
    # c = made_date(latest_date)
    # print('c',c)
    c=['','','0.31','15','2018-05-15']
    print(c[2],c[4])

    #今日预期净值
    latest_date = latest_kv_value*(1.0+float(c[2]))
    #今日预期净值拼装到净值dict后
    made_dict = eval("{'"+str(c[4])+"':{'ACWorthTrend':"+str(latest_date)+"}}")
    _self_dict.update(made_dict)
    #预测今日日均线
    forecast_daily_line = daily_line_dict_assembly_ACWorthTrend(_self_dict,20)
    forecast_daily_line = getLastDict(forecast_daily_line);tprint(forecast_daily_line)




    #{'2018-05-09':{'20dailyLine':4.48},'2018-05-10':{'20dailyLine':4.49},'2018-05-11':{'20dailyLine':4.49}}

    # 目前问题在于这样取到的数据没有最新的，没法对应实施实时控制，所以要取到今天的数据进行一起的拼装