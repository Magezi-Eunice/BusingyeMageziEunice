def student_info():
    print("Please input the following information: ")
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    studentNum = input("Student number: ")

    data = f"""

            -------Your Student Data-------
                Name: {name}
                Age: {age}
                Course: {course}
                Student Number: {studentNum}

            """

    print(data)

student_info()
