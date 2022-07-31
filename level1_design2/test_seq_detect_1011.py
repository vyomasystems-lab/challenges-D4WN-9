import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

e_list=[]

@cocotb.test()
async def test_all_bugs(dut):
	clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
	cocotb.start_soon(clock.start())        # Start the clock
	dut.reset.value = 0
	await RisingEdge(dut.clk)

	inp_seq = '000101101100011011000101011000101110110'
	out_seq = '000000010010000000100000000100000010001'

	for i in range(len(inp_seq)):
		if i < 3:
			continue
		dut.inp_bit.value = int(inp_seq[i])
		await RisingEdge(dut.clk)
		dut._log.info(f'input={int(inp_seq[i-3: i+1]):04}')
		dut._log.info(f'expected_output={int(out_seq[i]):01}')
		dut._log.info(f'actual_output={int(dut.seq_seen.value):01}')
		try:
			assert dut.seq_seen.value == out_seq[i], "TEST FAIL @ inp = {A}, out = {B}".format(A=dut.inp_bit.value, B=dut.seq_seen.value)
		except AssertionError as e:
			print(e)
			e_list.append(e)
	
	if len(e_list)==0:
		print("NO ERRORS FOUND")
	else:
		print(e_list)
		print(str(len(e_list))+' ERRORS FOUND')