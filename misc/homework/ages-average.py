import random

def averageAge(students):
    '''
    This function takes in a dictionary of student records and returns the average age of the students.
    The dictionary contains the names of the students as keys and the values are dictionaries with the keys "age" and "standing".
    The "age" key contains the age of the student and the "standing" key contains the standing of the student.
    If the student's age is not provided, the student should not be included in the calculation of the average age.
    Use the "in" operator to check if the "age" key is in the student's record.
    students: A dictionary of student records.
    return: The average age of the students.    
    '''
    ages = []
    for key in students:
        if 'age' in students[key]:
            ages.append(students[key]['age'])
    return sum(ages)/len(ages)

def main():
    student_records = {
        "Jane": {"age": 19, "standing": "freshman"},
        "John": {"age": 20, "standing": "sophomore"},
        "Jude": {"age": 21, "standing": "junior"},
        "Janis": {"age": 22, "standing": "senior"},
        "James": {"standing": "freshman"},
        "Jared": {"age": 23, "standing": "super senior"},
    }
    result = averageAge(student_records)
    print(f"The average student age is {result}.")
    # Expected output: The average student age is 21.0.

if __name__ == '__main__':
    main()