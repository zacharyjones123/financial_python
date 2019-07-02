name = []
date = []
time = []
lesson = []
money = []

lesson_dict = {}
date_dict = {}


# Way to print out all of the data in an organized way
def print_out_data():
    for i in range(len(money)):
        print("I completed a lesson with {name} at {date}|{time} in {lesson} for {money}".format(name=name[i],
                                                                                                 date=date[i],
                                                                                                 time=time[i],
                                                                                                 lesson=lesson[i],
                                                                                                 money=money[i]))


# Total Amount of Money Made (entire text file)
def total_money_made():
    total = 0
    for m in money:
        total += m
    return total


# Total number of lessons completed
def total_lessons_completed():
    return len(lesson)


# Average amount of money made
def average_money_made():
    return total_money_made()/total_lessons_completed()


def make_lesson_dict():
    for l in lesson:
        if l in lesson_dict:
            lesson_dict[l] += 1
        else:
            lesson_dict[l] = 1


def print_lesson_dict():
    for l in lesson_dict:
        print("{} : {}".format(l, lesson_dict[l]))


def number_of_subjects():
    return len(lesson_dict.keys())


def make_date_dict():
    for d in date:
        if d in date_dict:
            date_dict[d] += 1
        else:
            date_dict[d] = 1


def print_date_dict():
    for d in date_dict:
        print("{} : {}".format(d, date_dict[d]))


# Open the file and read in the data
with open("chegg_test_data.txt") as chegg_test:
    index = 0

    for line in chegg_test.readlines():
        #print(line)
        if index == 0:
            # kelly
            name.append(line)
            index += 1
        elif index == 1:
            # Nov 27
            date.append(line)
            index += 1
        elif index == 2:
            # 1:24 PM
            time.append(line)
            index += 1
        elif index == 3:
            # Java Programming lesson
            lesson.append(line)
            index += 1
        elif index == 4:
            # n/a
            # Skip
            if not(line in "n/a\n"):
                if not(line in "Canceled\n") and not(line in "Void\n"):
                    money.append(float(line[1:]))
                index += 2
            else:
                 index += 1
        elif index == 5:
            # $38.50
            if not(line in "Canceled\n") and not(line in "Void\n"):
                money.append(float(line[1:]))
                index += 1
            else:
                index += 1
        elif index == 6:
            # View Lesson
            # Skip
            index = 0




# ----------------------------------------------------
# Below this is where all of the functions are called
# ----------------------------------------------------

# Tester for the total_money_made()
# print(total_money_made())

# Tester for total_lessons_completed()
# print(total_lessons_completed())

# Tester for average_money_made()
# print(average_money_made())

# Tester for make_lesson_dict()
# make_lesson_dict()

# Tester for print_lesson_dict()
# print_lesson_dict()

# Tester for number_of_subects()
# print(number_of_subjects())

# Tester for date_dict()
# make_date_dict()

# Tester for print_date_dict()
# print_date_dict()
