# pylint: skip-file  <-- delete this line to see the warnings
"""This is a module docstring (1)"""

# Possible pylint warning:
# - 1. Missing module docstring Pylint(C0114:missing-module-docstring)
# - 2. Final newline missing Pylint(C0304:missing-final-newline)
# - 3. Missing function or method docstring Pylint(C0116:missing-function-docstring)
# - 4. Line too long (129/100) Pylint(C0301:line-too-long)

def print_hello_world():
    """
    This is a function / method docstring
    """
    print("Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd Hello Wolrd")  #pylint: disable=line-too-long

# This is a new empty line but it resolves newline missing warning
