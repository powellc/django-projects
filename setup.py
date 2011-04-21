from setuptools import setup, find_packages

setup(
    name='django-projects',
    version=__import__('projects').__version__,
    license="BSD",

    install_requires = ['django-markup-mixin','django-extensions','django-eventy',],

    description='A simple reusable application for managing projects in a Django application.',
    long_description=open('README.rst').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-projects',
    download_url='http://github.com/powellc/django-projects/downloads',

    include_package_data=True,

    packages=['projects'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
