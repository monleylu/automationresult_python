# -*- coding: utf-8 -*-
# @Author  : monleylu
# @Time    : 2018/7/10 5:30 PM
import json


class BaseResult:
    def __init__(self,success=False,msg=None,data=None):
        #test result，success or false
        self._success=success

        #brief information about test result
        self._msg=msg

        # test data,store test data,
        self._data = data

    def toString(self):
        '''
        返回json格式字符串
        :return:返回json格式字符串
        '''
        return json.dumps(self.toJson(),ensure_ascii=False)

    def toJson(self):
        return {"success":self.success,"msg":self._msg,"data":self._data}

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self,value):
        self._success=value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self,value):
        self._msg=value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data=value



if __name__ =="__main__":
    b= BaseResult()
    # b.success=True
    b.success=False
    b.msg="测试结果信息"
    # b.data="任意内容"
    print(b.toString())

    b=BaseResult(success=True,msg="这测试",data="haha")
    print(b.toString())