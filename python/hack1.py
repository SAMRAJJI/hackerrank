def print_rangoli(size):
    alpha= 'abcdefghijklmnopqrstuvwxyz'
      # Generate the first half of the pattern
    for i in range(n):
        letters = '-'.join(alpha[n-1:n-1-i:-1] + alpha[n-1-i:n])
        print(letters.center(4*n-3, '-'))

    # Generate the second half of the pattern (mirror of the first half)
    for i in range(n-2, -1, -1):
        letters = '-'.join(alpha[n-1:n-1-i:-1] + alpha[n-1-i:n])
        print(letters.center(4*n-3, '-'))
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)