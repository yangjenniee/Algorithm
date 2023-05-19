import sys

gradesum=0
grade=0.0
final = 0.0
for _ in range(20) :
    sheet = list(sys.stdin.readline().rstrip().split())
    gradesum += float(sheet[1])
    if sheet[2] == 'A+':
        grade += (4.5*float(sheet[1]))
    if sheet[2] == 'A0':
        grade += (4.0*float(sheet[1]))
    if sheet[2] == 'B+':
        grade += (3.5*float(sheet[1]))
    if sheet[2] == 'B0':
        grade += (3.0*float(sheet[1]))
    if sheet[2] == 'C+':
        grade += (2.5*float(sheet[1]))
    if sheet[2] == 'C0':
        grade += (2.0*float(sheet[1]))
    if sheet[2] == 'D+':
        grade += (1.5*float(sheet[1]))
    if sheet[2] == 'D0':
        grade += (1.0*float(sheet[1]))
    if sheet[2] == 'F':
        grade += (0.0*float(sheet[1]))
    if sheet[2] == 'P':
        gradesum -= float(sheet[1])

final = float(grade/gradesum)
print("%.6f"%final)
















