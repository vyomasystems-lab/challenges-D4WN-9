# See LICENSE.vyoma for details
TOPLEVEL_LANG ?= verilog
PWD=$(shell pwd)
VERILOG_SOURCES = $(PWD)/mux.v
TOPLEVEL := mux
MODULE   := test_mux
include $(shell cocotb-config --makefiles)/Makefile.sim
clean_all: clean
	rm -rf *.xml sim_build __pycache__