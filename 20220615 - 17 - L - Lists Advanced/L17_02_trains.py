# 20220616 - Python - Lists Advance - Lecture
# 02 - Trains - judge: https://judge.softuni.org/Contests/Practice/Index/1730#1


# ----------------- version 1 ------------------- judge 100%


wagons = int(input())
train = [0 for n in range(wagons)]                      # train = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break

    lst_com = [n for n in command.split(' ')]
    operation = lst_com[0]

    if operation == 'add':
        num_people = int(lst_com[1])
        train[-1] += num_people
    else:
        index = int(lst_com[1])
        people = int(lst_com[2])

        if operation == 'insert':
            train[index] += people

        elif operation == 'leave':
            train[index] -= people

print(train)


""" _______________ Trains _________________


You will receive a number representing the number of wagons a train has.
Create a list (train) with the given length containing only zeros.

Until you receive the command "End", you will receive some of the following commands:

    •	"add {people}"              – you should add the number of people in the last wagon
    •	"insert {index} {people}"   - you should add the number of people at the given wagon
    •	"leave {index} {people}"    - you should remove the number of people from the wagon.

-	There will be no case in which the people will be more than the count in the wagon.
-	There will be no case in which the index is invalid!

After you receive the "End" command print the train.



___________ Test Data ____________


Input 1:
-------
3
add 20
insert 0 15
leave 0 5
End


Output 1:
--------
[10, 0, 20]


----------------------------------


Input 2:
-------
5
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End


Output 2:
--------
[16, 32, 100, 0, 105]


"""