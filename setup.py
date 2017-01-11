from distutils.core import setup

from hal.version import __version__ as version

setup(
    name='hal-assistant',
    packages=['hal'],
    version=version,
    description='Command Line Assistant',
    author='Anup Pokhrel',
    author_email='virtualanup@gmail.com',
    url='https://github.com/virtualanup/hal',
    download_url='https://github.com/virtualanup/hal/archive/{}.tar.gz'.format(version),
    keywords=['assistant', 'hal'],
    classifiers=[],
    install_requires=[
          'six==1.10.0',
          'simpleeval==0.9.1',
          'pytz==2016.10'
      ],
)
