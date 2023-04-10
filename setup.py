from setuptools import setup

setup(
    name='pymplu',
    version='0.0.1',    
    description='A set of utilities to make plots with matplotlib',
    url='https://github.com/giovastabile/pymplu',
    author='Giovanni Stabile',
    author_email='giovanni.stabile@uniurb.it',
    license='BSD 2-clause',
    packages=['pymplu'],
    install_requires=['matplotlib',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
