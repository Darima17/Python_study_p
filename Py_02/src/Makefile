.PHONY: all ex00 ex01 style_fix style_check unit_tests

all: style_fix style_check

ex00:
	python3 ex00.py

ex01:
	python3 ex01.py

unit_tests:
	python3 unit_test.py

style_fix:
	autopep8 --in-place --aggressive --aggressive *.py

style_check:
	pycodestyle *.py --ignore=E501