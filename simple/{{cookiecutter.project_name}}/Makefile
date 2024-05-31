TOPLEVEL_LANG = verilog

SIM ?= {{cookiecutter.simulator}}

PWD=$(shell pwd)

VERILOG_SOURCES += $(PWD)/{{cookiecutter.dut}}.sv

VERILOG_SOURCES += $(PWD)/{{cookiecutter.dut}}_wrapper.sv

TOPLEVEL = {{cookiecutter.dut}}

MODULE = test_{{cookiecutter.dut}}

include $(shell cocotb-config --makefiles)/Makefile.sim


