.PHONY: default

NAME=put
VERSION=0.0.1

PYTHON=python3
PIP=$(PYTHON) -m pip
GIT=git

default:
	@echo "build target is required"
	@exit 2
devinstall:
	$(PIP) install -e .
sandboxinstall:
	$(PIP) install -i https://test.pypi.org/simple/ $(NAME)
prodinstall:
	$(PIP) install $(NAME)
uninstall:
	$(PIP) uninstall -y $(NAME)
check:
	$(PYTHON) -c "import $(NAME); print($(NAME).__version__); print($(NAME).__dir__())"
devcheck: devinstall check
version:
	$(PYTHON) setup.py --version
tag:
	$(GIT) tag $(VERSION)
untag:
	$(GIT) tag -d $(VERSION)
clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	@rm -rf *.egg-info/ build/ dist/ MANIFEST .pytest_cache/
build: clean
	$(PYTHON) setup.py sdist bdist_wheel
test:
	$(PYTHON) setup.py test
pushsandbox:
	$(PYTHON) -m twine upload dist/* -r testpypi
pushprod:
	@if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "master" ]; then echo "must be on the master branch"; exit 3; fi
	$(PYTHON) -m twine upload dist/*
publish: test tag build pushsandbox pushprod
