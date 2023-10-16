from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("C:/Users/Lenovo/Documents/SEM 5/Advanced Python/chutiya/lib/pygame_sdl2/src/pygame_sdl2/font.pyx")
)
