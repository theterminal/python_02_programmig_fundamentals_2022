# 20220621 - Python Code - Mid Exam Preparation
# 02 - The Lift - judge url: https://judge.softuni.org/Contests/Practice/Index/2517#1


people_waiting = int(input())
lift = list(map(int, input().split()))
flag = False

while True:
    for wagon in range(len(lift)):
        if lift[wagon] < 4:
            needed_people = 4 - lift[wagon]
            if people_waiting >= needed_people:
                lift[wagon] = 4
                people_waiting -= needed_people
            else:
                lift[wagon] += people_waiting
                flag = True
                break

    if flag:
        print('The lift has empty spots!')
        print(f'{" ".join([str(i) for i in lift])}')
        break

    elif not flag:
        if people_waiting > 0:
            print(f'There isn\'t enough space! {people_waiting} people in a queue!')
            print(f'{" ".join([str(i) for i in lift])}')
            break

        else:
            print(f'{" ".join([str(i) for i in lift])}')
            break
