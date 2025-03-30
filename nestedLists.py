# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    studentScore = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        studentScore.append( [name, score] )
       
    studentScore.sort(key=lambda x: x[1]) # Sort by the second element (score)
        
    # find the second lowest score
    secondLowest = studentScore[0][1] # Initialise with lowest score
    for student in studentScore:
        if student[1] > secondLowest:
            secondLowest = student[1]
            break

    # Generate a new list with the second lowest score (name only) and sort alphabectically
    lowestStudents = [student[0] for student in filter( lambda x: x[1] == secondLowest, studentScore )]
    lowestStudents.sort()

    print( *lowestStudents, sep='\n' ) 