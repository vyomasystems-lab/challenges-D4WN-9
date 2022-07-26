import cocotb
import numpy as np
from cocotb.triggers import Timer

@cocotb.test()
async def mux_exhaustive_test(dut):
	input_arr = np.int(np.zeros(31))
	# input_arr = [0] * 30
	input_arr[0] = 1

	for i in range(31):
		x = np.roll(input_arr, i)
		for j in range(31):
			temp = 'dut.inp'+str(j)+'.value='+str(x[j])
			exec(temp)
			for k in range(31):
				dut.sel.value = k
				await Timer(1, units='ns')
				cocotb.log.info(f'i={i:05} j={j:05} model={x[k]:05} DUT={int(dut.out.value):05}')
				assert dut.out.value == x[k], 'TEST FAIL with sel={k}'.format(k = dut.sel.value)