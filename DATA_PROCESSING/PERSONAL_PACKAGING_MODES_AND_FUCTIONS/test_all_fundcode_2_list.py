from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.A_TianTianJiJinShuJuChuLi_ChangeData import *
from DATA_PROCESSING.BASE_CONDITIONING_MODES_AND_FUCTIONS.txt_io import *

codelist = all_fundcode_2_list()
returnlist = []
for i in codelist:
    d = open("C:\\Users\Administrator\Desktop\空.txt", 'a')
    try:
        singleness_fund_inquire(i)
        print(str(i), file=d)
    except Exception as e :
        continue
    d.close()


if __name__ == '__main__':
    strings= format_removeal(read_file_inline("C:\\Users\Administrator\Desktop\新建文本文档.txt"))
    