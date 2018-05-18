PYTHON_BIN := $(shell which python3)
PYTHON_VER := $(word 2,$(shell $(PYTHON_BIN) -V 2>&1))

.PHONY: run
run:
	$(PYTHON_BIN) echo.py
