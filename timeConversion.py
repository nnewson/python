# https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Format is either hh:mm:ssAM or hh:mm:ssPM
    if s[-2:] == 'AM' and s[:2] == "12":
            return "00" + s[2:8]
    elif s[-2:] == 'PM' and s[:2] != "12":
        return str( int(s[:2]) + 12 ) + s[2:8]
    else:
        return s[:8]


if __name__ == '__main__':
    s = input()
    print( timeConversion(s) )
