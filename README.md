
# *pyvardump* project by Mark Veltzer

![PyPI - Status](https://img.shields.io/pypi/status/pyvardump)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyvardump)
![PyPI - License](https://img.shields.io/pypi/l/pyvardump)
![PyPI - Package Name](https://img.shields.io/pypi/v/pyvardump)
![PyPI - Format](https://img.shields.io/pypi/format/pyvardump)

![PyPI - Downloads](https://img.shields.io/pypi/dd/pyvardump)
![PyPI - Downloads](https://img.shields.io/pypi/dw/pyvardump)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyvardump)

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

![build](https://github.com/veltzer/pyvardump/workflows/build/badge.svg)

pyvardump helps you dump variables in python

project website: https://veltzer.github.io/pyvardump

chat with me at [![gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/veltzer/mark.veltzer)

The reason for this module is that other dumping solutions cannot easily be used
everywhere.

These solutions usually get stuck on AttributeError or TypeError, fail to list
slots or attributes etc.

I hope to overcome all of these.

This module just exports one function "dump".

