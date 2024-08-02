.PHONY: all ex00 ex01 ex02 style_fix style_check

all: style_fix style_check

ex00:
	python3 ex00.py

ex01:
	python3 ex01.py

ex02:
	python3 ex02.py

style_fix:
	autopep8 --in-place --aggressive --aggressive *.py

style_check:
	pycodestyle *.py