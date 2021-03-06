VENV_NAME?=.venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	pip install --upgrade pip virtualenv
	@test -d $(VENV_NAME) || python -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -U pip tox
	${VENV_NAME}/bin/python -m pip install -e .
	@touch $(VENV_NAME)/bin/activate

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

ci: venv
	@${VENV_NAME}/bin/python setup.py test -a "-n auto --cov=cohesivenet"

fmt: venv
	@${VENV_NAME}/bin/tox -e fmt

fmtcheck: venv
	@${VENV_NAME}/bin/tox -e fmt -- --check --verbose

lint: venv
	@${VENV_NAME}/bin/tox -e lint

build: venv
	@${VENV_NAME}/bin/python setup.py build sdist bdist_wheel

cleanbuild:
	@rm -rf build/ dist/

clean: cleanbuild
	@rm -rf $(VENV_NAME)

.PHONY: venv test ci fmt fmtcheck lint clean build cleanbuild