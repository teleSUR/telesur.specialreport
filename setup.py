# -*- coding: utf-8 -*-
"""Installer for the collective.flash_specials package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='collective.flash_specials',
    version='0.1',
    description="Content type to upload flash files.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone, flash',
    author='Juan Pablo Giménez',
    author_email='jpg@rosario.com',
    url='http://pypi.python.org/pypi/collective.flash_specials',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'five.pt',
        'Pillow',
        'Plone',
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
