'''https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
#provided in the compiler
   
avg_marks = sum(student_marks[query_name])/len(scores)  #finding averages
print("{:.2f}".format(avg_marks)) #prinitng till 2 decimal places