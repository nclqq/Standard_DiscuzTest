import sys
sys.path.append("E:\Discuz")

import unittest
import os
import HTMLTestRunner

from testsuites.test_LoginSendMail import TestLoginSend
from testsuites.test_manage import TestManageCreate
from testsuites.test_search import TestSearch
from testsuites.test_vote import TestVote

#E:\DiscuzTest
current_path=os.path.abspath('.') #获取当前路径（用例路径）
print(current_path)
report_path=os.path.join(current_path,"/report") #设置报告路径，并且路径名是report(报告存放路径)
print(report_path)
if not os.path.exists(report_path):
    os.mkdir(report_path)

#构造测试套件
suite=unittest.TestSuite() #创建套件
suite.addTest(unittest.makeSuite(TestLoginSend)) #增加home测试
suite.addTest(unittest.makeSuite(TestManageCreate)) #增加two测试
suite.addTest(unittest.makeSuite(TestSearch)) #增加three测试
suite.addTest(unittest.makeSuite(TestVote)) #增加four测试

if __name__=="__main__":
    #打开一个文件，将result写入此file中
    html_report=report_path+r"\result.html" #（html报告文件路径）
    fp=open(html_report,"wb")

    #初始化一个htmltestrunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)