# -*- coding: utf-8 -*-
# @Author  : monleylu
# @Time    : 2018/7/12 3:00 PM
from TestCaseResult import TestCaseResult, TypeEnum
import  time

class UiTestCaseResult(TestCaseResult):
    '''
    UI自动化测试结果
    '''

    def __init__(self, success=False, msg=None, data=None, testcaseid=0, testcasename="defaultTestCaseName",
                 startTime=0, endTime=0):
        super().__init__(success=success, msg=msg, data=data, testcaseid=testcaseid, testcasename=testcasename,
                         startTime=startTime, endTime=endTime, type=TypeEnum.UI.value)


if __name__ == "__main__":
    t = UiTestCaseResult(success=True,msg="aah")
    t.startTimer()
    time.sleep(5)
    t.stopTimer()
    t.testcasename="这是测试测试"
    t.data="aahha"
    print(t.toString())
