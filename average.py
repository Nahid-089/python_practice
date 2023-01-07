'''
marks = [45, 60, 75, 98]
percentage = (sum(marks)/400 )*100

marks2 = [48, 60, 65, 88]
percentage2 = (sum(marks2)/400 )*100
print(percentage,percentage2)
'''

def percent(marks) :
    p=((marks[0] + marks[1] + marks[2] + marks[3])/400 )*100
    return p

marks1 = [45, 75, 88, 94]
percentage1 = percent(marks1)

marks2 = [46, 75, 88, 94]
percentage2 = percent(marks2)

print(percentage1,percentage2)


