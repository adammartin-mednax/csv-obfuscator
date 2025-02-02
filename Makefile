clean:
	rm -rf build dist obfuscate.spec .pytest_cache **/__pycache__ coverage.xml .coverage coverage_html unit_test_results csv_obfuscator_win
initialize:
	poetry install
analyze: initialize
	poetry run pylint --rcfile=.pylintrc csv_obfuscator
	poetry run flake8 --ignore=E501,E722 csv_obfuscator
quick-test: initialize
	poetry run pytest --ignore=./winpython
unit-test: analyze
	poetry run pytest -s -vv --cov=csv_obfuscator/ --junit-xml="./unit_test_results/test_results.xml" --cov-report term-missing  --ignore=./winpython
	poetry run coverage xml
	poetry run coverage html -d coverage_html
	poetry run coverage report --fail-under 90 --skip-covered
install-in-linux: clean initialize
	poetry run pyinstaller -w -F --clean "./obfuscate.py"
build-docker: clean
	docker build -t csv_obfuscator_linux .
build: build-docker
	$(info Build Complete)
all: build
