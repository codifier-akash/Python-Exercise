def getdate():
    import datetime
    return datetime.datetime.now()

date_time = getdate()

def first_question():
    print("\nChoose person\n\n1 - Harry\n2 - Rohan\n3 - Hammad")

def second_question():
    print("\nChoose subject\n\n1 - Diet\n2 - Exercise")

def third_question():
    print("\nChoose your work\n\n1 - Lock\n2 - Retrive")

print("Health Management System | Developed by Codifier Akash")
first_question()
person_input = str(input("Enter number for person : "))
if person_input == '1':
    second_question()
    subject_input = str(input("Enter number for subject : "))
    if subject_input == '1':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input = str(input("Enter food what you want to lock : "))
            with open("./diet/Harry.txt", "a") as file1:
                file1.write(f"[{date_time}] - {data_input}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./diet/Harry.txt") as file2:
                data2 = file2.read()
                print(data2)
    elif subject_input == '2':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input2 = str(input("Enter exercise what you want to lock : "))
            with open("./exercise/Harry.txt", "a") as file3:
                file3.write(f"[{date_time}] - {data_input2}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./exercise/Harry.txt") as file4:
                data4 = file4.read()
                print(data4)
elif person_input == '2':
    second_question()
    subject_input = str(input("Enter number for subject : "))
    if subject_input == '1':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input3 = str(input("Enter food what you want to lock : "))
            with open("./diet/Rohan.txt", "a") as file5:
                file5.write(f"[{date_time}] - {data_input3}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./diet/Rohan.txt") as file6:
                data6 = file6.read()
                print(data6)
    elif subject_input == '2':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input4 = str(input("Enter exercise what you want to lock : "))
            with open("./exercise/Rohan.txt", "a") as file7:
                file7.write(f"[{date_time}] - {data_input4}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./exercise/Rohan.txt") as file8:
                data8 = file8.read()
                print(data8)
elif person_input == '3':
    second_question()
    subject_input = str(input("Enter number for subject : "))
    if subject_input == '1':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input5 = str(input("Enter food what you want to lock : "))
            with open("./diet/Rohan.txt", "a") as file9:
                file9.write(f"[{date_time}] - {data_input5}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./diet/Rohan.txt") as file10:
                data10 = file10.read()
                print(data10)
    elif subject_input == '2':
        third_question()
        work_input = str(input("Enter number for work : "))
        if work_input == '1':
            data_input6 = str(input("Enter exercise what you want to lock : "))
            with open("./exercise/Rohan.txt", "a") as file11:
                file11.write(f"[{date_time}] - {data_input6}\n")
                print("Data entered successfully")
        elif work_input == '2':
            with open("./exercise/Rohan.txt") as file12:
                data12 = file12.read()
                print(data12)