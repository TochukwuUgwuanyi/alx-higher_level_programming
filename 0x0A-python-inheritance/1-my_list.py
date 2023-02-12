#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """implements sorted printing for built-in list classs"""

    def print_sorted(self):
        """function that Print list in ascending sort """
        print(sorted(self))
