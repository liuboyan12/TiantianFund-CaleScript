from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num as find_double


def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            # print()


def cross_line(dictA={},dictB={},startLocation=1):
    """
    :param dictA:传入离散点dict数据
    :param dictB:传入离散点lict数据
    :return:dictR:穿线点的字典

    焦点表示规则（way)：
    ABX——0，BAX——1
        解释
            ABX：A在上B在下，A穿越B到B的下方（B穿越A到A的上方）
            BAX：B在上A在下，B穿越A到A的下方（A穿越B到B的上方）

    出口规则：
        返回值为dict
        格式：
            dictR={
                    "pointNo":{"firstPoint":"Xi"，"secondPoint":"Xi+step"，"way":"ABX/BAX"}
                    }
    """
    Xi = list(dictA.keys())
    step=1
    i=startLocation
    i1 = 1
    dictR = {}
    dictPart = '{"pointNo":{"firstPoint":"","secondPoint":"","way":""}}'
    while 1<2:
        if i+1>=len(Xi):
            break
        else:
            X = Xi[i-1]
            Xp=Xi[i+step-1]
            Yai = float(dictA[X])
            Ybi = float(dictB[X])
            Yaip = float(dictA[Xp])
            Ybip = float(dictB[Xp])
            Value1 = Ybi - Yai
            Value2 = Ybip - Yaip
            judgement = Value1*Value2
            print(judgement,"judgement")
            startPoint = Yai - Ybi
            # print("Yai,Ybi,Yaip,Ybip",Yai,Ybi,Yaip,Ybip)
            # print("Value1,Value2,judgement",Value1,Value2,judgement)
            if startPoint == 0:
                i = i+step
                continue
            else:
                if judgement == 0:
                    step=step+1
                    continue
                else:
                    i = i + step
                    step = 1
                    if judgement>0:
                        continue
                    else:
                        controlString = "point" + str(i1)
                        dictPart=dictPart.replace("pointNo",controlString)
                        i1 = i1 + 1
                        dictP=eval(dictPart)
                        # ABX：A在上B在下，A穿越B到B的下方（B穿越A到A的上方）
                        # BAX：B在上A在下，B穿越A到A的下方（A穿越B到B的上方）

                        dictP[controlString]["firstPoint"] = X
                        dictP[controlString]["secondPoint"] = Xp

                        if startPoint>0:
                            # yai>ybi,A线在上B线在下——ABX
                            dictP[controlString]['way']='ABX'
                        else:
                            #BAX
                            dictP[controlString]['way'] = 'BAX'
                        dictR.update(dictP)
                        dictPart = '{"pointNo":{"firstPoint":"","secondPoint":"","way":""}}'
    return dictR

if __name__ == '__main__':
    # dictA={'a':'2','b':'0','c':'0'}
    # dictB = {'a':'1','b': '1', 'c': '1'}
    dictA={'q':'1','w':'1','e':'1','r':'1','t':'1','y':'1','u':'1','i':'1','o':'1','p':'1'}
    dictB={'q':'1','w':'0','e':'2','r':'1','t':'0','y':'0','u':'1','i':'0','o':'2','p':'2'}
    # dictA={'e':'1','r':'1','t':'1','y':'1','u':'1','i':'1','o':'1','p':'1'}
    # dictB={'e':'2','r':'1','t':'0','y':'0','u':'1','i':'0','o':'2','p':'2'}
    returnvalue= cross_line(dictA,dictB)
    print(returnvalue)
    # cross_lisetest(dictA)




