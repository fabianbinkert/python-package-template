from src.example_package_binkertf.example import add_one


def test_add_one():
    assert add_one(1.0) == 2.0
    assert add_one(-1.0) == 0.0
    assert add_one(0.0) == 1.0
    assert add_one(10.5) == 11.5
