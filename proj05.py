################################################################################
#
# Computer Project 05
#
# Description:
#    This Python script is designed to display a menu of options that
#    perform tasks for example:
#    1. Giving the maximum grade a student received on a subject
#    2. Giving the average grade a student received
#    3. Giving information on a particular student
#    4. Giving the student name and grade of the highest average grade achieved.
#
#  Here are some of the following tasks the program does:
#    - Takes the files the user gave and combines them into a huge list
#    - Uses the list to perform tasks as described in the menu.
################################################################################
# Write all your function definitions before the main
def open_file(input_file):
    '''
    - takes the user_input
    - checks if the file exists
    '''
    error = "Error. File does not exist"
    count = 0
    while error != "":
        try:
            file = open(input_file, "r")
            error = ""
            file.close()
            return input_file
        except FileNotFoundError:
            print(error)
            if "english" in input_file or "English" in input_file or count == 1:
                input_file = input("\n:~Enter a English grade score file ~:")
            elif "names" in input_file or "Name" in input_file or "name" in input_file or count == 0:
                input_file = input("\n:~Enter a student names score file ~:")
            elif "math" in input_file or "Math" in input_file or count == 2:
                input_file = input("\n:~Enter a Math grade score file ~:")
            elif "science" in input_file or "Science" in input_file or count == 3:
                input_file = input("\n:~Enter a Science grade score file ~:")
            else:
                input_file = input(":~Enter a file name ~:")
        count += 1

def create_lists(file_name):
    """
    Takes the file name
    creates a list from the file
    """
    final_list = list()
    names_list = list()
    file_obj = open(file_name, 'r')
    for line in file_obj:
        count = 0
        line = line.strip()
        if line:
            if line.find(",") != -1:
                my_list = line.split(",")
                for i in my_list:
                    if i == "":
                        my_list[count] = 0
                    else:
                        my_list[count] = int(i)
                    count += 1
                final_list.append(my_list)
            else:
                names_list.append(line)
    if (len(names_list) != 0):
        final_list.append(names_list)
    return final_list

def choice_one(final_list):
    """
    - Takes a student's name as input
    - returns the student's highest grade score along with the subject.
    """
    user_input = input(":~Enter a person name ~:")
    while user_input not in final_list[0][0]:
        print("Invalid name or does not exist")
        user_input = input(":~Enter a person name ~:")

    #Final lists
    index_of_name = final_list[0][0].index(user_input)
    english_list = final_list[1][index_of_name]
    math_list = final_list[2][index_of_name]
    science_list = final_list[3][index_of_name]

    #Final Score
    english_score = sum(english_list)
    math_score = sum(math_list)
    science_score = sum(science_list)

    if english_score > math_score and english_score > science_score:
        print("--------------")
        print(f"Highest grade score: {english_score}")
        print("Subject name: English")
    elif math_score > english_score and math_score > science_score:
        print("--------------")
        print(f"Highest grade score: {math_score}")
        print("Subject name: Math")
    elif science_score > english_score and science_score > math_score:
        print("--------------")
        print(f"Highest grade score: {science_score}")
        print("Subject name: Science")
    elif english_score > math_score and english_score == science_score:
        print("--------------")
        print(f"Highest grade score: {english_score}")
        print("Subject name: English Science")
    elif english_score > science_score and english_score == math_score:
        print("--------------")
        print(f"Highest grade score: {english_score}")
        print("Subject name: English Math")
    elif math_score > english_score and math_score == science_score:
        print("--------------")
        print (f"Highest grade score: {math_score}")
        print("Subject name: Math Science")

def choice_two(final_list):
    """
    - Takes a student's name as input
    - returns the student's grades in all subjects.
    """
    user_input = input(":~Enter a person name ~:")
    while user_input not in final_list[0][0]:
        print("Invalid name or does not exist")
        user_input = input(":~Enter a person name ~:")

    # Final lists
    index_of_name = final_list[0][0].index(user_input)
    english_list = final_list[1][index_of_name]
    math_list = final_list[2][index_of_name]
    science_list = final_list[3][index_of_name]

    # Final Score
    english_score = sum(english_list)
    math_score = sum(math_list)
    science_score = sum(science_list)
    full_score = (english_score + math_score + science_score)/3
    full_score = round(full_score, 1)
    print("--------------")
    print(f"Average grade score: {full_score}")

