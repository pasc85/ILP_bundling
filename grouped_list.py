import sys

# read in arguments and open the corresponding files
tutorials = str(sys.argv[1])
names = str(sys.argv[2])
tuts = open(tutorials, 'r')
naml = open(names, 'r')

# generate list of tutors
tutors = []
for line in tuts:
    if line.startswith('Staff allocation:'):
        t = line.split(':')[1]
        t = t.strip()
        t = t.rstrip(';')
        tutors.append(t)
tutors = list(set(tutors))
tuts.close()

# generate list of students with ILPs
students = []
for line in naml:
    s = line.upper().split(',')
    students.append([s[0], s[1].strip(), s[2].strip()])
naml.close()

# for each tutor, print list of students with ILPs
tuts = open(tutorials, 'r')
for t in tutors:
    # print: TUTOR NAME:
    tn = t.split(',')
    print(tn[0]+tn[1]+':')
    # go through tutorials, print all students with ILPs for the current tutor
    check = 0
    for line in tuts:
        if line.startswith('Staff allocation:'):
            if t in line:
                check = 1
            else:
                check = 0
        else:
            if check:
                for k in range(len(students)):
                    b = students[k][0] in line
                    b = b and students[k][1] in line
                    b = b and students[k][2] in line
                    if b:
                        s = students[k]
                        print(s[0]+', '+s[1]+', '+s[2])
    print('\n')
    tuts.seek(0)
tuts.close()
