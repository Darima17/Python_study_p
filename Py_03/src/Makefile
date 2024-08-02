.PHONY: all ex00 run_server open_ex00 ex01_consumer ex01_producer ex02 style_fix

all: style_fix

ex00:
	python3 exploit.py

run_server: 
	python3 -m http.server --bind 127.0.0.1 8000

open_ex00:
	open http://127.0.0.1:8000/evilcorp_hacked.html

ex01_producer:
	python3 producer.py

ex01_consumer:
	python3 consumer.py -e 1111111111,2222222222,3333333333

ex02:
	python3 gen_ansible.py

style_fix:
	autopep8 --in-place --aggressive --aggressive *.py