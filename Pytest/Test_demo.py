import pytest

def test_1():
    name = 'kalaivanan'
    assert name.upper() == "KALAIVANAN"

@pytest.mark.login
def test_2():
    assert False  # ⚠️ This will fail on purpose

def test_3():
    assert True

@pytest.mark.login
def test_login():
    assert "admin" == "admin"

def test3():
    assert 100 == 100

@pytest.mark.login
def test_4():
    assert "kalai" == "KALAI"

def test_id():
    assert "kalai" == "KALAI"

