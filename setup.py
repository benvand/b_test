"""
test b
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

version='1'

requirements = list(parse_requirements('requirements.txt',
                                       session=pip.download.PipSession()))

all_dependencies = [str(r.req) for r in requirements]
install_requires = filter(lambda i: not i.startswith('git+https'), all_dependencies)
dependency_links = filter(lambda i: i.startswith('git+https'), all_dependencies)

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
