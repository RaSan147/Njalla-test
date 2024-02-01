from setuptools import setup, find_packages

setup(
    name='Njalla',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            # Include any console scripts here
        ],
    },
)
