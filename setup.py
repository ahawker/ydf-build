"""
    ydf-build
    ~~~~~~~~~

    Generate YAML files for `ydf` to support many environments.

    :copyright: (c) 2017 Andrew Hawker.
    :license: Apache 2.0, see LICENSE file.
"""

import ast
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version_regex = re.compile(r'__version__\s+=\s+(.*)')


def get_version():
    with open('ydf/__init__.py', 'r') as f:
        return str(ast.literal_eval(version_regex.search(f.read()).group(1)))


setup(
    name='ydf-build',
    version=get_version(),
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/ydf-build',
    license='Apache 2.0',
    description='Generate YAML files for ydf',
    long_description=__doc__,
    packages=['ydf-build'],
    install_requires=[
        'click',
        'ydf'
    ],
    entry_points="""
        [console_scripts]
        ydf-build=ydf-build.cli:main
    """,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    )
)
