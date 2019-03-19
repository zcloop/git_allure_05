import allure #pytest测试框架中的一个插件，用来生成测试报告
import pytest


class Test01():
    @allure.step("这是测试第一步") #测试用例步骤描述，只能加在方法上面，不能加到方法内部
    def test01(self):
        allure.attach("点击登录","") #测试用例详细描述，可为空字符串，但两个参数必不可少
        allure.attach("输入用户名", "")
        allure.attach("输入密码", "")
        print("test01被执行")

    @allure.step("这是测试第二步")
    def test02(self):
        print("test02被执行")

    @allure.step("这是测试第三步")
    def test03(self):
        print("test03被执行")
        print("断言失败，截图并写入报告")
        with open("./image/failure.png","rb") as f: #图片读写以rb/wb模式打开
            #allure.attach("描述",图片读取,图片类型)
            allure.attach("失败原因：",f.read(),allure.attach_type.PNG)

    @allure.step("这是测试第四步")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)#设置用例优先级
    def test04(self):
        print("test04被执行")

    @allure.step("这是测试第五步")
    @allure.severity("blocker") # 设置用例优先级
    def test05(self):
        print("test05被执行")

    @allure.step("这是测试第六步")
    @allure.severity("trivial") # 设置用例优先级 ,如果断言错误，那么这也是bug的严重级别
    def test06(self):
        print("test06被执行")
        assert False #断言错误