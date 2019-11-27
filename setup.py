from setuptools import setup, find_packages

install_requires = []

with open('requirements.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            install_requires.append(line)

setup(
    name='pszt_n_puzzle',
    version=1.0,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'n_puzzle = pszt_n_puzzle.main:main'
        ]
    },
)
