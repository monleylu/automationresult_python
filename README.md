# python版本通用自动化结果接口设计


为了可以使用统一的结构体定义UI、接口、安全等不同测试过程的测试结果，现定义如下结构体  
## 基础结构体: ##

```json
{
    "success":false,
    "msg":"测试结果信息",
    "data":null
}
 ```
 
**参数介绍:**

|名称	|类型	|是否必须|	描述|
|:-:|:-:|:-:|:-:|
|success	|布尔值	|是	|用例执行成功失败标记
|msg	| 字符串	|是	|简要描述本测试用例，如失败时可反馈失败原因
|data	|Object对象|	是|存储任意内容，用户自定义内容，一般建议存储数组列表类型数据，可以格式话存储运行过程中的关键数据等


## 测试用例执行结果数据结构：
```json
{
    "success":true,
    "msg":"adf",
    "testcaseid":0,
    "testcasename":"测试用例名称",
    "startTime":1533275756,
    "endTime":1533275756,
    "type":2,
    "data":"测试过程中的数据，可以存储在这里，任何格式的数据都可以"
}
```

**参数介绍：**

|名称	|类型	|是否必须|	描述|
|:-:|:-:|:-:|:-:|
|success|	布尔值	|是	|用例执行成功失败标记|
|msg	|字符串	|是	|简要描述本测试用例，如失败时可反馈失败原因
|testcaseid|	字符串|	否|	测试用例id，方便未来扩展
|testcasename|	字符串	|否	|测试用例名称
|startTime|	整型|	否	|测试用例开始执行时间，单位为s，开始执行时间到1970年时间戳
|endTime	|整型	|否	|测试用例结束执行时间，单位为s
|type|	整型|	否|	自动化测试类型，0：未定义1:UI自动化 2：接口自动化		
|data	|Object对象|	否|	存储任意内容，用户自定义内容，一般建议存储数组列表类型数据，可以格式话存储运行过程中的关键数据等

# 和服务端交互数据结构
```json
{
    "name":"自动化测试",
    "key":"201801030405",
    "time":1533465771,
    "departmentID":null,
    "departmentName":"xmonley",
    "data":[
        {
            "success":false,
            "msg":null,
            "testcaseid":0,
            "testcasename":"adsfads",
            "startTime":1533466701,
            "endTime":1533466701,
            "type":1,
            "data":null
        },
        {
            "success":true,
            "msg":null,
            "testcaseid":0,
            "testcasename":"defaultTestCaseName",
            "startTime":1533466701,
            "endTime":1533466701,
            "type":2,
            "data":null
        },
        {
            "success":true,
            "msg":"基础测试",
            "data":{
                "adsf":1
            }
        }
    ]
}
```


**参数介绍：**

|名称	|类型	|是否必须|	描述|
|:-:|:-:|:-:|:-:|
|name|	字符串|	是|	本次自动化测试结果名称，统计系统以本名称聚合测试结果
|key	|字符串|	否|	批次概念，如果key相同，并且name相同，认为是同一次测试结果，统计报表时合并结果
|time	|字符串	|否	|单位s，到1970年时间戳，主要用在报表展示时，展示的时间节点
|departmentID|	整数|	否	|本次自动化结果归属部门id，预留扩展
|departmentName	|字符串	|是	|本次自动化结果归属部门名称，后续以这个参数统计合并自动化结果
|data| 数组|	否|	存储本批次测试用例执行结果




