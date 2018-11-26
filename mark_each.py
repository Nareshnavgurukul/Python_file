# ==========give marks to each name
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]

#print len(students)
# print len(marks)
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
    print students[counter],marks[counter]
    counter+=1