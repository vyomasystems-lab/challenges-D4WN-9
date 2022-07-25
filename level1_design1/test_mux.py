# # See LICENSE.vyoma for details

# import cocotb
# from cocotb.triggers import Timer
import numpy as np
# @cocotb.test()
# async def test_mux(dut):
#     """Test for mux2"""

input_arr = np.zeros(31)
input_arr[0]=1

for i in range(31):
    x = np.roll(input_arr, i)
    for j in range(31):
        temp = 'dut.inp' + str(j) + '.value = ' + str(int(x[j]))
        print(temp)
        for k in range(31):
            dut.sel.value = k
            assert dut.out.value == x[k]

    # cocotb.log.info('##### CTB: Develop your test here ########')
