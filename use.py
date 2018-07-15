from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.cross_line import cross_line as cline
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import singleness_fund_inquire as data,cut_Data_ACWorthTrend as ljjz
from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.daily_line import daily_line_dict_assembly_ACWorthTrend as dl

def mechanicalFundCalc(fundcode,fistline,secondline):
    """
    基金机械操作脚本,传入参数，查找
    :param fundcode:
    :return:
    """
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



if __name__ == '__main__':
    def tprint(obj, except_word=""):
        for name, item in globals().items():
            if item == obj and name != except_word:
                print(name + ':', type(obj))
                print(obj)
    _dictFundDate = ljjz(data("002001"))
    # print(_dictFundDate)
    _20dl = dl(_dictFundDate,20)
    _30dl = dl(_dictFundDate,30)
    _50dl = dl(_dictFundDate,50)
    _60dl = dl(_dictFundDate,60)
    _20dl_dict = makeUseAbleDict(_20dl)
    tprint(_20dl_dict)
