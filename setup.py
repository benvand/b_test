"""
test b
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

version='1'

requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))

install_requires = [str(r.req) for r in requirements]
dependency_links = [i for i in install_requires if i.startswith('git+https')]

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
    install_requires=install_requires,
    dependency_links=dependency_links,
)
