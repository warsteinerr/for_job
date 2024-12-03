import  pytest
from methods.get_list_methods import GetListMethods
from methods.tg_methods import TgMethods

@pytest.fixture
def get_list_method():
    return GetListMethods()

@pytest.fixture
def tg_method():
    return TgMethods()
