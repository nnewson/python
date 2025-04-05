# https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

from functools import reduce

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum = reduce( lambda sum, x: sum + x, arr, 0 )
    print( str( sum - reduce( lambda max, x: x if x > max else max, arr, arr[0] ) ) + " " + str( sum - reduce( lambda min, x: x if x < min else min, arr, arr[0] ) ) )

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)