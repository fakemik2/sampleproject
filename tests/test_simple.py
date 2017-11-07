# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import sample


def test_success():
    assert True


def test_foo():
    assert sample.foo()[1] == 1