def choice_three(final_list):
    user_input = input(":~Enter a person name ~:")
    while user_input not in final_list[0][0]:
        print("Invalid name or does not exist")
        user_input = input(":~Enter a person name ~:")
    index_of_name = final_list[0][0].index(user_input)
    english_list = final_list[1][index_of_name]
    math_list = final_list[2][index_of_name]
    science_list = final_list[3][index_of_name]
    # Final Score
    english_score = sum(english_list)
    math_score = sum(math_list)
    science_score = sum(science_list)
    #English
    speaking = english_list[0]
    writing = english_list[1]
    reading = english_list[2]
    listening = english_list[3]
    #Math
    geometry = math_list[0]
    arithmetic = math_list[1]
    logic = math_list[2]
    #Science
    biology = science_list[0]
    chemistry = science_list[1]
    physics = science_list[2]

    print("--------------")
    print(f"English: {english_score}\nSpeaking: {speaking} Writing: {writing} Reading: {reading} Listening: {listening}")
    print("--------------")
    print(f"Math: {math_score}\nGeometry: {geometry} Arithmetic: {arithmetic} Logic: {logic}")
    print("--------------")
    print(f"Science: {science_score}\nBiology: {biology} Chemistry: {chemistry} Physics: {physics}")

def choice_four(final_list):
    """
    - user inputs subject name
    - gives the average grade score in the subject
    """
    max = 0
    average = 0
    count = 0
    final_sum = 0
    subject_list = ["English", "Math", "Science"]
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    user_input = input(":~Enter a subject name ~:")
    while user_input not in subject_list:
        print("Invalid name or does not exist")
        user_input = input(":~Enter a subject name ~:")

    if user_input == "English":
        for i in final_list[0][0]:
            english_list = final_list[1][count]
            final_sum += sum(english_list)
            count+= 1
        average = final_sum/count
        average = round(average, 1)
        print("--------------")
        print(f"Average grade score: {average}")
    elif user_input == "Math":
        for i in final_list[0][0]:
            math_list = final_list[2][count]
            final_sum += sum(math_list)
            count += 1
        average = final_sum / count
        average = round(average, 1)
        print("--------------")
        print(f"Average grade score: {average}")
    elif user_input == "Science":
        for i in final_list[0][0]:
            science_list = final_list[3][count]
            final_sum += sum(science_list)
            count += 1
        average = final_sum / count
        average = round(average, 1)
        print("--------------")
        print(f"Average grade score: {average}")

def choice_five(final_list):
    """
    - user inputs grade threshold
    - code returns the number of students who passed grade threshold
    """
    count = 0
    num_students_passed = 0
    user_input = input(":~Enter a grade threshold ~:")
    while int(user_input) < 0 or int(user_input) > 100 or user_input.isdigit() == False:
        print("Invalid grade score")
        user_input = input(":~Enter a grade threshold ~:")
    for i in final_list[0][0]:
        english_list = final_list[1][count]
        math_list = final_list[2][count]
        science_list = final_list[3][count]
        english_sum = sum(english_list)
        math_sum = sum(math_list)
        science_sum = sum(science_list)
        average = (english_sum + math_sum + science_sum)/3
        if average > int(user_input):
            num_students_passed += 1
        count += 1
    print("--------------")
    print(f"The number of students having average grade score higher than {int(user_input)} is: {num_students_passed}")

def choice_six(final_list):
    """
    - function takes a list as a parameter
    - function returns student name and the highest average grade score
    """
    count = 0
    max_average = -5
    max_index = 0
    for i in final_list[0][0]:
        english_list = final_list[1][count]
        math_list = final_list[2][count]
        science_list = final_list[3][count]
        final_english_score = sum(english_list)
        final_math_score = sum(math_list)
        final_science_score = sum(science_list)
        names = final_list[0][0]
        average = (final_english_score + final_math_score + final_science_score)/3
        average = round(average,2)
        if average > max_average:
            max_average = average
            max_index = count
        elif average == max_average and count > 0:
            #English
            past_english_list = final_list[1][count - 1]
            final_past_english_score = sum(past_english_list)
            past_english_average = final_past_english_score/4
            past_english_average = round(past_english_average,1)
            this_english_average = final_english_score/4
            this_english_average = round(this_english_average, 1)
            #Math
            past_math_list = final_list[2][count - 1]
            final_past_math_score = sum(past_math_list)
            past_math_average = final_past_math_score / 3
            past_math_average = round(past_math_average,1)
            this_math_average = final_math_score / 3
            this_math_average = round(this_math_average, 1)
            #Science
            past_science_list = final_list[3][count - 1]
            final_past_science_score = sum(past_science_list)
            past_science_average = final_past_science_score / 3
            past_science_average = round(past_science_average,1)
            this_science_average = final_science_score / 3
            this_science_average = round(this_science_average,1)
            if this_english_average > past_english_average:
                max_average = average
                max_index = count
            elif this_math_average > past_math_average:
                max_average = average
                max_index = count
            elif this_science_average > past_science_average:
                max_average = this_science_average
                max_index = count
        count += 1
        max_average = round(max_average,1)
    print("--------------")
    print(f"Name: {names[max_index]}\nAverage grade score: {max_average}")


