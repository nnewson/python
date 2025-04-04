# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

from functools import reduce

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    print( "{:0.6f}".format( reduce( lambda posOccurences, num : posOccurences + 1 if num > 0 else posOccurences, arr, 0 ) / len( arr ) ) )
    print( "{:0.6f}".format( reduce( lambda negOccurences, num : negOccurences + 1 if num < 0 else negOccurences, arr, 0 ) / len( arr ) ) )
    print( "{:0.6f}".format( reduce( lambda zeroOccurences, num : zeroOccurences + 1 if num == 0 else zeroOccurences, arr, 0 ) / len( arr ) ) )

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)