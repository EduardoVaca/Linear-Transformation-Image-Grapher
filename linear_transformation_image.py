"""
Author: Eduardo Vaca
"""


def build_ecuations_system():
	"""Buids the ecuations system by user input.
	The system is represented by a list of lists
	This is only for 3 * 3 matrix (ecuations/variables)
	"""
	ecuations = variables = 3
	variable_names = ['x', 'y', 'z']
	ecuations_system = [[] for _ in range(ecuations)]	

	for i in range(ecuations):
		print('Ecuation {}:'.format(i + 1))
		for j in range(variables):
			print('Value for variable {}{}: '.format(variable_names[j], i + 1), end='')
			ecuations_system[i].append(int(input()))

	return ecuations_system



def main():
	ecuations = build_ecuations_system()
	print(ecuations)

if __name__ == '__main__':
	main()

