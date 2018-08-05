# -*- coding: utf-8 -*-
# @Author  : monleylu
# @Time    : 2018/7/10 5:31 PM

from enum import Enum
from BaseResult import BaseResult
import time, json, requests


class TestCaseResult(BaseResult):
    """
    test case struct
    """

    def __init__(self, success=False, msg=None, data=None, testcaseid=0, testcasename="defaultTestCaseName",
                 startTime=0, endTime=0, type=0):
        super().__init__(success=success, msg=msg, data=data)

        # testcase id,design for future ,now default value is 0
        self._testcaseid = testcaseid

        # testcase name
        self._testcasename = testcasename

        # testcase start run time, time in seconds since the Epoch
        self._startTime = startTime

        # testcase stop run time, time in seconds since the Epoch
        self._endTime = endTime

        # testcase type , 0:undefine , 1:UI , 2:Interface ，detail informaiton define in TypeEnum class
        self._type = type


    @property
    def testcaseid(self):
        return self._testcaseid

    @testcaseid.setter
    def testcaseid(self, value):
        self._testcaseid = value

    @property
    def testcasename(self):
        return self._testcasename

    @testcasename.setter
    def testcasename(self, value):
        self._testcasename = value

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, value):
        self._startTime = value

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def startTimer(self):
        """
        start time
        :return:
        """
        self.startTime = int(time.time())

    def stopTimer(self):
        """
        stop time
        :return:
        """
        self.endTime = int(time.time())

    def toString(self):
        '''
        返回json格式字符串
        :return:返回json格式字符串
        '''
        return json.dumps(self.toJson(), ensure_ascii=False)

    def toJson(self):
        return {"success": self.success,
                "msg": self.msg,
                "testcaseid": self.testcaseid,
                "testcasename": self.testcasename,
                "startTime": self.startTime,
                "endTime": self.endTime,
                "type": self.type,
                "data": self.data
                }


class TypeEnum(Enum):
    '''
    test case type enum value
    '''
    Undefine = 0

    # ui test type
    UI = 1

    # interface test type
    Interface = 2


if __name__ == "__main__":
    t1 = TestCaseResult(success=True)
    t = TestCaseResult()
    t.startTimer()
    t.testcasename = "测试用例名称"
    t.success = True
    t.msg = "adf"
    t.type = TypeEnum.Interface.value
    t.data = "测试过程中的数据，可以存储在这里，任何格式的数据都可以"
    t.stopTimer()
    print(t.toString())
