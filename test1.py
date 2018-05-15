'519697'
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import *
#
# _dict = singleness_fund_inquire('519697')
# _dict = cut_Data_ACWorthTrend(_dict)
# a = eval(daily_line_dict_assembly_test(_dict, 20))
# _list = list(a.keys())
# print(type(_list))
# print(type(a), a[_list[-1]])

if __name__ == '__main__':
    _dict = singleness_fund_inquire('002001')
    result_dict = cut_Data_ACWorthTrend(_dict)
    print(result_dict)
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
    #判断最新数据与获取的数据时间
    _self_dict = changeUnixTime(result_dict)
    print('_self_dict:',_self_dict)


    #{'ACWorthTrend': 4.487}, '2018-05-14': {'ACWorthTrend': 4.503}}
    #从此可以看到数据只有昨日的数据没有今日的数据的，最新的计算数据要到明天需要加入时间判断