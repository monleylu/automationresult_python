# -*- coding: utf-8 -*-
# @Author  : monleylu
# @Time    : 2018/7/12 3:03 PM
from TestCaseResult import TestCaseResult,TypeEnum

class InterfaceTestCaseResult(TestCaseResult):
    '''
    接口自动化测试用例测试结果
    '''

    def __init__(self,success=False,msg=None,data=None,testcaseid=0,testcasename="defaultTestCaseName",startTime=0,endTime=0):
        super().__init__(success=success, msg=msg, data=data, testcaseid=testcaseid, testcasename=testcasename,
                         startTime=startTime, endTime=endTime, type=TypeEnum.Interface.value)



if __name__=="__main__":
    i=InterfaceTestCaseResult()
    print(i.toString())