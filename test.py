from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.self_encapsulation_scripts import fetch_dict_by_num as find_double


def tprint(obj, except_word=""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            print(name + ':',type(obj))
            print(obj)
            # print()

def cross_line(dictA={},dictB={}):
    """
    :param dictA:
    :param dictB:
    :return:

    焦点表示规则（way)：
    ABX——0，BAX——1
        解释
            ABX：A在上B在下，A穿越B到B的下方（B穿越A到A的上方）
            BAX：B在上A在下，B穿越A到A的下方（A穿越B到B的上方）

    出口规则：
        返回值为dict
        格式：
            dictR={
                    "pointNo":{"X前":"Y前"，"X后":"Y后"，"way":"ABX/BAX"}
                    }
    """
    Xi = list(dictA.keys())
    step=1
    i = 1
    while 1<2:
        if i+1>=len(Xi):
            break
        else:
            Yai = dictA[Xi[i]]
            Ybi = dictB[Xi[i]]
            Yaip1 = dictA[Xi[i+step]]
            Ybip2 = dictB[Xi[i+step]]
            Value1=Ybi-Yai
            Value2=Ybip2-Yaip1
            judgement = Value1*Value2
            if judgement<0:

                i=i+step
                step=1

            if judgement>0:

                i=i+step
                step=1

            if judgement==0:
                    step = step + 1
                    continue
            i=i+1
















if __name__ == '__main__':

    print()





