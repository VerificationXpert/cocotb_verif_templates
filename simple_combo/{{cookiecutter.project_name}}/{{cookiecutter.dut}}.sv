// {{cookiecutter.dut}}.sv
// Author: {{cookiecutter.author}}

module {{cookiecutter.dut}} (
// Port declarations
    input logic a,
    output logic a_not

);

    assign a_not = ~a;
    // Add your code here

endmodule : {{cookiecutter.dut}}
