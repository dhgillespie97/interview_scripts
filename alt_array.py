#Prints alternating elements in a given array

def printAl(arr,n):
	for i in range(0,n,2):
		print(arr[i])
		
if __name__ == '__main__':

	arr = [1,2,3,4,5]
	n = len(arr)
	
	printAl(arr,n)
