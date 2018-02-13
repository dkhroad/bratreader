from setuptools import setup

setup(name='bratreader',
      version="0.2",
      description="Converts Brat standoff annotations to SpaCy JSON format",
      url='https://github.com/dkhroad/bratreader',
      author='Devinder Khroad',
      author_email='dkhroad@gmail.com',
      licence='MIT',
      packages=['bratreader'],
      install_requires=['simplejson'],
      scripts=['bin/brat2spacy'],
      zip_safe=True)
