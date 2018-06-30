#!/bin/bash

# Tutorial: https://packaging.python.org/tutorials/packaging-projects/


# clean
rm -rf build
rm -rf dist
rm -rf libfhqcli.egg-info

python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

