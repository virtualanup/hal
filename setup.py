from distutils.core import setup
setup(
    name='hal',
    packages=['hal'],
    version='0.1',
    description='Command Line Assistant',
    author='Anup Pokhrel',
    author_email='virtualanup@gmail.com',
    url='https://github.com/virtualanup/hal',
    download_url='https://github.com/virtualanup/hal/archive/0.1.tar.gz',
    keywords=['assistant', 'hal'],
    classifiers=[],
    install_requires=[
          'six==1.10.0',
          'simpleeval==0.9.1',
          'pytz==2016.10'
      ],
)
