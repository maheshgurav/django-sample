echo "This script will install required modules for running home test"
python get-pip.py
pip install nltk
pip install distance
pip install sortedcontainers
pip install django
pip install djangorestframework
python module_checker.py