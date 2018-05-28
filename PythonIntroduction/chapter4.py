
def before():
    #4-1
    pizzas = ['cheese','strawberry','beef']
    for pizza in pizzas:
        print('I like '+pizza+' pizza')
    print('I really love pizzas!')

    #4-2
    pets = ['dog','cat','bird']
    for pet in pets:
        print('A '+pet+' would make a great pet')
    print('Any of animals would make a great pet!')

    #4-3
    for i in range(1,21):
        print(i)

    #4-4
    for i in range(1,1000001):
        print(i)

    #4-5
    million = list(range(1,1000001))
    print(max(million))
    print(min(million))
    print(sum(million))
    # 4-6
    odd_1_20 = list(range(1,20,2))
    for i in odd_1_20:
        print(i)
    # 4-7
    divide_by3 = [num for num in range(3,30) if num%3==0]
    print(divide_by3)
    for i in divide_by3:
        print(i)
    # 4-8 4-9
    thirdmult = [num**3 for num in range(1,11)]
    for i in thirdmult:
        print(i)
    #4-10
    print('The first three items in the list are:',thirdmult[:3])
    print('The items from the middle of the list are:',thirdmult[4:7])
    print('The last three items in the list are:',thirdmult[-3:])

    #4-11
    pizzas = ['cheese','strawberry','beef']
    friend_pizzas = pizzas[:]
    pizzas.append('icecream')
    friend_pizzas.append('hot')
    print('My favorite pizzas are:')
    for pizza in pizzas:
        print(pizza)
    print("My friend's favorite pizzas are:")
    for pizza in friend_pizzas:
        print(pizza)
    #4-13
    foods = ('noodles','rice','fru it','water','juice')
    for food in foods:
        print(food)
    # foods[2]='hot dog'
    foods = ('hot dog','rice')
    for food in foods:
        print(food)