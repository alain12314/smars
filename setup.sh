#!/bin/bash
echo Setting up SMARS Python Environment
echo -----------------------------------
pip install --user pipenv
sudo pipenv install
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
