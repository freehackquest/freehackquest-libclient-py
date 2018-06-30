import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='libfhqcli',
    version='0.2.15',
    author='FreeHackQuest Team',
    author_email='freehackquest@gmail.com',
    description='FreeHackQuest Python Client Library for fhq-server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/freehackquest/libfhqcli-py',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    )
)
