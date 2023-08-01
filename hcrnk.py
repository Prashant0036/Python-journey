if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    c=0
    if query_name=="Malika":
        for i in student_marks.values():
            c+=1
            if c==3:
             print(format(((i[0]+i[1]+i[2])/3),".2f"))
    if query_name=="Harsh":
        for i in student_marks.values():
            c+=1
            if c==1:
             print(format(((i[0]+i[1]+i[2])/3),".2f"))
    
    
