from sg_hello_pypi import identity


def test_identity_returns_args():
    assert identity(1, 2, 3) == (1, 2, 3)
