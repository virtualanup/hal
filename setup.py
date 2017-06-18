from distutils.core import setup

version = '0.3'
setup(
    name='hal-assistant',
    packages=['hal', 'hal.libraries'],
    version=version,
    description='Command Line Assistant',
    author='Anup Pokhrel',
    author_email='virtualanup@gmail.com',
    url='https://github.com/virtualanup/hal',
    download_url='https://github.com/virtualanup/hal/archive/{}.tar.gz'.format(
        version),
    keywords=['assistant', 'hal'],
    classifiers=[],
    entry_points={
        "console_scripts": [
            "hal=hal:main",
        ]
    },
    install_requires=[
        'numpy==1.11.3',
        'python-chess==0.18.2',
        'pytz==2016.10',
        'quantities',
        'simpleeval==0.9.1',
        'simplejson==3.10.0',
        'six==1.10.0',
        'yahoo-finance==1.4.0',
        'semantic3==1.0.2',
    ],
)
