"""
将天天基金里面的传来数据进行更改更改为可以用的字典数据
{
时间:
    {x:value,y:value}
}
"""
# 单位净值走势转化为dict,返回值a为dict
#对应返回值为/*单位净值走势 equityReturn-净值回报 unitMoney-每份派送金*/下所有数据
def Data_netWorthTrend(return_value):
    a = return_value.replace('},{"x":', '},')
    a = a.replace('{"x":', '')
    a = a.replace(',"y"', ':{"y"')
    a = a.replace(']', '}')
    a = a.replace('[', "{'")
    a = a.replace('"', "'")
    a = a.replace("},", "},'")
    a = a.replace(":{'y'", "':{'y'")
    a = a.replace(";","")
    a = eval(a)
    # print(a)
    return a

def Data_stockThrend(return_value):
    a =return_value
    a= a.replace(' ','')
    a= a.replace('"',"")
    a=a.replace(';','')
    a=a.replace('[','')
    a=a.replace(']','')
    a=str(a)
    # print(a)
    target_list = [i for i in a.split(',')]
    return target_list

def Data_bondThrend(return_value):
    a = return_value
    a= a.replace(' ','')
    a= a.replace('"',"")
    a=a.replace(';','')
    a=a.replace('[','')
    a=a.replace(']','')
    target_list = [i for i in a.split(',')]
    return target_list

def Data_ACWorthTrend(return_value):
    a = return_value
    a= a.replace("[[","[['").replace(",","',").replace("',[",",['").replace(",",":").replace("]:[","],[").replace("[","{").replace("]","}")
    a =a.replace("}}","}}}").replace(":",":{'ACWorthTrend':").replace("},","}},")
    a= a.replace("{{'","{'").replace("}},","},").replace(",{'",",'").replace("}}}","}}")
    return a