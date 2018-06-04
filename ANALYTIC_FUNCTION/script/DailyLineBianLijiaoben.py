from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.time_exchange import *
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import daily_line_dict_assembly_ACWorthTrend as GO
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import find_max_or_min_in_list as max_some,value_2_key,find_dict_key_and_fetch_value_to_list,dict_cut_out_piece_in_sequence

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

# 输入基金code和买入的日期start_day和持有周期长度long（交易日的个数）可以计算
# 得到该基金出现涨幅超过20日均线多少的时候取的最大收益/最小收益max_or_min
# 也可以选择输出多个值_quzhigeshu

def daily_line_analyze(fundcode,start_day,long=30,_quzhigeshu=3,max_or_min='max'):
    while 1<2:
        try:
            backdate = singleness_fund_inquire(fundcode)
            AN_lib = cut_Data_ACWorthTrend(backdate)
            AN_lib = changeUnixTime(AN_lib)
            #数据转换

            Tr_lib = list(AN_lib.keys())
            Tr = start_day

            AN_Tr = AN_lib[Tr]['ACWorthTrend']
            _dict = {}
            for T in Tr_lib:
                AN = AN_lib[T]['ACWorthTrend']
                AN_input = round(AN - AN_Tr, 4)
                _string = "{'" + str(T) + "':" + str(AN_input) + "}"
                _dict.update(eval(_string))# 时间--收益
            DL20 = GO(AN_lib, 20)
            DL_list = list(DL20.keys())
            DL20_lib = {}
            for i in DL_list:
                _value = DL20[i]['20dailyLine']
                real_value = AN_lib[i]['ACWorthTrend']
                rate = round((real_value - _value) / real_value, 4)
                _string = eval("{'" + i + "':" + str(rate) + "}")
                DL20_lib.update(_string)
            # 时间--日均线差值比率

            DL_20_final =dict_cut_out_piece_in_sequence(DL20_lib,Tr,long)
            _dict_final = dict_cut_out_piece_in_sequence(_dict,Tr,long)
            _dict_final_value = list(_dict_final.values())

            a = max_some(_dict_final_value,_quzhigeshu, max_or_min)
            key_list = []
            for i in a:
                key_list_append = value_2_key(_dict_final, i)
                key_list.append(key_list_append)
            # 选取区间内最大收益反推该收益的key
            DL20_max_or_min_list = find_dict_key_and_fetch_value_to_list(DL_20_final, key_list)
            example="出现收益最大/最小的20日日均线离线值为："
            for i in DL20_max_or_min_list:
                example= example+str(i)+" , "
            example=example[:-3]
            break
        except Exception as e:
            continue
    return DL20_max_or_min_list,example


if __name__ == '__main__':
    import os

    pwd = os.getcwd()
    pwd = pwd.replace(":\\", ':\\\\')
    filepath = pwd+'\INFORMATION_AND_ATTACHMENT\基金文件\均线最大收益均值结果\均线最大收益.txt'
    f = open(filepath, "w")
    # ['519772', '110013',
    _list1 = ['161725','165312','000619']
    for fundcode in _list1:

        trade_date = fund_trade_date(fundcode)
        #近两年数据吧，例如易方达那个，有九年数据就很吓人了啊

        # tprint(trade_date)
        average_list = []
        _strings=''
        dayslong=60
        trade_date=trade_date[:-60]
        for i in trade_date:
            print(fundcode,":",i)
            a=daily_line_analyze(fundcode,i,dayslong)[0]
            # tprint(a)
            for ai in a:
                average_list.append(ai)
        # tprint(average_list)
            # average_list.append(str(a))
        maxvalue = max(average_list)
        while 1<2:
            try:
                whilenum = average_list.index(maxvalue)
                # tprint(whilenum)
                average_list.remove(maxvalue)
            except:
                break
        minvalue = min(average_list)
        while 1 < 2:
            try:
                whilenum = average_list.index(minvalue)
                # tprint(whilenum)
                average_list.remove(minvalue)
            except:
                break
        lenth=float(len(average_list))
        # tprint(lenth)
        sum = float(0)
        for ali in average_list:
            print(fundcode,":",ali)
            sum = sum+float(ali)
            # tprint(sum)
        result = round(sum/lenth,4)
        print(fundcode,':',result,file= f)
        print("历史最大值为:",maxvalue)

    f.close()


