from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.cross_line import cross_line as cline
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import singleness_fund_inquire as data,cut_Data_ACWorthTrend as ljjz
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import daily_line_dict_assembly_ACWorthTrend as dl
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import abandon_front_section_dict as ab1dict

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
        _result_dict = cline(dict1,dict2,1)
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

if __name__ == '__main__':

    fundlist = []
    filepath = 'C:\\Users\Administrator\Desktop'

    for i in fundlist:
        fundcode = i
        dox =open(filepath+'\\总览.txt','w')
        filename='\\'+fundcode+'.txt'
        doc = open(filepath+filename, 'w')
        day1=[5,10,15,20,15,30]
        day2=[35,40,45,50,55,60]
        print("基金",fundcode,"数据",file=doc)


        maxdata = ''
        ratedata = 0
        for dayi1 in day1:
            for dayi2 in day2:
                i = mechanicalDailyLineAnalysisCalc(fundcode,dayi1,dayi2)
                a = 0
                ill=0
                for i1 in list(i.keys()):
                    ill=i[i1]
                    a = a+i[i1]

                # p=a

                print('选择日期为:',dayi1,dayi2,file=doc)
                junzhi = round(a/len(list(i.keys())),4)
                print('收益均值：',str(junzhi)+" %",file=doc)
                print(file=doc)
                print(dayi1,dayi2)
            if ratedata <= junzhi:
                ratedata = junzhi
                maxdata = str(dayi1) + ' ' + str(dayi2)
        print(fundcode,file=dox)
        print("最值为:",maxdata,ratedata,'%',file=dox)
        print("最值为:", maxdata, ratedata, '%', file=doc)

