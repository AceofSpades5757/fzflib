import unittest

from fzflib import FZF


class TestCase(unittest.TestCase):
    """Test Case"""

    def test_simple(self):
        fzf = FZF()
        self.assertIsNotNone(fzf)


if __name__ == '__main__':
    unittest.main()
