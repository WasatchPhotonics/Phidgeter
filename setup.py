import os

from setuptools import setup, find_packages

# These will break the travis build.
#here = os.path.abspath(os.path.dirname(__file__))
#with open(os.path.join(here, "README.txt")) as f:
#    README = f.read()
#with open(os.path.join(here, "CHANGES.txt")) as f:
#    CHANGES = f.read()

README=""
CHANGES=""

requires = [
    #"pytest",
    #"pytest-cov",
    #"pytest-qt",
    #"phidgets",
    ]

setup(name="phidgeter",
      version="0.0",
      description="phidgeter - logging and control wrappers for Phidgets",
      long_description=README + "\n\n" + CHANGES,
      classifiers=[],
      author="",
      author_email="",
      url="",
      keywords="",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite="phidgeter",
      install_requires=requires,
      )
