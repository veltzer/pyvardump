from typing import List


config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = []
make_requires: List[str] = [
    "pyclassifiers",
    "pydmt",
    "pymakehelper",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
