from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import singleness_fund_inquire as dwdata ,cut_Data_ACWorthTrend
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import dict_value_average_line
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num
import time
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import single_fund_date


def make_base_date_for_dailyline(fundcode):
    date_value_dict = {}
    def make_date_value_dict(fundcode):
        #制作时间：值函数方便计算日均线date_value_dict
        dataACWorthTrend = cut_Data_ACWorthTrend(dwdata(fundcode))
        datelist = list(dataACWorthTrend.keys())
        dicts={}
        for i in datelist:
            value = dataACWorthTrend[i]['ACWorthTrend']
            partdict = {i:value}
            dicts.update(partdict)
        return dicts
    def daysUnix():
        #获取今日的时间戳（今日0时）
        now_time = int(time.time())
        day_time = now_time - now_time % 86400 + time.timezone
        unix=str(day_time)+"000"
        return unix
    def getTodayValue(fundcode,dict):
        #获取今日的基金的ACWorthTrend
        todayRate = single_fund_date(fundcode)[2]
        lastnum = len(dict)
        todayValue = float(list(fetch_dict_by_num(date_value_dict, lastnum).values())[0])*float(todayRate)
        return todayValue

    date_value_dict=make_date_value_dict(fundcode)
    taildict = {daysUnix():getTodayValue(fund,date_value_dict)}
    date_value_dict.update(taildict)
    return date_value_dict

def pick_rule(linerule):
    nowstring = linerule
    lists = []
    while(1<2):
        try:
            a = nowstring.index("-")
        except Exception:
            a = -1
        if a==-1:
            break
        else:
            prlist = nowstring[:a]
            lists.append(prlist)
            nowstring = nowstring[a+1:]
    lists.append(nowstring)
    return lists


if __name__ == '__main__':

    ruledict = {"110022": "30-90-20-120"}

    for i in range(len(ruledict)):
        fund = list(ruledict.keys())[i]
        rule = list(ruledict.values())[i]
    listrules = pick_rule(rule)#[]

    _dateDict = make_base_date_for_dailyline("002001")

    in_line1 = dict_value_average_line(_dateDict,listrules[0])
    in_line2 = dict_value_average_line(_dateDict,listrules[1])
    # out_line1 = dict_value_average_line(_dateDict,listrules[2])
    # out_line2 = dict_value_average_line(_dateDict,listrules[3])

    print(in_line1)