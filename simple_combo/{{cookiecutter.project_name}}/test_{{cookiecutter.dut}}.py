# test_{{cookiecutter.dut}}.py

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles,RisingEdge,Timer
from cocotb.types import LogicArray,Logic

import os
import random
from pathlib import Path

@cocotb.test()
async def hello_{{cookiecutter.dut}}_test(dut) -> None:
    
    # Assert Initial output is unknown
    assert LogicArray(dut.a_not.value) == LogicArray("X")

    Timer(10,'ps')

    dut.a.value = 1

    Timer(10,'ps')

    assert dut.a.not.value == 0

from cocotb.runner import get_runner

def test_{{cookiecutter.dut}}_runner() -> None:
    hdl_toplevel_lang:str = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim:str = os.getenv("SIM", "{{cookiecutter.simulator}}")
    testcase:str = os.getenv("testcase", "")

    proj_path:Path = Path(__file__).resolve().parent

    verilog_sources = []
    vhdl_sources = []

    verilog_sources = [proj_path / "{{cookiecutter.dut}}.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        vhdl_sources=vhdl_sources,
        hdl_toplevel="{{cookiecutter.dut}}",
        always=True,
    )

    runner.test(hdl_toplevel="{{cookiecutter.dut}}", test_module="test_{{cookiecutter.dut}},",testcase=testcase)


if __name__ == "__main__":
    test_{{cookiecutter.dut}}_runner()