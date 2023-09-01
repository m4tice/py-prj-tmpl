"""Test ultilities"""

from src.utils.utils import get_none


def test_get_none():
    """
    Assert get_none()
    Expected return of get_none() is 'None'
    """
    assert get_none() is None
