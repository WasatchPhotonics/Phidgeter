try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Wasatch Photonics Board Roaster',
    'author': 'Nathan Harrington',
    'url': 'http://github.com',
    'download_url': 'Where to download it.',
    'author_email': 'nharrington@wasatchphotonics.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['broaster'],
    'scripts': [],
    'name': 'broaster'
}

setup(**config)
