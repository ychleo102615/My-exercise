def main():

	height_input = int(input('please enter height: '))
	style = input('please enter ideal character: ')
	pt_pyrimid(height_input, style)

def pt_pyrimid(height_input, symbol):  #print pyrimid

	for height in range(1, height_input+1):
		anti_height = height_input-height  #space number
		#print(' ', end = '')
		print (' '*anti_height + symbol*height + '  ' + symbol*height)


if __name__ == '__main__':
	main()

""" python2 and python3 differ at: 

	#input	
	input-->int 		|	input-->str
	raw_input-->str		|

	#print
	no need of print()	|	print()
					^^	|	can use end=''
"""