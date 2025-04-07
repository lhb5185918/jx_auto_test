基线产品-自动化测试框架
-----------------------------------------------------------------------------------------------------------------

1、基线产品-自动化测试框架
1、1主要通过python+pytest+allure实现
2、主要功能
2、1包含基础资料、入库、出库、库内、报表、gsp、配送管理模块

-----------------------------------------------------------------------------------------------------------------

使用方式：
直接运行run.py文件即可，执行所有测试用例
执行完成用例后，可以执行airun.py文件，生成智能化测试报告，如果不运行aitun.py文件是无法使用ai文档服务的


--------------------------------------------------------------------------------------------------------------------

相关依赖：
注意，python版本不能大于3.8，如果大于3.8版本，因为pytest兼容性的原因，会引起问题

--------------------------------------------------------------------------------------------------------------------

代码规范：
1、测试数据放在testdata目录下，以yaml的形式存放
2、需要的中间数据-比如说id、obj等需要参数化的数据，也放在testdata目录下，命名中会多一个middle证明是中间数据
3、测试用例存放在testcase目录下，命名规则为test_开头
4、测试用例中需要的token、钩子等函数放置在conftest文件中，以pytest的fixture的形式存在
5、测试用例编写中的公共工具放在utils目录下，ding_webhook【钉钉通知工具】、get_yaml_data【yaml文件读取写入工具】、log【日志工具】、mysql【mysql操作工具】、requests_util【请求方法二次封装，全量的请求工具】
time_decorator【响应时间装饰器工具】、other_utils【其他工具-包含批号生成工具、随机数生成工具、时间生成工具】
6、测试用例编写中的公共方法放置在common目录下，现在主要是封装的断言工具
7、测试用的文件路径放置在config目录下，主要是文件路径配置
8、编写自动化测试用例时，需要先构筑测试数据、构筑完成后导入到对应的测试用例文件中，需要在class中添加一个初始化方法，将读取测试用例的方法初始化，读取后，直接用parametrize装饰器装饰方法即可