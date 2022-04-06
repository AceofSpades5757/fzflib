import os
import shutil
import unittest
from pathlib import Path
from typing import Callable

from fzf import FZF


os.chdir(Path(__file__).parent)
TARGET_DIR: Path = Path(__file__).parent / 'fzf'


def error_handler(function: Callable, path: str, exc_info) -> None:
    # Change Permission
    try:
        os.chmod(path, 0o777)
        Path(path).unlink()
    except Exception:
        # Unknown Error
        ...


class TestCase(unittest.TestCase):
    """Test Case"""

    def setUp(self):
        self.skipTest("Test downloads and runs an install.")
        if Path(TARGET_DIR).exists():
            shutil.rmtree(TARGET_DIR, onerror=error_handler)

    def tearDown(self):
        shutil.rmtree(TARGET_DIR, onerror=error_handler)

    def test_default(self):
        FZF.install()
        self.assertEquals(Path(TARGET_DIR).exists(), True)

    def test_http(self):
        FZF.install('http')
        self.assertEquals(Path(TARGET_DIR).exists(), True)

    def test_https(self):
        FZF.install('https')
        self.assertEquals(Path(TARGET_DIR).exists(), True)

    def test_ssh(self):
        FZF.install('ssh')
        self.assertEquals(Path(TARGET_DIR).exists(), True)

    def test_gh(self):
        FZF.install('gh')
        self.assertEquals(Path(TARGET_DIR).exists(), True)


if __name__ == '__main__':
    unittest.main()
