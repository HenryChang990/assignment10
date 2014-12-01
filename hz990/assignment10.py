from Questions import Q1, Q2, Q3, Q4, Q5, Q6

def main():
	'''This main function consists of six parts, each part answers the corresponding question.

	'''
	# Question 1
	raw_data = Q1.Run()

	# Question 2
	data = Q2.Run(raw_data)

	# Question 3
	Q3.Run()

	# Question 4
	Q4.Run(data)

	# Question 5
	Q5.Run(data)

	# Question 6
	Q6.Run(data)

if __name__ == '__main__':
	main()