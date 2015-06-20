from setuptools import setup
from setuptools import find_packages

setup(
    name = "collective.recipe.maildump",
    version = "0.1",
    description = "Buildout recipe to install maildump",
    long_description=read('README.txt'),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications :: Email',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Utilities'
    ],
    keywords='buildout recipe maildump',
    author='Noe Nieto',
    author_email='nnieto@noenieto.com',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zc.buildout',
        # -*- Extra requirements: -*-
        'zc.recipe.egg'
    ],
    entry_points = {'zc.buildout': ['default = collective.recipe.maildump:Recipe']},
)