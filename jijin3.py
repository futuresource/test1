"""
基金排行请求
pi是页数
pn是基金数
ft: zq  种类：债券
"""

import requests,time

t = time.strftime("%Y-%m-%d", time.localtime())


def rank(pi,sc = '1yzf'):
    cookies = {
        'st_si': '79198021873616',
        'st_asi': 'delete',
        'EMFUND1': 'null',
        'EMFUND2': 'null',
        'EMFUND3': 'null',
        'EMFUND4': 'null',
        'EMFUND5': 'null',
        'EMFUND6': 'null',
        'EMFUND7': 'null',
        'EMFUND8': 'null',
        'EMFUND0': 'null',
        'EMFUND9': '12-25 10:35:23@#$%u5E7F%u53D1%u53CC%u64CE%u5347%u7EA7%u6DF7%u5408@%23%24005911',
        'ASP.NET_SessionId': 'hxko3rdj3ds4rnvpjs2kav2u',
        'qgqp_b_id': '46531301e841a708d782dad333d7c16c',
        'st_pvi': '41983179780459',
        'st_sp': '2019-12-25%2010%3A34%3A52',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '3',
        'st_psi': '20191225103752435-111000300841-7729570632',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'Connection': 'keep-alive',
    }
    # params = (
    #     ('op', 'ph'),
    #     ('dt', 'kf'),
    #     ('ft', 'all'),
    #     ('rs', ''),
    #     ('gs', '0'),
    #     ('sc', '%s'%sc),
    #     ('st', 'desc'),
    #     ('sd', '2019-01-01'),
    #     ('ed', '%s'%t),
    #     ('qdii', ''),
    #     ('tabSubtype', ',,,,,'),
    #     ('pi', pi),
    #     ('pn', '2000'),
    #     ('dx', '1'),
    #     ('v', '0.8429148933369384'),
    # )
    params = (
        ('op', 'ph'),
        ('dt', 'kf'),
        ('ft', 'zq'),
        ('rs', ''),
        ('gs', '0'),
        ('sc', '%s'%sc),
        ('st', 'desc'),
        ('sd', '2019-06-19'),
        ('ed', '2020-06-19'),
        ('qdii', '|'),
        ('tabSubtype', ',,,,,'),
        ('pi', pi),
        ('pn', '1700'),
        ('dx', '1'),
        ('v', '0.5802450781336554'),
    )
    response = requests.get('http://fund.eastmoney.com/data/rankhandler.aspx', headers=headers, params=params,
                            cookies=cookies).text
    return eval(response.split(':')[1].split(',allRecords')[0])
    '''
    ['006148,宝盈融源可转债债券C,BYRYKZZZQC,2020-06-19,1.1670,1.1670,0.9516,3.7426,7.1921,15.0888,12.0284,,,,10.0943,16.70,2019-09-04,1,16.7,,0.00%,,,,',
     '006147,宝盈融源可转债债券A,BYRYKZZZQA,2020-06-19,1.1698,1.1698,0.9580,3.7425,7.2227,15.1718,12.2003,,,,10.2545,16.98,2019-09-04,1,16.98,0.80%,0.08%,1,0.08%,1,']
    '''
    # return response.split('[')[1].split(']')[0]

# print(rank(1))
# l = rank(1).split(':')[1].split(',allRecords')[0]
# # print(type(eval(l)))
# with open('writetxt.txt', 'a') as f:
#     for ff in eval(l):
#         # for fff in ff:
#         f.write(ff+' ')
#         f.write('\n')