import sys
from setuptools import setup, find_packages

setup(
    name="pix-to-xls",
    version="1.0.1",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="A simple tool to make ascii art from an image using excel colored cells",
    long_description="A simple tool to make ascii art from an image using excel colored cells",
    url="https://github.com/joelibaceta/pix-to-xls",
    project_urls={
        'Source': 'https://github.com/joelibaceta/pix-to-xls',
        'Tracker': 'https://github.com/joelibaceta/pix-to-xls/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xlrd', 'getkey'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='xls pixel-art images',
    entry_points={
        "console_scripts": [
            'pix-to-xls=pix_to_xls.cli:main'
        ]
    }
)
