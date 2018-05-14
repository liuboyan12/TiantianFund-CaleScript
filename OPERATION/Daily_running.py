from DATA_PROCESSING.PERSONAL_PACKAGING_MODES_AND_FUCTIONS.TianTianfundition_static_module import fund_static_main
import datetime
import os
import time


def daily_ruuning(filepath):
    for i in filepath:
        filepath_use = i
        result = fund_static_main(filepath_use)
        # print(result[6])
        import_file_name=filepath_use[(filepath_use.find("\基金文件")+1+len("\基金文件")):filepath_use.find('.txt')]
        import_file_name1 = str(str(datetime.datetime.now())[:10] + import_file_name)+'.txt'
        filepath = os.path.join("d:\\Python_Lib_local\基金计算\基金统计结果", import_file_name1)
        doc = open(filepath, 'w')
        print('==================================================',file=doc)
        print(import_file_name,file=doc)
        stings = i[i.find("基金文件")+5:i.find(".txt")]
        print(stings +'今日涨跌无权重平均： ' + str(result[0]) + "%")
        print('今日涨跌无权重平均： '+str(result[0])+"%",file=doc)
        print('==================================================',file=doc)
        print('涨基金：',file=doc)
        print('     1以内:',file=doc)
        result1 = result[1]
        for i in range(len(result1)):
            print(result1[i],file=doc)
        print('     1以上: ',file=doc)
        result3 = result[3]
        for i in result3:
            print(i,file=doc)
        print('     2以上: ',file=doc)
        result5=result[5]
        for i in result5:
            print(i,file=doc)
        print('==================================================',file=doc)
        print('跌基金：',file=doc)
        print('     1以内:',file=doc)
        result2 = result[2]
        for i in range(len(result2)):
            print(result2[i],file=doc)
        print('     1以上: ',file=doc)
        result4= result[4]
        for i in result4:
            print(i,file=doc)
        print('     2以上: ',file=doc)
        result6=result[6]
        for i in result6:
            print(i,file=doc)
        print('==================================================',file=doc)
        # print('记录时间： '+datetime.datetime.now())
        print()
        time.sleep(30)
        # i = datetime.datetime.now()
        # print(str(i.year)+str(i.day)+str(i.month)+' '+str(i.hour)+':'+str(i.minute))

    #     print(context,file = doc)
stop_while_code = 1
plus_plus = 0
if __name__ == '__main__':
    pwd = os.getcwd()
    pwd =pwd.replace(":\\",':\\\\')
    filepath_all = pwd+'\INFORMATION_AND_ATTACHMENT\基金文件\\'
    # print(filepath)
    filename = ['个人基金.txt','关注基金列表.txt','媳妇基金.txt']
    # filename = ['媳妇基金.txt']
    filepath = [filepath_all+filename[0],filepath_all+filename[1],filepath_all+filename[2]]
    # filepath = [filepath_all + filename[0]]
    while(stop_while_code == 1):
        try:
            daily_ruuning(filepath)
            i = datetime.datetime.now()
            time_now = i.hour
            if time_now >= 15:
                stop_while_code = 2
            if stop_while_code == 1:
                out_put_word ='今日交易未结束'
            else:
                out_put_word = '交易未开启'
            print(out_put_word)
            plus_plus = plus_plus+1
            print('结果跑出次数统计：'+str(plus_plus))
            print('=============================================')
            print(datetime.datetime.now())
            time.sleep(150)
        except Exception as e:
            print(e)
            pass

