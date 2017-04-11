"""
Author: Eduardo Vaca
"""
from random import randint

NUMBER_OF_ECUATIONS = 3
VARIABLE_NAMES = ['x', 'y', 'z']

def build_system_of_equations():
	"""Buids the equations system by user input.
	The system is represented by a list of lists
	This is only for 3 * 3 matrix (equations/variables)
	"""
	equations = variables = NUMBER_OF_ECUATIONS	
	system_of_equations = [[] for _ in range(equations)]	

	for i in range(equations):
		print('Equation {}:'.format(i + 1))
		for j in range(variables):
			print('Value for variable {}{}: '.format(VARIABLE_NAMES[j], i + 1), end='')
			system_of_equations[i].append(int(input()))

	return system_of_equations


def print_system_of_equations(system_of_equations):
	"""Prints the system of equations in formal way.
	Params:
		- system_of_equations: List of lists representing the system.
	"""
	print('\nYour System of Equations:')
	for equation in system_of_equations:
		print('|', end=' ')
		for i in range(len(equation)):
			print('\t{}{}'.format(equation[i], VARIABLE_NAMES[i]), end=' ')
		print('\t|')

def evaluate(system_of_equations, values):
	"""Evaluates a list of values in the system of equations.
	Params:
		- system_of_equations: List of lists representing the system.
		- values: List of values to be evaluated.
	"""
	result = [0] * NUMBER_OF_ECUATIONS
	for i in range(len(system_of_equations)):
		value = 0
		for j in range(len(values)):
			value += values[j]*system_of_equations[i][j]
		result[i] = value
	return result


def generate_points_in_graph(system_of_equations):
	"""Generates psceudo-random values and use them as values
	for the system of equations.
	Params:
		- system_of_equations: List of lists representing the system.
	"""
	print('How many points would you wish to graph?', end=' ')
	n_points = int(input())
	print('Minimum value for a variable:', end=' ')
	min_limit = int(input())
	print('Maximun value for a variable:', end=' ')
	max_limit = int(input())

	for _ in range(n_points):
		current_values = [randint(min_limit, max_limit) 
							for _ in range(NUMBER_OF_ECUATIONS)]
		print('CURRENT VALUES: {}'.format(current_values))
		print('RESULT: {}'.format(evaluate(system_of_equations, current_values)))



def main():
	equations = build_system_of_equations()
	print_system_of_equations(equations)
	generate_points_in_graph(equations)

if __name__ == '__main__':
	main()

