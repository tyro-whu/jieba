# coding: UTF-8
import OpenHowNet
import json
import jieba
import jieba.posseg
import pymysql
pymysql.install_as_MySQLdb()
import csv

hownet_dict = OpenHowNet.HowNetDict()
hownet_dict.initialize_sememe_similarity_calculation()
hownet_dict_advanced = OpenHowNet.HowNetDict(use_sim=True)


# 定义种子集PP
PP=['赞','好评','棒','实惠','不错','方便','感谢']
PN=['咸','慢','恶心','难吃','超时','失望','迟到']
jieba.enable_paddle()

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Wang1212',
                     database='shehui')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表，一个词和Polarity
sql = """CREATE TABLE EMPLOYEE (
         Words  CHAR(20) NOT NULL,
         Pol    FLOAT)"""
cursor.execute(sql)

# 定义函数得到其倾向值Polarity
def GetPolarity(word):
    P = 0
    N = 0
    for i in range(len(PP)):
        if (hownet_dict_advanced.calculate_word_similarity(PP[i], word) == 0):
            return 0
        else:
            P = P + hownet_dict_advanced.calculate_word_similarity(PP[i], word)
            N = N + hownet_dict_advanced.calculate_word_similarity(PN[i], word)
    if(len(PP)!=0 and len(PN)!=0):
        Polarity = P / len(PP) - N / len(PN)
    return Polarity


with open('./外卖评论.csv', encoding='utf-8', errors='ignore') as f:        #utf-8
    f_csv = csv.reader(f)
    headers = next(f_csv)
    # for row in f_csv:
    #     print(row)


    for i in f_csv:
        words = jieba.posseg.cut(i[1])         #利用jieba分割词
        for word,flag in words:
            Pol = GetPolarity(word)
            # print(word,flag)
            # # 包 v; 很 d; 一般 a; 。 x; 凉面 n; 没 v; 想象 n; 中 f     得到的词和词性
            if(flag in['a', 'v', 'n', 'd']) and (Pol != 0):
                if(i[0] == '0'):
                    # SQL 插入语句
                    sql = "INSERT INTO EMPLOYEE(Words, Pol) VALUES ('%s','%s')" %(word,Pol)
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        db.commit()
                    except:
                        # 如果发生错误则回滚
                        db.rollback()
                elif (i[0] == '1'):
                    # SQL 插入语句
                    sql = "INSERT INTO EMPLOYEE(Words, Pol) VALUES ('%s','%s')" %(word,Pol)
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        db.commit()
                    except:
                        # 如果发生错误则回滚
                        db.rollback()

#数据库排序，选取前50个负向词
print('-'*100)
print('负向词：')
sql = "SELECT  distinct * FROM EMPLOYEE ORDER BY Pol"
cursor.execute(sql)
result = cursor.fetchall()
i = 0
for x in result:
    if(i < 50):

        print(x)
        i+=1
    else:
        break


#数据库排序，选取前50个正向词
print('-'*100)
print('正向词：')
sql = "SELECT  distinct * FROM EMPLOYEE ORDER BY Pol DESC"
cursor.execute(sql)
result1 = cursor.fetchall()
i = 0
for x in result1:
    if(i < 50):
        print(x)
        i+=1
    else:
        break

# 关闭数据库连接
db.close()