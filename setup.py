from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-extwidget',
    version=version,
    description="This is a CKAN extension to create embedabble responsive widgets in other sites.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='No\xc3\xa9 Dom\xc3\xadnguez Porras',
    author_email='noe@codeandomexico.org',
    url='http://www.codeandomexico.org',
    license='AGPL V3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.extwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.extwidget.plugin:PluginClass
    ''',
)
