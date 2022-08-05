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


""" --------------------- The Pianist -----------------------


You are a pianist, and you like to keep a list of your favorite piano pieces.
Create a program to help you organize it and add, change, remove pieces from it!

On the first line of the standard input, you will receive an integer 'n' – the number of pieces you will initially have.
On the next 'n' lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format:

"{piece}|{composer}|{key}".

Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:

    •	"Add|{piece}|{composer}|{key}":
        o	You need to add the given piece with the information about it to the other pieces and print:
            "{piece} by {composer} in {key} added to the collection!"

        o	If the piece is already in the collection, print:
            "{piece} is already in the collection!"

    •	"Remove|{piece}":

        o	If the piece is in the collection, remove it and print:
            "Successfully removed {piece}!"

        o	Otherwise, print:
            "Invalid operation! {piece} does not exist in the collection."

    •	"ChangeKey|{piece}|{new key}":

        o	If the piece is in the collection, change its key with the given one and print:
            "Changed the key of {piece} to {new key}!"

        o	Otherwise, print:
            "Invalid operation! {piece} does not exist in the collection."

Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:

"{Piece} -> Composer: {composer}, Key: {key}"


Input/Constraints:
-----------------

    •	You will receive a single integer at first – the initial number of pieces in the collection
    •	For each piece, you will receive a single line of text with information about it.
    •	Then you will receive multiple commands in the way described above until the command "Stop".

Output:
------
    •	All the output messages with the appropriate formats are described in the problem description.


---------------- Test Data ------------------


Input 1:
-------
3
Fur Elise|Beethoven|A Minor
Moonlight Sonata|Beethoven|C# Minor
Clair de Lune|Debussy|C# Minor
Add|Sonata No.2|Chopin|B Minor
Add|Hungarian Rhapsody No.2|Liszt|C# Minor
Add|Fur Elise|Beethoven|C# Minor
Remove|Clair de Lune
ChangeKey|Moonlight Sonata|C# Major
Stop


Output 2:
--------
Sonata No.2 by Chopin in B Minor added to the collection!
Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
Fur Elise is already in the collection!
Successfully removed Clair de Lune!
Changed the key of Moonlight Sonata to C# Major!
Fur Elise -> Composer: Beethoven, Key: A Minor
Moonlight Sonata -> Composer: Beethoven, Key: C# Major
Sonata No.2 -> Composer: Chopin, Key: B Minor
Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor


---------------------------------------------


Input 2:
-------
4
Eine kleine Nachtmusik|Mozart|G Major
La Campanella|Liszt|G# Minor
The Marriage of Figaro|Mozart|G Major
Hungarian Dance No.5|Brahms|G Minor
Add|Spring|Vivaldi|E Major
Remove|The Marriage of Figaro
Remove|Turkish March
ChangeKey|Spring|C Major
Add|Nocturne|Chopin|C# Minor
Stop


Output 2:
--------
Spring by Vivaldi in E Major added to the collection!
Successfully removed The Marriage of Figaro!
Invalid operation! Turkish March does not exist in the collection.
Changed the key of Spring to C Major!
Nocturne by Chopin in C# Minor added to the collection!
Eine kleine Nachtmusik -> Composer: Mozart, Key: G Major
La Campanella -> Composer: Liszt, Key: G# Minor
Hungarian Dance No.5 -> Composer: Brahms, Key: G Minor
Spring -> Composer: Vivaldi, Key: C Major
Nocturne -> Composer: Chopin, Key: C# Minor


---------------------------------------------

"""