test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]
filtered_students = filter(lambda student: 50 <= student["result"] <= 70, test_results)

# Display the students
for student in filtered_students:
    print(student["name"])