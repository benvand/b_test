"""
test b
"""
from setuptools import setup, find_packages


version='1'


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
    install_requires=[
        'c_test==1',
    ],
    dependency_links=[
        'git+https://github.com/benvand/c_test.git#egg=c_test-1'
    ],
)
