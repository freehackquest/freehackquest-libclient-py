#!/bin/bash

# Tutorial: https://packaging.python.org/tutorials/packaging-projects/


# clean
rm -rf build
rm -rf dist
rm -rf libfreehackquestclient.egg-info

python3 setup.py sdist bdist_wheel
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
