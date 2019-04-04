# usdt_deploy_test

## 本文档介绍usdt合约部署及用python脚步进行简单测试
#### 文档分2个部分
##### 1.使用tronbox部署合约
##### 2.使用python脚步进行简单的接口测试（建议在Anaconda下进行测试）

#### -------------------------------------------------------------------------------------------------------------
## 第一部分: 使用tronbox部署合约

##### 1.1 tronbox安装
###### 具体请参见tronbox文档   https://cn.developers.tron.network/docs/%E5%85%A5%E9%97%A8

##### 1.2 安装 zeppelin-solidity
###### npm install zeppelin-solidity

##### 1.3 需要修改的文件(具体修改根据需求进行修改即可)
######  a.tronbox.js (选择需要部署的网络及添加合约部署账户的私钥)
######  b.migrations/2_deploy_contracts.js (token名称及精度等)
######  c.修改contracts/ERC20Basic.sol中
######        uint256 public totalSupply; 修改为 function totalSupply() public constant returns (uint);



##### 1.4 合约部署
###### 具体参见文档 https://cn.developers.tron.network/docs/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6%E9%83%A8%E7%BD%B2

#### -------------------------------------------------------------------------------------------------------------
## 第二部分: 使用python脚步进行简单的接口测试

###  2.1 使用说明
##### a. 使用python3.7版本
##### b. 推荐在Anaconda(spyder)平台下进行测试。

### 2.2 代码介绍
##### a. trans_url(创建交易地址)，sign_url(签名地址),broast_url(广播地址),根据需求，可选择主网地址或shasta地址，也可根据自己需要进行修改。
##### b. contract_addres(合约地址)
##### c. owner_address & owner_address_privateKey 根据需求可修改合约调用者地址及对应私钥。
##### d. trans_payload_transfer01 调用合约内部函数对应的参数，其中function_selector根据需要修改需要测试使用的函数，parameter为函数需要传入的参数。
##### e. trans_respon 创建交易的返回值
##### f. sign_respon.json()  签名后的返回值
##### g. broast_respon.json() 广播后的返回值
##### h. ack_trans_respon.text 确认交易是否成功，具体请查看返回结果内容。
### 注：ack_trans_respon.text 返回可能为空，具体结果可根据txid再进行查看。

