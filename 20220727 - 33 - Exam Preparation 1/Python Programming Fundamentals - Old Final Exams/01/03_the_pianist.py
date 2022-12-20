# 20220802 - Python - Old Exam
# 03 - The Pianist - judge url: https://judge.softuni.org/Contests/Practice/Index/2525#2


# ------------------------- version 1 ------------------------ judge: 100%


def import_pieces():
    num_pcs = int(input())
    pcs_dict = {}
    for _ in range(num_pcs):
        pc_data = input().split('|')
        pcs_dict[pc_data[0]] = [pc_data[1], pc_data[2]]  # pcs_dict = {piece: [composer, key]}

    return pcs_dict


def calculations(pcs_dict):
    # pcs_dict = {piece: [composer, key]}
    while True:
        command = input().split('|')
        if command[0] == 'Stop':
            break

        action = command[0]
        piece = command[1]

        if action == 'Add':
            composer = command[2]
            key = command[3]

            if piece in pcs_dict:
                print(f'{piece} is already in the collection!')
            else:
                pcs_dict[piece] = [composer, key]
                print(f'{piece} by {composer} in {key} added to the collection!')

        elif action == 'Remove':
            if piece not in pcs_dict:
                print(f'Invalid operation! {piece} does not exist in the collection.')
            else:
                del pcs_dict[piece]
                print(f'Successfully removed {piece}!')

        elif action == 'ChangeKey':
            new_key = command[2]

            if piece not in pcs_dict:
                print(f'Invalid operation! {piece} does not exist in the collection.')
            else:
                pcs_dict[piece][1] = new_key
                print(f'Changed the key of {piece} to {new_key}!')


def output(pcs_dict):
    # Format to print: {Piece} -> Composer: {composer}, Key: {key}

    for k, v in pcs_dict.items():
        print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')


def wrapper():
    pcs_dict = import_pieces()
    calculations(pcs_dict)
    output(pcs_dict)


wrapper()
