initialize:
	poetry install
analyze: initialize
	poetry run pylint --rcfile=.pylintrc csv_obfuscator
	poetry run flake8 --ignore=E501,E722 csv_obfuscator
quick-test:
	poetry run pytest
unit-test: analyze
	poetry run pytest -s -vv --cov=csv_obfuscator/ --junit-xml="./unit_test_results/test_results.xml" --cov-report term-missing
	poetry run coverage xml
	poetry run coverage html -d coverage_html
	poetry run coverage report --fail-under 90 --skip-covered
build: unit-test
	poetry run pyinstaller -w -F --clean "./obfuscate.py"
clean:
	rm -rf build dist obfuscate.spec .pytest_cache **/__pycache__ coverage.xml .coverage coverage_html unit_test_results
