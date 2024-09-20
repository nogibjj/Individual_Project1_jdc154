install: #installs requirements
	pip install --upgrade pip && pip install -r requirements.txt
#ensures pip works?

format: #formats files
	black *.py

lint: #checks that python files are 
	#pylint --ignore-patterns=test_.*?py *.py
	ruff check test_*.py && ruff check *.py
	nbqa ruff *.ipynb
	
test:
	python -m pytest -cov=main test_*.py
	py.test --nbval *.ipynb

all: install format lint test
