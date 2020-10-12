#Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
#Split an array into two equal Sum subarrays
#divide an array into two subarrays so that sum of elements in both are same
# Python3 program to split an array into Two
# equal sum subarrays

# Returns split point. If not possible, then
# return -1.
def findSplitPoint(arr, n):
    leftSum = 0

    # traverse array element
    for i in range(0, n):

        # add current element to left Sum
        leftSum += arr[i]

        # find sum of rest array elements (rightSum)
        rightSum = 0
        for j in range(i + 1, n):
            rightSum += arr[j]

        # split poindex
        if (leftSum == rightSum):
            return i + 1

    # if it is not possible to split array into
    # two parts
    return -1


# Prints two parts after finding split pousing
# findSplitPoint()
def printTwoParts(arr, n):
    splitPo = findSplitPoint(arr, n)

    if (splitPo == -1 or splitPo == n):
        print("Not Possible")
        return

    for i in range(0, n):
        if (splitPo == i):
            print("")
        print(str(arr[i]) + ' ', end='')

    # driver program


arr = [1, 2, 3, 4, 5, 5]
n = len(arr)
printTwoParts(arr, n)

# This code is contributed by Manish Shaw
# (manishshaw1)

#Example 2
# Partition the list into two sublists with the same sum
def partition(A):

	# do for each element of the list
	for i in range(len(A)):
		left_sum = 0
		for j in range(i):
			left_sum += A[j]

		right_sum = 0
		for j in range(i, len(A)):
			right_sum += A[j]

		# if sum of A[0..i-1] is equal to A[i, n-1]
		if left_sum == right_sum:
			return i

	# invalid input
	return -1


if __name__ == '__main__':

	A = 6, -4, -3, 2, 3

	# get index i that points to starting of second sublist
	i = partition(A)

	if i != -1:
		print(A[:i])		# print the first sublist [0, i-1]
		print(A[i:])		# print the second sublist [i, n-1]
	else:
		print("The list can't be partitioned")

#example 2

