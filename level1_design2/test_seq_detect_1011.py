import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

e_list=[]

@cocotb.coroutine
def cloc_proc(signal, half_period):
    signal.value = 0
    timer = Timer(half_period, "us")
    while True:
        yield timer
        signal.value = ~signal


@cocotb.test()
async def test_all_bugs(dut):
	inp_seq = '000101101100011011000101011000101110110'
	out_seq = '000000010010000000100000000100000010001'

	# cocotb.start_soon(Clock(dut.clk, 10, units="us").start())
	cocotb.start_soon(cloc_proc(dut.clk, 5))
    # yield RisingEdge(dut.clk)

	dut.reset.value = 0
	await RisingEdge(dut.clk)

	for i in range(len(inp_seq)):
		if i < 3:
			continue
		dut.inp_bit.value = int(inp_seq[i])
		# await FallingEdge(dut.clk)
		await RisingEdge(dut.clk)
		# dut._log.info(f'input={int(inp_seq[i-3: i+2]):05}')
		# dut._log.info(f'model={int(out_seq[i]):01}')
		# dut._log.info(f'DUT={int(dut.seq_seen.value):01}')
		try:
			assert dut.seq_seen.value == int(out_seq[i]), "TEST FAIL @ inp = {A}, out = {B}".format(A=dut.inp_bit.value, B=dut.seq_seen.value)
		except AssertionError as e:
			print(e)
			e_list.append(e)
	
	if len(e_list)==0:
		print("NO ERRORS FOUND")
	else:
		print(e_list)
		print(str(len(e_list))+' ERRORS FOUND')