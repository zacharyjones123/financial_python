name = []
date = []
time = []
lesson = []
money = []


# Way to print out all of the data in an organized way
def print_out_data():
    for i in range(len(money)):
        print("I completed a lesson with {name} at {date}|{time} in {lesson} for {money}".format(name=name[i],
                                                                                                 date=date[i],
                                                                                                 time=time[i],
                                                                                                 lesson=lesson[i],
                                                                                                 money=money[i]))


# Total Amount of Money Made (entire text file)
def total_money_made(money1):
    total = 0
    for m in money1:
        total += m
    return total


# Total number of lessons completed
def total_lessons_completed():
    return len(lesson)


# Open the file and read in the data
with open("chegg_test_data.txt") as chegg_test:
    for line in chegg_test.readlines():
        data = line.split(",")
        name.append(data[0])
        date.append(data[1])
        time.append(data[2])
        lesson.append(data[3])
        money.append(float(data[4][1:]))

# ----------------------------------------------------
# Below this is where all of the functions are called
# ----------------------------------------------------

# Tester for the total_money_made
print(total_money_made(money))

# Tester for total_lessons_completed
print(total_lessons_completed())
