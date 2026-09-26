#!/usr/bin/env python
from setuptools import find_packages, setup

install_requires = [
    'django>=5.2,<6.0',
    'django-oscar>=4.2,<4.3',
    'python-dateutil>=2.9,<3.0',
]

tests_require = [
    'django-webtest>=1.9.12,<1.10',
    'pytest-cov>=6.0',
    'pytest-django>=4.9',
    'freezegun>=1.5,<2',
    'sorl-thumbnail',
    'factory-boy>=3.3,<4',
    'coverage>=7.6',
    'tox>=4.0',
]


setup(
    name='django-oscar-accounts',
    author="David Winterbottom",
    author_email="david.winterbottom@tangentlabs.co.uk",
    description="Managed accounts for django-oscar",
    long_description=open('README.rst').read(),
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    python_requires='>=3.12',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['setuptools_scm'],
    extras_require={
        'test': tests_require,
    },
    use_scm_version=True,
)
