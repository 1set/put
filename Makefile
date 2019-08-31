.PHONY: default

PYTHON=python3
PIP=$(PYTHON) -m pip
NAME=put
VERSION=0.0.1

default:
	@echo "build target is required"
	@exit 2
devinstall:
	$(PIP) install -e .
devuninstall:
	$(PIP) uninstall -y $(NAME)
devcheck: devinstall
	$(PYTHON) -c "import $(NAME); print($(NAME).__version__); print($(NAME).__dir__())"
version:
	$(PYTHON) setup.py --version
build:
	@echo "WIP
	@exit 3
pushtest:
	@echo "WIP
	@exit 3
pushprod:
	@echo "WIP
	@exit 3
