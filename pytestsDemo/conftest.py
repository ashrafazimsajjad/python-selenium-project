import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("User profile created")
    return ["Sajjad", "Hossain", "sajjadhossain"]


@pytest.fixture(params=[("chrome", "Sajjad", "Hossain"), ("Firefox", "Hossain"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
