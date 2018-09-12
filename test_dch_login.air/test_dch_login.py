# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from dch_common import config
auto_setup(__file__)
config.setup()
start_app("com.iris.dch.itask")
sleep(5)
txt1 = ''
try:
    txt1 = poco("com.iris.dch.itask:id/btn_login").get_text()
except BaseException as e:
    txt = ''
    print (u'未获取到元素:',e)
if txt1 == '登录':
    poco("com.iris.dch.itask:id/et_login_user").click()
    #text("auto_test")
    text(config.login_user())
    poco("com.iris.dch.itask:id/et_login_psw").set_text(config.login_pwd())
    #text("111111")
    #不同手机要用set_text 和 text() 两个方法来实现，坑爹啊
    #text(config.login_pwd())
    keyevent("Enter")
    poco("com.iris.dch.itask:id/btn_login").click()
    sleep(3)
    txt2 = poco(text="时间").get_text()
    assert_equal(txt2,'时间','登录成功')

else:
    poco("com.iris.dch.itask:id/im_circle").click()
    poco("com.iris.dch.itask:id/tv_menu_tuichu").click()
    poco("com.iris.dch.itask:id/et_login_user").click()
    #text("auto_test")
    text(config.login_user())
    poco("com.iris.dch.itask:id/et_login_psw").set_text(config.login_pwd())
    #text("111111")
    #text(config.login_pwd())
    keyevent("Enter")
    poco("com.iris.dch.itask:id/btn_login").click()
    sleep(3)
    txt2 = poco(text="时间").get_text()
    assert_equal(txt2,'时间','登录成功')









