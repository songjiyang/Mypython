
def before():
    #5-1
    car = 'subaru'
    print("Is car == 'subaru'? I predict True")
    print(car == 'subaru')

    print("Is car == 'audi'? I predict False")
    print(car == 'audi')

    num = 1
    print("Is num == 1? I predict True")
    print(num==1)
    print("Is num == '1'? I predict False")
    print(num=='1')
    print("Is num == 1.0 I predict True")
    print(num==1.0)

    names = ['alex','bob']
    samenames = names[:]
    print("Is nams == samenames? I predict False")  #I am wrong,It's True
    print(names == samenames)

    samenames2 = names

    print("Is nams == samenames2? I predict True")
    print(names == samenames2)

    samenames3 = names[:1]

    print("Is nams == samenames3? I predict False")
    print(names == samenames3)

    alien = {'color':'green','points':50}
    alien2 = {'color':'green','points':50}

    print("Is alien == alien2? I predict True")
    print(alien == alien2)
    #5-3
    alien_color = 'green'
    if alien_color == 'green':
        print('player got 5 points')
    alien_color = 'red'
    if alien_color == 'green':
        print('player got 5 points')

    #5-4
    alien_color = 'green'
    if alien_color == 'green':
        print('player get 5 points')
    else:
        print('player got 10 points')
    alien_color = 'blue'
    if alien_color == 'green':
        print('player get 5 points')
    else:
        print('player got 10 points')
def get_points(color):
    if color == 'green':
        print('player got 5 points')
    elif color == 'yellow':
        print('player got 10 points')
    else:
        print('player got 15 points')
#5-5
alien_color = ['yellow','red','green']
get_points(alien_color[0])
get_points(alien_color[1])
get_points(alien_color[2])