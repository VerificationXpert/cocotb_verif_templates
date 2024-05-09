# test_{{cookiecutter.dut}}.py

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles,RisingEdge

import os
import random
from pathlib import Path

async def reset(dut) -> None:
    resetValue:bool = False
    dut.{{cookiecutter.reset_name}}.setimmediatevalue(resetValue)
    await ClockCycles(dut.{{cookiecutter.clock_name}},10)
    dut.{{cookiecutter.reset_name}}.value = not resetValue

@cocotb.test()
async def hello_{{cookiecutter.dut}}_test(dut) -> None:
    cocotb.start_soon(Clock(dut.{{cookiecutter.clock_name}},10,units="ns").start())
    cocotb.start_soon(reset(dut))
    await ClockCycles(dut.{{cookiecutter.clock_name}},10)
    
    await RisingEdge(dut.{{cookiecutter.reset_name}})
    assert 1==1

from cocotb.runner import get_runner

def test_{{cookiecutter.dut}}_runner() -> None:
    hdl_toplevel_lang:str = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim:str = os.getenv("SIM", "{{cookiecutter.simulator}}")

    precision:str = os.getenv("TIMESCALE_PRECISION", "ps")

    timescale = (f"1{precision}", f"1{precision}")

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
        timescale=timescale,
    )

    runner.test(hdl_toplevel="{{cookiecutter.dut}}", test_module="test_{{cookiecutter.dut}},",testcase=testcase)


if __name__ == "__main__":
    test_{{cookiecutter.dut}}_runner()