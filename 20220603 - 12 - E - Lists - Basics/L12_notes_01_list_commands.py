# 20220603 - Python Code - Lists Basics

# ------- .sort() --------------------


# list_kk.sort()                            # sorts list in ascending order; works for nums and alpha
# list_kk.sort(reverse=True)                # sorts list in descending order; works for nums and alpha
# print(list_kk.sort)                       # cannot use this syntax (it returns None). Also, cannot assign it to a variable.


# ------- .reverse() -----------------


# list_kk.reverse                           # reverses the list
# list_kk[::-1]                             # reverses the list (using slicing)
# print(list_kk_2.reverse()                 # cannot use this syntax (it returns None). Also, cannot assign it to a variable.


# ------- .pop() ---------------------


# list_kk.pop()                             # deletes the last element from the list, returns the deleted (popped) element
# a = list_kk.pop()                         # 'a' takes the value of the popped element
# list_kk.pop(4)                            # deletes and returns the element with the specified index


# ------- del list_kk[index] ---------


# del list_kk[7]                            # deletes the element on the specified index


# ------- .remove() ------------------


# list_kk.remove(10)                        # removes the element with the specified value


# ------- .append() ------------------


# list_kk.append(value)                     # appends an element in the list, at the end, with the specified value (element)
# list_kk_1.append(list_kk_2.pop())         # takes the last element from list_kk_2 and adds it as last element of list_kk_1


# ------- .insert(index, element) ----


# list_kk.insert(5, 'George')               # inserts 'George' into the list on index 5


# ------- .index(value) --------------


# list_kk.index(34)                         # returns the index of the specified element


# ------- .count(element) --------------


# list_kk.count(5)                         # counts how many times the specified element exist in the list


# Examples of the above methods
print('\n---------- .sort() ----------------------\n')


list_kk_1 = [2, 34, -4, 5, 0]
print(list_kk_1, '- Original list => \'list_kk_1 = [2, 34, -4, 5, 0]\' => \'print(list_kk_1)\'')

list_kk_1.sort()
print(list_kk_1, '- Same list sorted ascending => \'list_kk_1.sort()\' => \'print(list_kk_1)\'')

list_kk_1.sort(reverse=True)
print(list_kk_1, '- Same list sorted descending => \'list_kk_1.sort(reverse=True)\' => \'print(list_kk_1)\'')

print(list_kk_1.sort(), '             - Cannot use this syntax, Returns \'None\' => \'print(list_kk_1.sort())\'')


print('\n---------- .reverse() --------------------\n')


list_kk_2 = [2, 34, -4, 5, 0]
print(list_kk_2, '- Original list => \'list_kk_2 = [2, 34, -4, 5, 0]\' => \'print(list_kk_2)\'')

list_kk_2.reverse()
print(list_kk_2, '- Same list reversed => \'list_kk_2.reverse()\' => \'print(list_kk_2)\'')

print(list_kk_2[::-1], '- Same list reversed again using slicing => \'print(list_kk_2[::-1])\'')

print(list_kk_2.reverse(), '             - Cannot use this syntax. Returns \'None\' => \'print(list_kk_2.reverse())\'')


print('\n---------- .pop() ------------------------\n')


list_kk_3 = [2, 34, -4, 5, 0]
print(list_kk_3, '- \'list_kk_3 = [2, 34, -4, 5, 0]\' - Original list => \'print(list_kk_3)\'')

list_kk_3.pop()
print(list_kk_3, '   - \'list_kk_3.pop()\' - removes the last element from the list => \'print(list_kk_3)\'')

list_kk_3.pop(1)
print(list_kk_3, '       - \'list_kk_3.pop(1)\' - removes the element with the specified index, from the list, and returns its value if needed => \'print(list_kk_3)\'')

print(list_kk_3.pop(), '                - \'print(list_kk_3.pop())\' => Prints out the deleted element from the list.')

print(list_kk_3, '          - \'list_kk_3\' - after the above operations')

print('\n\'.pop()\' is similar to \'.remove()\' but \'.remove()\' does NOT return the element that is being deleted. It returns \'None\'')


print('\n---------- del list_kk[index] ---------------\n')


lst_kk_6 = [2, 34, -4, 5, 0]
print(lst_kk_6, '   - \'lst_kk_6 = [2, 34, -4, 5, 0]\' - Original list => \'print(list_kk_6\')')

