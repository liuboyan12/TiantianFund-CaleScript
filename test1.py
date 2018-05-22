from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import daily_line_dict_assembly_ACWorthTrend as GO

def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            print()

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


if __name__ == '__main__':
    #
    # fundcode = '002001'
    # backdate = singleness_fund_inquire(fundcode)
    # AN_lib=cut_Data_ACWorthTrend(backdate)
    # AN_lib = changeUnixTime(AN_lib)
    AN_lib = eval("{'2018-04-23': {'ACWorthTrend': 4.412}, '2018-04-24': {'ACWorthTrend': 4.442}, '2018-04-25': {'ACWorthTrend': 4.442}, '2018-04-26': {'ACWorthTrend': 4.415}, '2018-04-27': {'ACWorthTrend': 4.414}, '2018-05-02': {'ACWorthTrend': 4.421}, '2018-05-03': {'ACWorthTrend': 4.44}, '2018-05-04': {'ACWorthTrend': 4.438}, '2018-05-07': {'ACWorthTrend': 4.473}, '2018-05-08': {'ACWorthTrend': 4.485}, '2018-05-09': {'ACWorthTrend': 4.482}, '2018-05-10': {'ACWorthTrend': 4.498}, '2018-05-11': {'ACWorthTrend': 4.487}, '2018-05-14': {'ACWorthTrend': 4.503}, '2018-05-15': {'ACWorthTrend': 4.511}, '2018-05-16': {'ACWorthTrend': 4.507}, '2018-05-17': {'ACWorthTrend': 4.488}, '2018-05-18': {'ACWorthTrend': 4.496}, '2018-05-21': {'ACWorthTrend': 4.497}}")
    # tprint(AN_lib)
    Tr_lib = list(AN_lib.keys())
    # tprint(Tr_lib)
    Tr = "2018-04-23"#______这里还是要控制下的我们可以计算的是任意一天一个月的最大收益平均
    T = ''
    AN_Tr = AN_lib[Tr]['ACWorthTrend']

    tprint(AN_Tr)
    _dict = {}
    for T in Tr_lib:
        AN = AN_lib[T]['ACWorthTrend']
        AN_input = round(AN-AN_Tr,4)
        _string = "{'"+str(T)+"':"+str(AN_input)+"}"
        _dict.update(eval(_string))
    #时间--收益

    DL20 = GO(AN_lib,20)
    DL_list = list(DL20.keys())
    DL20_lib = {}
    for i in DL_list:
        _value=DL20[i]['20dailyLine']
        real_value=AN_lib[i]['ACWorthTrend']
        rate = round((real_value-_value)/real_value,4)
        _string = eval("{'"+i+"':"+str(rate)+"}")
        DL20_lib.update(_string)
    # 时间--日均线差值比率

    tprint(DL20_lib)
    tprint(_dict)



