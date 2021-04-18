import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='Refrapt',
    version='0.1.1',
    description='A tool to mirror Debian repositories for use as a local mirror.',
    python_requires='>=3.8',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Progeny42/Refrapt",
    author="Progeny42",
    packages=["refrapt"],
    package_data={
        "refrapt": ["refrapt.conf"]
    },
    py_modules=[
        'refrapt', 
        'classes', 
        'helpers'
    ],
    install_requires=[
        'Click >= 7.1.2',
        'Colorama >= 0.4.4',
        'tqdm >= 4.60.0',
        'wget >= 3.2',
        'filelock >= 3.0.12'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: Implementation",
        "Topic :: System :: Archiving :: Mirroring"
    ],
    keywords=['Mirror', 'Debian', 'Repository'],
    entry_points='''
        [console_scripts]
        refrapt=refrapt:refrapt
    ''',
)