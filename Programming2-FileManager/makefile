.PHONY: install test clean

install:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

test:
	./venv/bin/pytest -q

clean:
	find . -type f -name "*.txt" -not -path "./venv/*" -delete
