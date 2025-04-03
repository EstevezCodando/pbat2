from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "soma_openmp",
        ["soma_openmp.pyx"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="soma_openmp",
    ext_modules=cythonize(ext_modules, language_level="3"),
)
