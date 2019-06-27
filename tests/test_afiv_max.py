from afivmax.afivmax import afiv_max
import pytest


def test_without_args():
    with pytest.raises(TypeError):
        afiv_max()


def test_iterable_with_no_key_and_default():
    """normal case"""
    assert 3 == afiv_max([1, 2, 3])
    assert 3 == afiv_max([3, 2, 1])
    assert 3 == afiv_max([3])
    with pytest.raises(TypeError):
        # no empty iterable
        assert 3 == afiv_max([]), "should raise exception with empty iterable and default=None"

    assert 9 == afiv_max((i for i in range(10)))


def test_iterable_with_key():
    """iterable with key"""
    assert 3 == afiv_max([1, 2, 3], key=lambda x: x ** 2)

    class TmpClass:
        def __init__(self, x):
            self.val = x

    assert 9 == afiv_max([TmpClass(x) for x in range(10)], key=lambda x: x.val).val


def test_iterable_default():
    """iterable with default only"""
    assert 10 == afiv_max([], default=10), "iterable with default only"
    assert 3 == afiv_max([1, 2, 3], default=10), "iterable with default only"


def test_iterable_with_key_and_default():
    """iterable with key and default"""
    assert 10 == afiv_max([], key=lambda x: x ** 2, default=10), "iterable with key and default"
    assert 3 == afiv_max([1, 2, 3], key=lambda x: x ** 2, default=10), "iterable with key and default"

    class TmpClass:
        def __init__(self, x):
            self.val = x

    assert 9 == afiv_max([TmpClass(x) for x in range(10)], key=lambda x: x.val, default=10).val


def test_iterable_with_duplication():
    """iterable with duplication"""
    assert 1 == afiv_max([1, 1, 1, 1, 1]), "iterable with duplication"


def test_args_with_no_key_and_default():
    """normal case"""
    assert 3 == afiv_max(1, 2, 3), "normal case with args"
    with pytest.raises(TypeError):
        assert 3 == afiv_max(3), "Only one argument which is not iterable is not allowed"


def test_args_with_key():
    """iterable with key"""
    assert 3 == afiv_max(1, 2, 3, key=lambda x: x ** 2), "args with key"

    class TmpClass:
        def __init__(self, x):
            self.val = x

    assert 9 == afiv_max(*[TmpClass(x) for x in range(10)], key=lambda x: x.val).val


def test_args_with_default():
    """args with key and default, should raise exception"""
    with pytest.raises(TypeError):
        afiv_max(1, 2, 3, default=10)


def test_args_with_duplication():
    """iterable with duplication"""
    assert 1 == afiv_max(1, 1, 1, 1, 1), "iterable with duplication"
