initialize:
	poetry install
analyze: initialize
	poetry run pylint --rcfile=.pylintrc csv_obfuscator
	poetry run flake8 --ignore=E501,E722 csv_obfuscator
unit-test: analyze
	poetry run pytest -s -vv --cov=csv_obfuscator/ --junit-xml="./unit_test_results/test_results.xml" --cov-report term-missing
	poetry run coverage xml
	poetry run coverage html -d coverage_html
	poetry run coverage report --fail-under 90 --skip-covered
quick-test:
	poetry run pytest
