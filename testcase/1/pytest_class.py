"""
1、定义类
2、创建测试方法test开头
3、创建setup_class,teardowm_class
4、运行查看结果
"""
import pytest

#1、定义类
class TestClass:
    #3、创建setup_class,teardowm_class
    def setup_class(self):
        print("---setup_class---")

    def teardowm_class(self):
        print("---teardown_class---")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

#4、运行查看结果
if __name__ == "__main__":
    pytest.main(["-s","pytest_class.py"])