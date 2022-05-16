clean:
	rm -rf build dist obfuscate.spec .pytest_cache **/__pycache__ coverage.xml .coverage coverage_html unit_test_results csv_obfuscator_win
initialize:
	poetry install
analyze: initialize
	poetry run pylint --rcfile=.pylintrc csv_obfuscator
	poetry run flake8 --ignore=E501,E722 csv_obfuscator
quick-test:
	poetry run pytest --ignore=./winpython
unit-test: analyze
	poetry run pytest -s -vv --cov=csv_obfuscator/ --junit-xml="./unit_test_results/test_results.xml" --cov-report term-missing  --ignore=./winpython
	poetry run coverage xml
	poetry run coverage html -d coverage_html
	poetry run coverage report --fail-under 90 --skip-covered
build-mac: clean unit-test
	poetry run pyinstaller -w -F --clean "./obfuscate.py"
	ditto -c -k --sequesterRsrc dist/ dist/csv_obfuscator_mac.zip
	zip -d dist/csv_obfuscator_mac.zip csv_obfuscator_mac.zip
	rm -rf dist/obfuscate.app
	rm -rf dist/obfuscate
build-win: clean unit-test
	mkdir csv_obfuscator_win
	cp -R ./winpython ./csv_obfuscator_win/winpython
	cp -R ./csv_obfuscator ./csv_obfuscator_win/csv_obfuscator
	cp obfuscate.py ./csv_obfuscator_win/obfuscate.py
	cp obfuscate.bat ./csv_obfuscator_win/obfuscate.bat
	zip -r "./dist/csv_obfuscator_win.zip" "./csv_obfuscator_win"
	rm -rf csv_obfuscator_win
build: build-mac build-win
	echo "Build Complete"
