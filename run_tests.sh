#!/usr/bin/env bash

rm -f .coverage
python setup.py nosetests
