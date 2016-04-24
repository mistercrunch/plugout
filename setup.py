from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(
    name='plugout',
    description="A simple plugin manager",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[],
    install_requires=[],
    tests_require=['coverage', 'coveralls'],
    author='Maxime Beauchemin',
    author_email='maximebeauchemin@gmail.com',
    url='https://github.com/mistercrunch/plugout',
    download_url=('https://github.com/mistercrunch/plugout/tarball/' + VERSION),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
