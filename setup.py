from setuptools import setup, find_packages
import os, sys

execfile('PySO8601/__version__.py')

setup(name="PySO8601",
      description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      version=(0,1,3), #__version__,
      url="http://unpluggd.github.com/PySO8601",
      packages=find_packages(exclude="specs"),
      )
      
