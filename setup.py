import cli
from distutils.core import setup

setup(
    name = 'random-rename',
    packages = 'random-rename',
    version = '1.0',
    license='MIT',
    description='A python package that implements non-deterministic renaming of files',
    author='Deji Atoyebi', 
    author_email='itisdeji@gmail.com',
    url='https://github.com/dejicranium',
    download_url='https://github.com/dejicranium/random-rename/archive/v1.0.tar.gz',
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',      
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts': ['randren=cli:main'],
    }
)