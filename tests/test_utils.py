"""Test ultilities"""

from src.utils.utils import get_none

def test_get_none():
    """
    This function return None
    Its purpose is for pytest GitHub Actions demo
    """
    assert get_none() == None