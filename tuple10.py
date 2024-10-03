//
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
//
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
my_tuple = tuple(map(int, input().split()))
x = int(input())
count = my_tuple.count(x)
factorial = calculate_factorial(count)
print(factorial)
