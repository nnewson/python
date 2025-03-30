# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

def listLoop():
    N = int(input())

    list = []

    for x in range(N):
        args = [x for x in input().split()]
        match args[0]:
            case "print": 
                print(list)
            case "append":
                list.append(int(args[1]))
            case "pop":
                list.pop()
            case "sort":
                list.sort()
            case "reverse":
                list.reverse()
            case "insert":
                list.insert(int(args[1]), int(args[2]))
            case "remove":
                list.remove(int(args[1]))

# Via ChatGPT
def test_listLoop():
    from io import StringIO
    import sys

    # Capture output
    input_data = """12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print"""
    
    expected_output = """[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

    # Redirect stdin and stdout
    stdin_backup = sys.stdin
    stdout_backup = sys.stdout
    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()

    # Call the function (you should implement listLoop to read from stdin)
    listLoop()  # assuming this is implemented to handle input()

    output = sys.stdout.getvalue()

    # Restore stdin and stdout
    sys.stdin = stdin_backup
    sys.stdout = stdout_backup

    # Test result
    assert output == expected_output, f"Expected:\n{expected_output}\nGot:\n{output}"

if __name__ == '__main__':
    test_listLoop()