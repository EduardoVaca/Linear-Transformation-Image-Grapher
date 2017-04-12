"""
Author: Eduardo Vaca
Script that graph the image of any Linear Tranformation of 3*3
Project for Linear Algebra Course
"""
from random import randint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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


def generate_points(system_of_equations):
	"""Generates psceudo-random values and evaluates them in the
	sytem of equations.
	Params:
		- system_of_equations: List of lists representing the system.
	Returns:
		- List of list representing the points from values already evaluated.
	"""
	print('How many points would you wish to graph?', end=' ')
	n_points = int(input())
	print('Minimum value for a variable:', end=' ')
	min_limit = int(input())
	print('Maximun value for a variable:', end=' ')
	max_limit = int(input())

	points = [[] for _ in range(NUMBER_OF_ECUATIONS)]

	for _ in range(n_points):
		current_values = [randint(min_limit, max_limit) 
							for _ in range(NUMBER_OF_ECUATIONS)]
		result = evaluate(system_of_equations, current_values)
		
		for i in range(NUMBER_OF_ECUATIONS):
			points[i].append(result[i])

	return points
		

def graph_points(points):
	"""
	Graph the points in a 3d Scatter plot.
	Params:
		- points: List of list representing values for each variable.
	"""
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(points[0], points[1], points[2], c='r', marker='o')

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plt.show()


def main():
	equations = build_system_of_equations()
	print_system_of_equations(equations)
	points = generate_points(equations)
	graph_points(points)


if __name__ == '__main__':
	main()

