def before():
    def invite(list):
        #3-9
        print('i invited '+str(len(list))+' people')
        for people in list:
            print(people + ' Welcome to my home to have dinner')
    #3-4
    guests = ['My Mom','My Dad','My Grandpa','My Brother']
    invite(guests)

    #3-5
    print(guests[2])
    guests[2]='My Aunt'
    invite(guests)

    #3-6
    print('big dinnerTable')
    guests.insert(0,'Bob')
    guests.insert(3,'Jim')
    guests.append('Lily')
    invite(guests)

    #3-7
    print('sorry my new dinnerTable dont arrial in time,now only two people i can invite to')
    while len(guests)>2:
        pop_guest = guests.pop()
        print('sorry '+pop_guest+" i can't invite you")
    invite(guests)
    print(guests)
    del guests[0]
    del guests[0]
    invite(guests)
    print(guests)

def after():
    #3-8
    place = ['scotland','roman','paris','afghan','tokyo']
    print(place)
    print(sorted(place))
    print(place)
    print(sorted(place,reverse=True))
    print(place)
    place.reverse()
    print(place)
    place.reverse()
    print(place)
    place.sort()
    print(place)
    place.sort(reverse=True)
    print(place)


#
# before()
motor = []
print(motor[-1])