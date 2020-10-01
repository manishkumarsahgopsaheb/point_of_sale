# a list of students who can't graduate has been set
# user enters student names
# return students whoa are eligible to graduate now

black_list = ['jadu', 'imam', 'bhaala', 'kudan', 'heman']
num_students = int(input('Enter the number of students: '))

student_list = []
white_list = []

for students in range(num_students):
    prompt = input('input a name')
    while prompt == '':
        prompt = input('Input a non-empty name')
    student_list.append(prompt)


for students in student_list:
    if students not in black_list:
        white_list.append(students)


print(f'These {len(white_list)} students are allowed to graduate.')

# print(*white_list)
# print(*white_list, sep='\n')

print(*sorted(white_list), sep='\n')


