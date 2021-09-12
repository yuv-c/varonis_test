import unittest
from magic_list import MagicList
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.magic_list = MagicList()
        cls.magic_list_with_cls_type = MagicList(cls_type=Person)

    def test_boundary_check(self):
        try:
            self.magic_list[0] = 5
            assert self.magic_list[-1] == 5
        except IndexError:
            assert False

    def test_support_cls_type(self):
        try:
            self.magic_list.age
            assert False  # Should not reach here
        except AttributeError:
            pass
        assert self.magic_list_with_cls_type.age == 1

    def test_index_continuity(self):
        try:
            self.magic_list_with_cls_type[-5]
            assert False  # Should not reach here
        except IndexError:
            pass
