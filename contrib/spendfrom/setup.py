from distutils.core import setup
setup(name='dtcspendfrom',
      version='1.0',
      description='Command-line utility for datacoin "coin control"',
      author='Gavin Andresen',
      author_email='gavin@bitcoinfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
