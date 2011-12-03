from setuptools import setup, find_packages

setup(
    name='django-bootstrapped',
    version='0.1.0-dev',
    description='A reusable Django application to quickly integrate the Bootstrap toolkit from Twitter.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Ryan Brady',
    author_email='ryan@ryanbrady.org',
    url='https://github.com/rbrady/django-bootstrapped',
    download_url='https://github.com/rbrady/django-bootstrapped/downloads',
    license='BSD',
    packages=find_packages(exclude=('ez_setup', 'tests', 'example')),
    # tests are on the roadmap
    #tests_require=[
    #    'django>=1.3,<1.4',
    #],
    #test_suite='runtests.runtests',
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)