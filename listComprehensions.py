# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Range is exclusive, so need to +1  
    # List comprehension can generate multiple variables in one line
    print( [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n ] )