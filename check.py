import requests
from datetime import date, timedelta


def get_token():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'http://hr.biz-united.com.cn:8210',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://hr.biz-united.com.cn:8210/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        'functionCode': '',
        'loginUserToken': 'undefined',
        'menuCode': '',
    }

    json_data = {
        'ujlrwebjruzddjnu': 'YH0591',
        'pazjofxkyvyoosot': 'lvQXLQOlLuyo7rsYtyapIA==',
    }

    response = requests.post(
        'http://hr.biz-united.com.cn:8210/mdm/mdmSystemLoginController/login',
        headers=headers,
        json=json_data,
        verify=False,
    )
    print(response.json())
    token = str(response.json()['result']['loginUserToken'])
    # print(token)
    return token


def check(token):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'http://hr.biz-united.com.cn:8210',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://hr.biz-united.com.cn:8210/engineering_center/work_situation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
        'functionCode': 'work_situation_list',
        'loginUserToken': token,
        'menuCode': 'CRM20220811000002422',
    }

    json_data = {
        'pageNum': 1,
        'pageSize': 15,
    }

    response = requests.post(
        'http://hr.biz-united.com.cn:8210/mdm/mdmhrworkreport/findUserDistributionByCode',
        headers=headers,
        json=json_data,
        verify=False,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"pageNum":1,"pageSize":15}'
    # response = requests.post(
    #    'http://hr.biz-united.com.cn:8210/mdm/mdmhrworkreport/findUserDistributionByCode',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    #    verify=False,
    # )
    print(response.json())
    if response.json()["success"] == True and str(response.json()["message"]) == '操作成功！':
        info = response.json()
        return info
    else:
        return False


'''
企业微信通道
'''


def send_msg_QiYeWehat(name, warn):
    if len(warn) == 0:
        print("没有消息内容")
        warn = "没有消息内容，很诡异！"
    # 自定义webhook地址
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=be5ee142-9cb0-4657-90fd-33c7708da212"
    http_url = "http://hr.biz-united.com.cn:8210/engineering_center/work_situation"
    headers = {"Content-Type": "text/plain"}
    txt = f'''🔔🔔🔔报工系统提醒to{name}（定时消息）:\n{warn}！！！\n[点击进入报工系统]({http_url})\n'''
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": txt
        }
    }
    r = requests.post(url=webhook, headers=headers, json=data)
    # print(r)
    print("提醒发送成功")


'''
飞书webhook通道
'''


def webhook_method(webhook_url,today,yesterday,today_msg,yesterday_msg,name):
    # webhook_url = "https://www.feishu.cn/flow/api/trigger-webhook/a688067579f85fa9b3e5724c76ca1232"
    data={
	"data": [{
			"name": name,
			"yesterday": yesterday,
			"yesterday_msg": yesterday_msg,
			"today": today,
			"today_msg": today_msg
		}
	]
}

    print(today,yesterday,today_msg,yesterday_msg,name)
    print(data)
    print("-----------------------")
    r=requests.post(url=webhook_url, json=data)
    print("推送完成")
   
  


def main():


    # 获取时间
    # Get today's date and store it in today
    today = date.today()

    # Print the day of the month
    # print("Today is day {} of the month {}".format(today.day, today.month))

    d = today.day
    l_day = "date"+str(d-1)
    t_day = "date"+str(d)

    # Get today's date
    today_detail = date.today()

    # Get yesterday's date
    yesterday_detail = today - timedelta(days=1)

    today=str(today_detail)
    yesterday=str(yesterday_detail)
    # 获取token
    token = get_token()
    # print(type(token))

    info = check(token)
    if info != False:

        # 判断最近两天报工情况
        yesterday_msg = info['result']['data'][0][l_day]
        today_msg = info['result']['data'][0][t_day]
        
        name = "周纪元"
        # send_msg(name, warn)

        import datetime
        # today=datetime.datetime.now().strftime('%Y-%m-%d')
        weekday = datetime.datetime.now().weekday()
        if weekday == 6 or weekday == 7:
            print("今天是周末，今天可以休息！")
        else:
            print("今天是工作日，继续加油！")
            '''
            # 第一种方法是通过企业微信发送
            # 消息合成内容
            # warn = f"**昨天：{str(yesterday_detail)}**\n报工情况：{last_day}\n\n**今天：{str(today_detail)}**\n报工情况：{this_day}\n\n"
            #send_msg_QiYeWehat(name,warn)
            '''
            # 第二种方法是通过飞书捷径的webhook发送
            
            webhook_method(today,yesterday,today_msg,yesterday_msg,name)
        print("-------------------------done------------------------")

 

