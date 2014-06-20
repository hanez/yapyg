from os import environ
from os.path import dirname, join
from distutils.core import setup
from distutils.extension import Extension
try:
        from Cython.Build import cythonize
        have_cython = True
except ImportError:
        have_cython = False

if have_cython:
        ext = cythonize("yapyg/*.pyx") + cythonize("yapyg_movers/*.pyx")
else:
        ext = [ Extension('yapyg/fixpoint', ['yapyg/fixpoint.c']),
                Extension('yapyg/collisions', ['yapyg/collisions.c']),
                Extension('yapyg/movers', ['yapyg/movers.c']),
                Extension('yapyg/sprites', ['yapyg/sprites.c']),
                Extension('yapyg/widget', ['yapyg/widget.c']),
                Extension('yapyg_movers/physical', ['yapyg_movers/physical.c']),
                ]

setup(  name='yapyg',
        version='0.1.0',
        description='Yet Another Python Game Engine',
        author='Raihan Kibria',
        author_email='raihan@kibria.de',
        url='https://github.com/rkibria/yapyg',
        packages=['yapyg', 'yapyg_helpers', 'yapyg_movers', 'yapyg_viewers'],
        ext_modules=ext
        )
