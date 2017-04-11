"""
Author: Eduardo Vaca
"""


def build_system_of_equations():
	"""Buids the equations system by user input.
	The system is represented by a list of lists
	This is only for 3 * 3 matrix (equations/variables)
	"""
	equations = variables = 3
	variable_names = ['x', 'y', 'z']
	system_of_equations = [[] for _ in range(equations)]	

	for i in range(equations):
		print('Equation {}:'.format(i + 1))
		for j in range(variables):
			print('Value for variable {}{}: '.format(variable_names[j], i + 1), end='')
			system_of_equations[i].append(int(input()))

	return system_of_equations



def main():
	equations = build_system_of_equations()
	print(equations)

if __name__ == '__main__':
	main()

