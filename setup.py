from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name='plugout',
    description="A simple plugin manager",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[],
    install_requires=[],
    tests_require=['coverage'],
    author='Maxime Beauchemin',
    author_email='maximebeauchemin@gmail.com',
    url='https://github.com/misetrcrunch/plugout',
    download_url=('https://github.com/mistercrunch/plugout/tarball/' + VERSION),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
