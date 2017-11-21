import sys

class Brainfuck:

	cells = [0] * 30000
	pointer = 0
	program = input().strip()
	test = list(program)
	abre = 0
	auxLoop = []
	for i in test:
		if i == '[':
			abre += 1
		elif i == ']':
			abre -= 1	
	if abre != 0:
		raise SyntaxError('Malformed expression')
		
	pc = 0
	mark = 0
	while pc < len(program):
		# current operation
		op = program[pc]

		if op == '+':
			cells[pointer] += 1
		elif op == '-':
			cells[pointer] -= 1
		elif op == '>':
			pointer += 1
		elif op == '<':
			pointer -= 1
		elif op == '.':
			print(chr(cells[pointer]),end="")
		elif op == ',':
			aux = input()
			cells[pointer] = ord(aux[0])
			
		elif op == "[":
			if cells[pointer] != 0:
				if pc not in auxLoop:
					auxLoop.append(pc)
		elif op == "]":
			if cells[pointer] != 0:
				pc = auxLoop[-1] - 1
			else:
				auxLoop.pop(-1)
		if cells[pointer] > 255:
			cells[pointer] -= 256
		elif cells[pointer] < 0:
			cells[pointer] = 256 - cells[pointer]
		if pointer < 0 or pointer > 29999:
			raise MemoryError('Out of range')
		pc += 1
	print()
