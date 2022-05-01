import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

run_requires = [
]

test_requires = [
    'pylint',
    'pytest',
    'pytest-cov',
    'pyflakes',
    'flake8',
    'pymakehelper',
]

dev_requires = [
    'pyclassifiers',
    'pypitools',
    'pydmt',
    'Sphinx',
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.7"

extras_require = {
}
test_os = "[ubuntu-20.04]"
test_python = "[3.7, 3.8, 3.9]"
test_container = "[ubuntu:20.04]"
