from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.cross_line import cross_line as cline
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import singleness_fund_inquire as data,cut_Data_ACWorthTrend as ljjz
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import daily_line_dict_assembly_ACWorthTrend as dl
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import abandon_front_section_dict as ab1dict
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import value_2_key,Erase_delete_corresponding_value as dropvalue
import os,time,random
def makeUseAbleDict(dailyline):
    """
    传本py里面的dl跑出值将值转化为穿线py中可以用的数据格式
    :param dailyline:计算出的日均线数据dict
    :return:可以用的dict
    """
    _return_dict = {}
    _list = list(dailyline.keys())
    same_keys= list(dailyline[_list[1]].keys())[0]
    for i in _list:
        value = dailyline[i]
        value = value[str(same_keys)]
        pinzhuangdict = eval('{"'+i+'":"'+str(value)+'"}')
        _return_dict.update(pinzhuangdict)
    return _return_dict

def mechanicalDailyLineAnalysisCalc(fundcode,time1=20,time2=60):
    """
    计算基金的日均线机械买卖盈利能力
    在time1日均线穿越time2日均线时候买入，在time1日均线跌破time2日均线卖出
    :param fundcode: 基金代码
    :param time1: 第一条日均线
    :param time2: 第二条日均线
    :return: 一个周期盈利能力dict
    """
    """数据集合"""
    FundDate = ljjz(data(fundcode))

    """日均线计算"""
    _time1dl = dl(FundDate,time1)
    _time2dl = dl(FundDate,time2)

    _time1dl_dict = makeUseAbleDict(_time1dl)
    _time2dl_dict = makeUseAbleDict(_time2dl)


    """核"""
    def mechanicalDailyLineAnalysisCalcCoreCode(dict1,dict2,_dictFundDate):
        """
        核心计算代码
        :param dict1:第一条日均线 dict
        :param dict2: 第二条日均线dict
        :param _dictFundDate: 该基金的累计净值
        :return:一个周期盈利能力dict（不加%号的百分比值）
        """
        _result_dict = cline(dict1,dict2)
        keylist = _result_dict.keys()
        resultDict = {}
        for i in keylist:
            point = _result_dict[i]["secondPoint"]
            way =_result_dict[i]["way"]
            appendString = eval('{"'+point+'":"'+way+'"}')
            resultDict.update(appendString)

        ifKeylist1 = list(resultDict.keys())
        ifcode = resultDict[ifKeylist1[0]]
        if ifcode == 'ABX':
            resultDict = ab1dict(resultDict,1)

        popValue = ifKeylist1[len(ifKeylist1)-1]
        ifcode = resultDict[popValue]
        if ifcode == 'BAX':
            resultDict.pop(popValue)

        transactionList = list(resultDict.keys())
        doubleCode = 0
        inValueKey =1
        outValueKey = 1
        inValueDict={}
        outValueDict = {}
        for i in transactionList:
            if doubleCode==0:
                inValue = _dictFundDate[i]['ACWorthTrend']
                inValueDictPart = eval('{"'+str(inValueKey)+'":""}')
                inValueDictPart[str(inValueKey)]=inValue
                inValueDict.update(inValueDictPart)
                doubleCode=1
                inValueKey=inValueKey+1
            elif doubleCode ==1:
                outValue = _dictFundDate[i]['ACWorthTrend']
                outValueDictPart = eval('{"' + str(outValueKey) + '":""}')
                outValueDictPart[str(outValueKey)] = outValue
                outValueDict.update(outValueDictPart)
                doubleCode=0
                outValueKey=outValueKey+1

        calcList = list(inValueDict.keys())
        calcResultDict = {}
        for i in calcList:
            calcResult = round(((outValueDict[i]-inValueDict[i])/outValueDict[i])*100,4)
            calcResultPart = eval('{"' + str(i) + '":""}')
            calcResultPart[str(i)]=calcResult
            calcResultDict.update(calcResultPart)
        return calcResultDict

    finalresult = mechanicalDailyLineAnalysisCalcCoreCode(_time1dl_dict, _time2dl_dict, FundDate)
    return finalresult

