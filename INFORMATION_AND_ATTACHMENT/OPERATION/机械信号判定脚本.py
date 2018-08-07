from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import singleness_fund_inquire as dwdata ,cut_Data_ACWorthTrend
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import dict_value_average_line
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num
import time
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import single_fund_date

"""
机械信号判定脚本：
    根据机械交易计算脚本跑出数据{"110022": "30-90-20-120"}
    对实际的每日数据进行计算，判断到当前基金"110022"存在30日均线自下而上突破90日均线时
    进行买入提醒，当20日均线跌破120日均线时候，进行卖出提醒，并加有返回值，方便储存
"""

def make_base_date_for_dailyline(fundcode):
    date_value_dict = {}
    def make_date_value_dict(fundcode):
        #制作时间：值函数方便计算日均线date_value_dict
        while 1<2:
            try:
                dataACWorthTrend = cut_Data_ACWorthTrend(dwdata(fundcode))
                datelist = list(dataACWorthTrend.keys())
                dicts={}
                for i in datelist:
                    value = dataACWorthTrend[i]['ACWorthTrend']
                    partdict = {i:value}
                    dicts.update(partdict)
                break
            except:
                time.sleep(10)
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
    taildict = {daysUnix():getTodayValue(fundcode,date_value_dict)}
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

def runner(ruledict,printControl=0):
    """
    传入机械交易脚本的键值对{"110022": "30-90-20-120"}
    对今日基金进行检测，如果存在买入或者卖出的信号将进行提示
    并返回一个今日数据的数据字典
    :param ruledict:{"110022": "30-90-20-120"}
    printControl:打印控制，如果为1(int)打印其他值都不打印
    :return:retDict:{'110022': {'Date': '1533052800000', 'buyIn': 'None', 'sellOut': 'None'}
    """
    retDict = {}
    for i in range(len(ruledict)):
        fund = list(ruledict.keys())[i]
        rule = list(ruledict.values())[i]
        listrules = pick_rule(rule)#[]
        _dateDict = make_base_date_for_dailyline(fund)
        in_line1_s = dict_value_average_line(_dateDict,listrules[0])
        in_line2_l = dict_value_average_line(_dateDict,listrules[1])
        out_line1_s = dict_value_average_line(_dateDict,listrules[2])
        out_line2_l = dict_value_average_line(_dateDict,listrules[3])
        def take_last_3_keyvalue(dayline):
            _list = list(dayline.keys())[-3:]
            _returnDict = {}
            for i in _list:
                _value = dayline[i]
                _pardict={i:_value}
                _returnDict.update(_pardict)
            return _returnDict
        recent_date1 = take_last_3_keyvalue(in_line1_s)
        recent_date2 = take_last_3_keyvalue(in_line2_l)
        recent_date3 = take_last_3_keyvalue(out_line1_s)
        recent_date4 = take_last_3_keyvalue(out_line2_l)
        def recent_data_judge(_dict1_long,_dict2_short,judgeCode="ABX"):
            _controlList = list(_dict1_long.keys())
            middleKey = _controlList[1]
            A1 = float(_dict1_long[_controlList[1]])
            B1 = float(_dict2_short[_controlList[1]])
            A2 = float(_dict1_long[_controlList[2]])
            B2 = float(_dict2_short[_controlList[2]])
            if float(_dict1_long[middleKey])-float(_dict2_short[middleKey])==0:
                A1=float(_dict1_long[_controlList[0]])
                B1=float(_dict2_short[_controlList[0]])
            else:
                firstValue = A1 - B1
                nextValue = A2 - B2
                if judgeCode=="ABX":
                    if firstValue>0 and nextValue<0:
                        return "ABX"
                    else:
                        return "None"
                elif judgeCode=="BAX":
                    if firstValue<0 and nextValue>0:
                        return "BAX"
                    else:
                        return "None"
                else:
                    return '输入judgeCode有误'
        buyInSign = recent_data_judge(recent_date2,recent_date1,"ABX")
        sellOutSign = recent_data_judge(recent_date4,recent_date3,"BAX")
        def daysUnix():
            # 获取今日的时间戳（今日0时）
            now_time = int(time.time())
            day_time = now_time - now_time % 86400 + time.timezone
            unix = str(day_time) + "000"
            return unix
        unix =daysUnix()
        parRetDict = {fund:{"Date":unix,"buyIn":buyInSign,"sellOut":sellOutSign}}
        retDict.update(parRetDict)
        if buyInSign=='ABX':
            insign = "买入"
        else:
            insign='None'
        if sellOutSign=='BAX':
            outSign='卖出'
        else:
            outSign='None'
        if printControl==1:
            print("基金代码：",fund)
            print("买入信号：",insign)
            print("卖出信号：",outSign)
            print()
    return retDict

if __name__ == '__main__':

    file = open("C:\\Users\Administrator\Desktop\strategy.txt")
    ruledict = eval(file.read())
    a = runner(ruledict)
    # print(a)#{'260112': {'Date': '1533139200000', 'buyIn': 'None', 'sellOut': 'None'}
    _list = list(a.keys())
    buylist = []
    selllist = []
    for i in _list:
        buysign=a[i]['buyIn']
        sellsign=a[i]['sellOut']
        if buysign!='None':
            buylist.append(i)
        else:
            pass
        if sellsign!='None':
            selllist.append(i)
        else:
            pass
    print('buylist',buylist)
    print('selllist',selllist)
