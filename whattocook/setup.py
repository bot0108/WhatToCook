from setuptools import setup, find_packages

setup(name='whattocook',
      version='0.1',
      url='https://github.com/bot0108/WhatToCook.git',
      description='WhatToCookProgram',
      author='Botond Grinacz',
      license='MIT',
      packages=find_packages(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      install_requires=['reportlab']
)