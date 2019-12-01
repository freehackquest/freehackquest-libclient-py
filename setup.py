import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='libfhqcli',
    version='0.2.23',
    install_requires=['websocket-client>=0.56.0', 'requests>=2.21.0'],
    keywords=['ctf', 'fhq', 'fhq-server', 'libfhq-client', 'jeopardy', 'freehackquest'],
    author='FreeHackQuest Team',
    author_email='freehackquest@gmail.com',
    description='FreeHackQuest Python Client Library for fhq-server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/freehackquest/libfhqcli-py',
    packages=['libfhqcli'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ),
    python_requires='>=3.6',
)
