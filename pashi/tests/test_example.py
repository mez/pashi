from unittest import TestCase


class TestExample(TestCase):
    def test_is_string(self):
        s = "pashi"
        self.assertTrue(s=='pashi')