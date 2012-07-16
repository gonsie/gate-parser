# Encapsulation of lexer/parser pair
class PLYPair:
	def __init__(self, l=None, p=None):
		self.lexer = l
		self.parser = p

	def set_lexer(self, l):
		self.lexer = l

	def set_parser(self, p):
		self.parser = p

	def parse(self, fname):
		f = open(fname, 'r')
		a = f.read()
		f.close()

		return self.parser.parse(a, lexer=self.lexer)

import ply_verilog_netlist
import ply_liberty

if __name__ == "__main__":
	print "\n*** Liberty Parser"
	l = PLYPair()
	l.set_lexer(ply_liberty.create_lexer())
	l.set_parser(ply_liberty.create_parser())
	l.parse('Examples/example_library.lib')

	print "\n*** Verilog Netlist Parser"
	vn = PLYPair()
	vn.set_lexer(ply_verilog_netlist.create_lexer({'and':'CELL','or':'CELL'}))
	vn.set_parser(ply_verilog_netlist.create_parser())
	vn.parse('Examples/example_netlist.v')

