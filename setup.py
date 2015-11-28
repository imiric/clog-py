from setuptools import setup, find_packages

import versioneer

setup(
    name='clog-py',
    version=versioneer.get_version(),
    cmd_class=versioneer.get_cmdclass(),
    url='https://github.com/imiric/clog-py',
    description='centralized logging Python client',
    author='Ivan Mirić',
    author_email='imiric@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Logging',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests==2.8.1'
    ]
)
