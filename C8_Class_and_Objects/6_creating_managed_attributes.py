"""
You want to add extra processing
(e.g., type checking or validation) to the getting or setting of an instance attribute.
"""

class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    """
    Init method call first_name method and the internal value is _first_name
    """

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

if __name__ == '__main__':
    p = Person(42)
    p.first_name = 42
    del p.first_name