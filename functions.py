import requests
import json
import pandas as pd
def access_token():
    url="https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    # method="post"
    headers={
        'content-type': 'application/json; charset=utf-8'
    }
    data={
        'app_id': 'cli_a48314db3da5d013',
        'app_secret': 'TIa8cQX4HQkucobu9z0XjbknxNdxj1Hh'
    }
    r=requests.post(url, json=data, headers=headers)
   
    print(r.json())
    access_token=r.json()['tenant_access_token']
    # print(r.json()['tenant_access_token'])
    Authorization='Bearer '+access_token
    print(Authorization)
    print("token获取成功------------------------")
    return Authorization


'''sheet information'''
def sheet_info(Authorization,sheet_token):
    url = f"https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{sheet_token}?user_id_type=user_id"
    headers = {
    'Authorization': Authorization
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)



'''
表格增加行列
'''
def sheet_add(Authorization,sheet_token,sheetId):
    url=f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range"

'''
删除行列
'''
def sheet_delete(Authorization,sheetId):
    pass
'''
换行列
'''
def sheet_change(Authorization,sheetId):
    pass
'''
更改行列
'''
def sheet_get(Authorization,sheetId):
    pass

'''
读取表格内容
'''
def sheet_read(Authorization,sheet_token,sheetId,ranges):
    url=f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{sheet_token}/values_batch_get?ranges={sheetId}!{ranges}&valueRenderOption=ToString&dateTimeRenderOption=FormattedString"
    print(url)
    headers={
        'Authorization': Authorization,
        'Content-Type': 'application/json; charset=utf-8'
    }
    res=requests.get(url, headers=headers)
    data=res.json()['data']['valueRanges'][0]['values']
    # print(res.text)
    # print(res.json())

    

if __name__ == "__main__":
    Authorization=access_token()
    sheet_token="shtcnOkHqM0VZzZevII4YKw1VAd"
    sheetId="fec223"
    range="A1:C4"
    sheet_read(Authorization=Authorization,sheet_token=sheet_token,sheetId=sheetId,ranges=range)
