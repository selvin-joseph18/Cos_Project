from setuptools import setup, find_packages

setup(
    name='selvin_egg',
    version='1.0.0',
    packages=find_packages(),
    url='',
    entry_points={'setuptools.installation': ['eggsecutable = src.main.main:main'], },
    data_files=[('.', ['__main__.py'])],
    license='',
    author='selvin.joseph',
    author_email='',
    description='My egg file'


)
