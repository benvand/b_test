"""
test b
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

version='1'

requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))

setup(
    name='test_b',
    version='1',
    url='https://github.com/benvand/test_b',
    license='MIT',
    author='benvand',
    description='B',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['git+https://github.com/benvand/c_test.git'],
    dependency_links=['git+https://github.com/benvand/c_test.git'],
)