def choice_seven(final_list):
    """
    - user inputs a subject name
    - function returns the student with the highest grade score in that subject
    """
    count = 0
    max_index = 0
    max_score = -5
    subject_list = ["English", "Math", "Science"]
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    user_input = input(":~Enter a subject name ~:")
    while user_input not in subject_list:
        print("Invalid name or does not exist")
        user_input = input(":~Enter a subject name ~:")
    for i in final_list[0][0]:
        english_list = final_list[1][count]
        math_list = final_list[2][count]
        science_list = final_list[3][count]
        if user_input == "English":
            english_sum = sum(english_list)
            if english_sum > max_score:
                max_score = english_sum
                max_index = count
            elif english_sum == max_score and count > 0:
                past_english_list = final_list[1][max_index]
                if english_list[0] > past_english_list[0]:
                    max_score = english_sum
                    max_index = count
                elif english_list[1] > past_english_list[1]:
                    max_score = english_sum
                    max_index = count
                elif english_list[2] > past_english_list[2]:
                    max_score = english_sum
                    max_index = count
                elif english_list[3] > past_english_list[3]:
                    max_score = english_sum
                    max_index = count
        elif user_input == "Math":
            math_sum = sum(math_list)
            if math_sum > max_score:
                max_score = math_sum
                max_index = count
            elif math_sum == max_score and count > 0:
                past_math_list = final_list[2][max_index]
                if math_list[0] > past_math_list[0]:
                    max_score = math_sum
                    max_index = count
                elif math_list[1] > past_math_list[1]:
                    max_score = math_sum
                    max_index = count
                elif math_list[2] > past_math_list[2]:
                    max_score = math_sum
                    max_index = count
        elif user_input == "Science":
            science_sum = sum(math_list)
            if science_sum > max_score:
                max_score = science_sum
                max_index = count
            elif science_sum == max_score and count > 0:
                past_science_list = final_list[3][max_index]
                if science_list[0] > past_science_list[0]:
                    max_score = science_sum
                    max_index = count
                elif science_list[1] > past_science_list[1]:
                    max_score = science_sum
                    max_index = count
                elif science_list[2] > past_science_list[2]:
                    max_score = science_sum
                    max_index = count
        count += 1
    names = final_list[0][0]
    user_name = names[max_index]
    print("--------------")
    print(f"Name: {user_name}\nGrade score: {max_score}")





def main():
    menu = '''
        Menu : 
            1: The maximum grade a student received in a single subject
            2: The average subject grade a student received
            3: Individual information
            4: The average grade of a subject over all students
            5: The number of students with an average grade exceeding given threshold X
            6: The name of student having the highest average grade
            7: The name of student having the highest grade of given subject name
                Enter any other key(s) to exit
    '''

    #storing lists
    master_list = list()
    variable = input("\n:~Enter a student names file ~:")
    new_input = open_file(variable)
    list_one = create_lists(new_input)
    variable_two = input("\n:~Enter a English grade score file ~:")
    new_input_two = open_file(variable_two)
    list_two = create_lists(new_input_two)
    variable_three = input("\n:~Enter a Math grade score file ~:")
    new_input_three = open_file(variable_three)
    list_three = create_lists(new_input_three)
    variable_four = input("\n:~Enter a Science grade score file ~:")
    new_input_four = open_file(variable_four)
    list_four = create_lists(new_input_four)

    #Appending Lists
    master_list.append(list_one)
    master_list.append(list_two)
    master_list.append(list_three)
    master_list.append(list_four)
    print(menu)
    #Options
    user_input_two = input(":~Input a choice ~:")
    while user_input_two == "1" or user_input_two == "2" or user_input_two == "3" or user_input_two == "4" \
            or user_input_two == "5" or user_input_two == "6" or user_input_two == "7":
        if user_input_two == "1":
            choice_one(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "2":
            choice_two(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "3":
            choice_three(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "4":
            choice_four(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "5":
            choice_five(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "6":
            choice_six(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
        elif user_input_two == "7":
            choice_seven(master_list)
            print(menu)
            user_input_two = input(":~Input a choice ~:")
    print("Thank you")




# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()