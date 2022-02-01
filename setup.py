from setuptools import setup, find_packages

VERSION = '0.0.1'

with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
        if line and not line.startswith("#")
    ]

setup(
    name="mkdocs-active-handout",
    version=VERSION,
    url='https://github.com/insper-education/active-handout-theme',
    license='',
    description="MkDocs theme for Insper's active handouts",
    author='Igor Montagner',
    author_email='igordsm@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'mkdocs.themes': [
            'active-handout = active_handout',
        ]
    },
    zip_safe=False
)
