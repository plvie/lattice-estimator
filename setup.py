from setuptools import setup

setup(
    name='lattice-estimator',
    version='0.1',
    description='Lattice Estimator fork',
    author='',
    packages=['estimator'],
    install_requires=[
        "black",
        "flake8",
        "pyproject-flake8",
        "pytest",
        "pytest-xdist",
        "nbmake",
        "sphinx-book-theme",
        "sphinxcontrib-jupyter",
    ],
)
