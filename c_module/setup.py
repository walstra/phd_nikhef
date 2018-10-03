'''
\brief Build file.
'''

from distutils.core import setup, Extension

hellomodule = Extension('hello', sources = ['hellomodule.c'])

setup (
    name           = 'hello',
    version        = '1.0',
    description    = 'Simple demo package for Python C extensions',
    ext_modules    = [hellomodule]
)
