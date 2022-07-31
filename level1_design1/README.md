# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Gitpod ID is shown in bottom left of screenshot below. I have used VS Code to SSH into Gitpod environment*

<img src="/level1_design1/gitpod_id.png" alt="Alt text" title="Optional title">

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (multiplexer module) which takes in 31 2-bit inputs and a 5 bit select input which selects one of the inputs to transfer to the output.

## Test Despcription

The values are assigned to the input port using a two nested for loops. It is an exhaustive test which drives input in all possible combinations.

The assert statement is used for comparing the multiplexer's output to the expected value. The assert statement is inside of a try block, this ensures the exhaustiveness of test as execution of code keeps on happening until all input combinations are driven without TEST failing. The bug is captured through printing the assertion statements that are saved in a list data structure inside the except block.

The following assertion errors are reflected in terminal:
```
TEST FAIL @ sel = 01100, in = 1, out = 00
TEST FAIL @ sel = 01101, in = 0, out = 01
TEST FAIL @ sel = 01101, in = 1, out = 00
TEST FAIL @ sel = 11110, in = 1, out = 00
```

## Design Bug
Based on the above test input and analysing the design, we see the following

```
5'b01011: out = inp11;
5'b01101: out = inp12;
5'b01101: out = inp13;
```
the correct logic should have ``5'b01100`` input address (select bits) for driving ``inp12`` to ``out``

and also

```
5'b11101: out = inp29;
default: out = 0;
```

the correct logic should have ``5'b11110`` input address (select bits) which is missing enirely, for driving ``inp30`` to ``out``

## Design Fix
Updating the design and re-running the test makes the test pass.

<img src="/level1_design1/design_fix_mux.png" alt="Alt text" title="Optional title">

The updated design is checked in as fixed_mux.v

## Verification Strategy

Exhaustive test was implemented as all input combinations need to be driven to the mux to get the required output. No change in input driven was applied, i.e. ``01`` input was driven in all combinations the value of input doesn't affect the output as much as the input combination.

### Numpy Library - Python

A numpy array is initialised using ``numpy.zeros`` and the first element is set to ``1``. This is used as the first input combination to be driven to the multiplexer. On each iteration ``numpy.roll`` is used to displace the ``1`` value to a new unique position. This creates a unique input combination for all iterations. Hence exhaustive test is achieved while minimising number of lines in code. 

## Is the verification complete ?

Verification stands complete as all test cases have driven to buggy design and output has been observed. Moreover the buggy design has been fixed and all test cases give expected output.