def exchang_dailyline_strategy(day11,day12,day21,day22,DATA):
    """
    日均线互换策略，基于基础版本只能计算两个日期下面的日均线，不能计算不同策略之间的数据，所以进行进一步
    的，例如我的买入日期我选择在20日均线穿越60日均线的时候进行买入，而在日常计算值突破60日均线时候卖出，
    这样的盈利均值为多少，以这个目的进行数据计算
    :param fundcode: 基金代码
    :param day11: 买入策略第一条日均线
    :param day12: 买入策略第二条日均线
    :param day21: 卖出策略第一条日均线
    :param day22: 卖出策略第二条日均线
    :return:收益百分比
    """

    """获取基金数据"""
    FundDate =DATA


    """日均线计算"""
    _time11dl = dl(FundDate,day11)
    _time12dl = dl(FundDate,day12)
    _time11dl_dict = makeUseAbleDict(_time11dl)
    _time12dl_dict = makeUseAbleDict(_time12dl)

    _time21dl = dl(FundDate, day21)
    _time22dl = dl(FundDate, day22)
    _time21dl_dict = makeUseAbleDict(_time21dl)
    _time22dl_dict = makeUseAbleDict(_time22dl)


    """制作两条穿线结果"""
    waitToTrateDataList = [_time11dl_dict,_time12dl_dict,_time21dl_dict,_time22dl_dict]
    _result_dict = cline(waitToTrateDataList[0], waitToTrateDataList[1])
    keylist = _result_dict.keys()
    resultDict1 = {}
    for i1 in keylist:
        point = _result_dict[i1]["secondPoint"]
        way = _result_dict[i1]["way"]
        appendString = eval('{"' + point + '":"' + way + '"}')
        resultDict1.update(appendString)

    _result_dict = cline(waitToTrateDataList[2], waitToTrateDataList[3])
    keylist = _result_dict.keys()
    resultDict2 = {}
    for i1 in keylist:
        point = _result_dict[i1]["secondPoint"]
        way = _result_dict[i1]["way"]
        appendString = eval('{"' + point + '":"' + way + '"}')
        resultDict2.update(appendString)

    resultDict1 = dropvalue(resultDict1, 'BAX')
    resultDict2 = dropvalue(resultDict2, 'ABX')

    #得到两条穿线数据
    keylist1 = list(resultDict1.keys())
    keylist2 = list(resultDict2.keys())

    #拼买入卖出时间对
    tradedict={}
    # tradedict={num:[buyin,sellout]}
    for buyin in keylist1:
        for sellout in keylist2:
            if buyin >= sellout:
                continue
            if buyin < sellout:
                ptradedict = {"t" + str(keylist1.index(buyin)): [buyin, sellout]}
                tradedict.update(ptradedict)
                break

    returndict = {}
    for i in tradedict.keys():
        pair = tradedict[i]
        buydate=pair[0]
        selldate=pair[1]
        buyinprice=float(FundDate[buydate]['ACWorthTrend'])
        selloutprice=float(FundDate[selldate]['ACWorthTrend'])
        D_value_rate = round(((selloutprice - buyinprice) / buyinprice), 4)
        PpriceDict ={"income_rate"+str(i):str(D_value_rate)}
        returndict.update(PpriceDict)

    return returndict


