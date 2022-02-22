raise NotImplementedError("No tests implemented yet.")
import unittest

from fzf import FZF


class TestCase(unittest.TestCase):
    """Test Case"""

    def test_simple(self):
        """Simple test"""
        fzf = FZF()
        fzf.run()


if __name__ == '__main__':
    unittest.main()
