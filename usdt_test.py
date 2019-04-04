#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:15:55 2019

@author: alexliu
"""

# -*- coding: utf-8 -*-
"""

usdt abi test 
               
"""

import requests

'''
#shasta地址
trans_url = "https://api.shasta.trongrid.io/wallet/triggersmartcontract"
sign_url = "https://api.shasta.trongrid.io/wallet/gettransactionsign"
broast_url = "https://api.shasta.trongrid.io/wallet/broadcasttransaction"
ack_trans_url =  "https://api.shasta.trongrid.io/wallet/gettransactioninfobyid"
'''


#主网地址
trans_url = "https://api.trongrid.io/wallet/triggersmartcontract"
sign_url = "https://api.trongrid.io/wallet/gettransactionsign"
broast_url = "https://api.trongrid.io/wallet/broadcasttransaction"
ack_trans_url =  "https://api.trongrid.io/wallet/gettransactioninfobyid"


#合约地址
contract_address = "41a7837ce56da0cbb28f30bcd5bff01d4fe7e4c6e3"


#owneraddress
owner_address = "your owneraddress"
owner_address_privateKey = "your privatekey"

#000000000000000000000041332036CDD70AA2E9EFB006A8E92BABE7F684E64D
#0000000000000000000000000000000000000000000000000000000000000032
#000000000000000000000041332036CDD70AA2E9EFB006A8E92BABE7F684E64D0000000000000000000000000000000000000000000000000000000000000000",


#函数参数
trans_payload_transfer01 = {
      "contract_address": contract_address,
      "function_selector":"balanceOf(address)",  
      "parameter":"0000000000000000000000413DBF0E713475EFF1A7F815976BFBA9D3A0951650",
      "fee_limit":1000000000,
      "call_value":0,
      "owner_address":owner_address
      }


#-------------------------main----------------------------


#修改测试函数
trans_payload = trans_payload_transfer01


print("======================"+trans_payload.get("function_selector")+"函数===================")

#owner_address对应的私钥
sign_private = {"privateKey":owner_address_privateKey}


#创建交易
trans_respon = requests.post(trans_url,json=trans_payload)


#交易返回值 + 添加私钥参数
print("**************trans_respon*************")
print(trans_respon)
print(trans_respon.json())
trans_respon = dict(trans_respon.json())
trans_respon.update(sign_private)

print("**************trans_respon_add_private*************")
print(trans_respon)



#签名

sign_respon = requests.post(sign_url,json = trans_respon)

print("**************sign_respon*************")
print(sign_respon.json())

#广播
broast_respon = requests.post(broast_url,json=sign_respon.json())

print("**************broast_respon*************")
print(broast_respon.json())

#确认交易是否成功
ack_trans_url =  "https://api.trongrid.io/wallet/gettransactioninfobyid?value="
print("&&&&&&&&&&&&&&&&&&&交易ID&&&&&&&&&&&&&&")
print(trans_respon["transaction"]["txID"])
ack_tans_url_end = ack_trans_url + trans_respon["transaction"]["txID"]
print(ack_tans_url_end)
ack_trans_respon = requests.get(ack_tans_url_end)
print(ack_trans_respon.text)
