def many_exchange_line_report(fundcode):
    pwd = os.getcwd()
    pwd = pwd.replace(":\\", ':\\\\')
    filepath = pwd + '\INFORMATION_AND_ATTACHMENT\基金文件\机械交易算法结果'

    funddoc=open(filepath+'\\'+str(fundcode)+".txt",'w')
    sleeptime = 5
    while(1<2):
        eout = ""
        try:
            FundDate = ljjz(data(fundcode))
        except Exception as e:
            eout = e
        if eout=="":
            break
        else:
            print("当前等待时间:",sleeptime,"进入等待")
            time.sleep(sleeptime)
            sleeptime=sleeptime+random.randint(5,15)*10+random.randint(0,9)


    daylist1=[1,5,10,20,30]
    daylist2=[40,50,60,90,120]
    daylist3=[1,5,10,20,30]
    daylist4=[40,50,60,90,120]
    # daylist1 = [1,5]
    # daylist2 = [40,90]
    # daylist3 = [5]
    # daylist4 = [120]
    print("基金：" + str(fundcode),file=funddoc)
    pindict = {}
    for i in daylist1:
        day1=i
        for i2 in daylist2:
            day2=i2
            for i3 in daylist3:
                day3=i3
                for i4 in daylist4:
                    try:
                        day4=i4
                        dict = exchang_dailyline_strategy(day1,day2,day3,day4,FundDate)
                        lists = list(dict.values())
                        num = 0
                        maxvalue=float(max(lists))
                        minvalue=float(min(lists))
                        for i in lists:
                            num=float(i)+num
                        mean_value=num/len(lists)

                        updatekey = str(day1)+'-'+str(day2)+'-'+str(day3)+'-'+str(day4)
                        Pdict = eval('{"'+updatekey+'":""}')
                        Pdict[updatekey]=mean_value
                        pindict.update(Pdict)

                        print("机械规则：" + str(day1) + '-' + str(day2) + '  ' + str(day3) + '-' + str(day4), file=funddoc)
                        print("收益均值：" + str(mean_value), file=funddoc)
                        print("最大值为：" + str(maxvalue) + " 最小值为：" + str(minvalue), file=funddoc)
                        print('', file=funddoc)
                        print("当前计算" + str(fundcode),
                              "机械规则：" + str(day1) + '-' + str(day2) + '  ' + str(day3) + '-' + str(day4))

                    except Exception as e:
                        pass

                    funddoc.close()
    return pindict


def runner(fundcodelist=[]):
    codelist = fundcodelist
    pwd = os.getcwd()
    pwd = pwd.replace(":\\", ':\\\\')
    filepath = pwd + '\INFORMATION_AND_ATTACHMENT\基金文件\机械交易算法结果'
    sumdoc = open(filepath + "\\总览.txt", 'w')
    print("",file=sumdoc)
    sumdoc.close()
    stratigyDict={}

    for i in codelist:
        sumdoc = open(filepath + "\\总览.txt", 'a')
        lastdict = many_exchange_line_report(i)
        fundcode = i
        maxvalue = max(list(lastdict.values()))
        stratigy=value_2_key(lastdict,maxvalue)
        # print(stratigy)
        rates=round(maxvalue,4)
        print("基金代码：" + str(fundcode), file=sumdoc)
        print("最大收益策略：" + str(stratigy) + " 最大收益：" + str(rates), file=sumdoc)
        sumdoc.close()
        parstratigyDict={i:str(stratigy)}
        stratigyDict.update(parstratigyDict)
    return stratigyDict

if __name__ == '__main__':
    a = runner(['110022'])
    pwd = os.getcwd()
    pwd = pwd.replace(":\\", ':\\\\')
    filepath = pwd + '\INFORMATION_AND_ATTACHMENT\基金文件\机械交易算法结果'
    ddoc = open(filepath + "\\策略字典.txt", 'w')
    print(a,file=ddoc)
    #不可查询'110051', '091023','270047', '110053',  '471060',
    # '260112', '519977', '530020','110022', '110011', '519697', '180012', '570005', '519091', '519712', '040008', '070032', '270041', '510630', '519700', '519702', '540006', '163412', '165312', '690001', '160212', '519066', '202023', '519069', '002021', '110003', '519068', '166005', '020026', '340008', '320011', '163406', '217022', '519669', '233005', '160916', '320021','570001', '163415', '121012', '163402', '128112', '159905', '481012', '040011', '050027', '166008','159916','050011', '110008', '233012', '340009', '050111', '530015', '110007','163407', '310398', '160716', '090007', '202005', '166001', '166002',