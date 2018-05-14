"""
批量均线分析脚本：

初期需求：获取最新数据，进行已有数据进行分析


"""
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import *

if __name__ == '__main__':
    # _dict = singleness_fund_inquire('002001')
     # _dict = cut_Data_ACWorthTrend(_dict)
    _dict = eval("{'1525795200000': {'ACWorthTrend': 4.482}, '1525881600000': {'ACWorthTrend': 4.498}, '1525968000000': {'ACWorthTrend': 4.487}}")
    time_list=_dict.keys()
    new_dict = {}
    # print(_dict,type(_dict))
    for i in time_list:
        _string = ''
        datetime_num = str(msUnix_2_datetime(i))
        # print(datetime_num,type(datetime_num))
        _string = "{'"+datetime_num+"':"+str(_dict[i])+"}"
        _part_dict = eval(_string)
        # print(_string)
        new_dict.update(_part_dict)
        # print(new_dict)
    a = daily_line_dict_assembly_test(new_dict, 20)
    print(a)

    #{'2018-05-09':{'20dailyLine':4.48},'2018-05-10':{'20dailyLine':4.49},'2018-05-11':{'20dailyLine':4.49}}

    # 目前问题在于这样取到的数据没有最新的，没法对应实施实时控制，所以要取到今天的数据进行一起的拼装