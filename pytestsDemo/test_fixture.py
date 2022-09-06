import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I execute setup method in this method1")

    def test_fixtureDemo2(self):
        print("I execute setup method in this method2")

    def test_fixtureDemo3(self):
        print("I execute setup method in this method3")

    def test_fixtureDemo4(self):
        print("I execute setup method in this method4")