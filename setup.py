from setuptools import setup, find_packages
import os, sys

execfile('PySO8601/__version__.py')

setup(name="PySO8601",
      description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      version=__version__,
      url="http://digitala.github.com/PySO8601",
      packages=find_packages(exclude="specs"),
      install_requires=['lxml','ordereddict'],
      )
      
