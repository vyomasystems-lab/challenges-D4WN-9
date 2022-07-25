import cocotb
from cocotb.triggers import Timer
import numpy as np

@cocotb.test()
async def mux_exhaustive_test(dut):
	input_arr = np.zeros(31)
	input_arr[0]=1

	for i in range(31):
		x = np.roll(input_arr, i)
		for j in range(31):
			temp = 'dut.inp' + str(j) + '.value = ' + str(int(x[j]))
			exec(temp)
			for k in range(31):
				dut.sel.value = k
				await Timer(1, units='ns')
				cocotb.log.info('##### CTB: Develop your test here ########')
				assert dut.out.value == x[k], 'TEST FAIL with sel={k}'.format(k=dut.sel.value)