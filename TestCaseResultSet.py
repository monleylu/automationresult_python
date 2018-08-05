# -*- coding: utf-8 -*-
# @Author  : monleylu
# @Time    : 2018/7/12 3:36 PM
from BaseResult import BaseResult
from UiTestCaseResult import UiTestCaseResult
from InterfaceTestCaseResult import InterfaceTestCaseResult
import json


class TestCaseResultSet:
    '''
    测试结果集
    '''

    def __init__(self, name="defaultname", key=None, time=None, departmentID=None, departmentName=None):

        # title to aggregation test
        self.name = name

        # uuid ,for bi to distinguish diffient data,if is the same ,bi will union data
        self.key = key

        # use this to show timeline,if serval data come with same key, use the first time
        self.time = time

        # department id
        self.departmentID = departmentID

        # departement name
        self.departmentName = departmentName

        # list of TestCaseResult
        self.data = []

    def toString(self):
        return json.dumps(self.toJson(), ensure_ascii=False)

    def toJson(self):
        tmpdata = []
        if isinstance(self.data, list):
            for i in self.data:
                if isinstance(i, BaseResult):
                    tmpdata.append(i.toJson())
                else:
                    print("error")
        else:
            print("data is not list")

        return {"name": self.name,
                "key": self.key,
                "time": self.time,
                "departmentID": self.departmentID,
                "departmentName": self.departmentName,
                "data": tmpdata
                }


if __name__ == "__main__":
    t = UiTestCaseResult(testcasename="adsfads")
    t.startTimer()
    t.stopTimer()
    t2 = InterfaceTestCaseResult(success=True)
    t2.startTimer()
    t2.stopTimer()
    t3 = BaseResult(success=True, msg="基础测试", data={"adsf": 1})
    l = TestCaseResultSet(name="自动化测试", key="201801030405",departmentName="xmonley",time=1533465771 )
    l.data = [t, t2, t3]
    # l.data = {"asdf"}
    print(l.toString())
