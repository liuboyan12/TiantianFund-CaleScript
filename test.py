from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *


codelist = all_fundcode_2_list()
returnlist = []
for i in codelist:
    d = open("C:\\Users\Administrator\Desktop\空.txt", 'a')
    try:
        singleness_fund_inquire(i)
        print(str(i) + ",", file=d)
    except Exception as e :
        continue
    d.close()


