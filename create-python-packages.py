from setuptools import setup

setup(
  name='package_name', # package name
  version='0.1', # version
  description='Package Description', # short description
  url='http://example.com', # package URL
  install_requires=[], # list of packages this package depends # on.
  packages=['package_name'], # List of module names that installing
  # this package will provide.
)

[distutils]
index-servers = 
  pypi
  pypitest
[pypi]
repository=https://pypi.python.org/pypi
username=your_username
password=your_password
[pypitest]
repository=https://testpypi.python.org/pypi
username=your_username
password=your_password
