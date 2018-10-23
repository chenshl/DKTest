# coding:utf-8
# @author : csl
# @date   : 2018/08/29 15:21
# 自动生成基础接口测试用例，如缺少必填参数、必填参数为空、传入特殊字符类型等
import copy

class creatTestCase(object):
    """自动生成基础参数接口测试用例用于单个接口调用测试"""

    def __init__(self, parmas={}):
        """
        传入字典类型请求参数示例：
        {"key1":"value1",
        "key2":"value2"}
        """
        self.parmas = parmas
        # 定义每个值的固定添加参数类型
        self.values = ["", "*", "&&&", "@", "test", "测试", 0, 0.0]

    def creat_beseTestCase(self):
        """创建基础测试用例参数"""

        result_parmas = []
        # 判断传入的参数为字典类型并且不为空
        if isinstance(self.parmas, dict) and self.parmas:
            # 将设定的value值添加到请求参数
            for values in self.values:
                # 添加到resutl_parmas后每次循环将result_parma置为空
                result_parma = {}
                for keys in self.parmas.keys():
                    result_parma[keys] = values
                result_parmas.append(result_parma)

            # 依次将请求参数中的key值删除，缺省参数
            for keys in self.parmas.keys():
                copyparmas = copy.deepcopy(self.parmas)
                del copyparmas[keys]
                result_parmas.append(copyparmas)
            # 将传入的原始参数添加到返回结果中
            result_parmas.append(self.parmas)
            return result_parmas
        else:
            print("传入参数 {} 为空".format(self.parmas))
            return result_parmas



if __name__ == "__main__":
    r = creatTestCase({"a":"1","b":"2","c":"3"}).creat_beseTestCase()
    print(r)
    rn = creatTestCase().creat_beseTestCase()
    print(rn)