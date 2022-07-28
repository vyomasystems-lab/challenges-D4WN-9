import cocotb
import numpy as np
from cocotb.triggers import Timer

@cocotb.test()
async def mux_exhaustive_test(dut):
	e_list = []
	input_arr = np.int32(np.zeros(31))
	input_arr[0] = 1
	for i in range(31):
		x = np.roll(input_arr, i)
		for j in range(31):
			exec('dut.inp'+str(j)+'.value='+str(x[j]))
			dut.sel.value = j
			await Timer(1, units='ns')
			dut._log.info(f'i={i:05} j={j:05} model={x[j]:05} DUT={int(dut.out.value):05}')
			try:
				assert dut.out.value == x[j], "TEST FAIL @ sel = {J}, in = {V} out = {M}".format(J=dut.sel.value, V=x[j], M=dut.out.value)
			except AssertionError as e:
				print(e)
				e_list.append(e)
	if len(e_list)==0:
		print("NO ERRORS FOUND")
	else:
		print(e_list)
		print(str(len(e_list))+' ERRORS FOUND')