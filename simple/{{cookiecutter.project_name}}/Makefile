TOPLEVEL_LANG = verilog

SIM ?= {{cookiecutter.simulator}}

WAVES ?= 1

PWD=$(shell pwd)

VERILOG_SOURCES += $(PWD)/{{cookiecutter.dut}}.sv

VERILOG_SOURCES += $(PWD)/{{cookiecutter.dut}}_wrapper.sv

ifeq ($(SIM), icarus)
        PLUSARGS += -fst

        ifeq ($(WAVES), 1)
                VERILOG_SOURCES += iverilog_dump.v
                COMPILE_ARGS += -s iverilog_dump
        endif
else ifeq ($(SIM), verilator)
        COMPILE_ARGS += -Wno-SELRANGE -Wno-WIDTH

        ifeq ($(WAVES), 1)
                EXTRA_ARGS += --trace --trace-structs
        endif
endif


TOPLEVEL = {{cookiecutter.dut}}

MODULE = test_{{cookiecutter.dut}}

include $(shell cocotb-config --makefiles)/Makefile.sim