del lst_kk_6[3]
print(lst_kk_6, '      - \'del list_kk_6[3]\' - deletes the element on index 3 => \'print(list_kk_6)\'')


print('\n---------- .remove() ---------------------\n')


list_kk_7 = [5, 10, -12, 25, 0]
print(list_kk_7, '  - \'list_kk_7 = [5, 10, -12, 25, 0]\' - Original list => \'print(list_kk_7)\'')

list_kk_7.remove(10)
print(list_kk_7, '      - \'list_kk_7.remove(10)\' => \'print(list_kk_7)\'')


print('\n---------- .append() ---------------------\n')


list_kk_4 = [2, 34, -4, 5, 0]
print(list_kk_4, '          - \'list_kk_4 = [2, 34, -4, 5, 0]\' - Original list => \'print(list_kk_4)\'')

list_kk_4.append(4555)
print(list_kk_4, '    - \'list_kk_4.append(4555)\'        - Adds the specified value/element to the end of the list => \'print(list_kk_4)\'')

print('\n\'list_kk_1.append(list_kk_2.pop())\'                           - This syntax takes the last element from \'list_kk_2\' and adds it as last element of \'list_kk_1\'')


print('\n---------- .insert() ---------------------\n')


list_kk_5 = [2, 34, -4, 5, 0]
print(list_kk_5, '              - \'list_kk_5 = [2, 34, -4, 5, 0]\' - Original list => \'print(list_kk_5)\'')

list_kk_5.insert(3, 'Gosho')
print(list_kk_5, '     - \'list_kk_5.insert(3, \'Gosho\') => inserting \'Gosho\' on index 3 => \'print(list_kk_5)\'')


print('\n---------- .index() ----------------------\n')


list_kk_8 = [2, 34, -4, 5, 0]
print(list_kk_8, '- \'list_kk_8 = [2, 34, -4, 5, 0]\' - Original list => \'print(list_kk_8)\'')

num = list_kk_8.index(34)
print(num, '                - \'num = list_kk_8.index(34)\' - \'num\' takes the value of the element of the specified index. => \'print(num)\'')


print('\n---------- .count() ----------------------\n')


list_kk_9 = [2, 5, -4, 5, 0]
print(list_kk_9, '  - \'list_kk_9 = [2, 5, -4, 5, 0]\' - Original list => \'print(list_kk_9)\'')

repetition = list_kk_9.count(5)
print(repetition, '                 - \'repetition = list_kk_9.count(5)\' - Counts how many times the element with value \'5\' is found in the list => \'print(repetition)\'')


print('\n---------- .append().pop() ---------------\n')


list_kk_10 = [2, 34, -4, 5, 0]                                              # original list
print(list_kk_10, '             - Original list - \'list_kk_10 = [2, 34, -4, 5, 0]\'')

list_kk_11 = ['apple', 'fish', 'beer']                                      # second list
print(list_kk_11, '     - Original list - \'list_kk_11 = [\'apple\', \'fish\', \'beer\']')

list_kk_11.append(list_kk_10.pop())                                         # useful tip
print(list_kk_11, '  - result after  - \'list_kk_11.append(list_kk_10.pop())\'')


print('\n---------- .copy() -----------------------\n')


list_kk_12 = [2, 34, -4, 5, 0]
print(list_kk_12, '- \'list_kk_12\' - original list')

list_kk_13 = list_kk_12                                                      # it does not copy the list only points to it in the memory
print(list_kk_13, '- \'list_kk_13\' after \'list_kk_13 = list_kk_12\' - looks identical but if you change one of the list, it\'ll change both')

list_kk_14 = list_kk_12.copy()                                               # that is the correct way to do it.
print(list_kk_14, '- \'list_kk_14\' after \'list_kk_14 = list_kk_12.copy\' - that creates completely independent instance in the memory')


print('\n--------- list comp-n --------------------\n')


list_100 = [1, 2, 3, -4, -6]                         # original list
print(list_100)

list_200 = [int(i) * -1 for i in list_100]           # changed the value of elements using list comp-n
print(list_200)


print('\n-------------------- The code above this line is a result of the four lines bellow--------------------')
print('\nlist_100 = [1, 2, 3, -4, -6]                         # original list')
print('print(list_100)')

print('\nlist_200 = [int(i) * -1 for i in list_100]           # changed the value of elements using list comp-n')
print('print(list_200)')
