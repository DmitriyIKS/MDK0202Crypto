# randomizing algorithm

import time
import math

minnum = int(input('Enter your min value > '))
maxnum = int(input('Enter your max value > '))
numsum = minnum

numstring = ''
numlist = []
i = minnum

while i <= maxnum:
    numlist.append(i)
    i += 1

def lengthoflist(thislist):
    numsinlist = 0
    while True:
        try:
            blank = thislist[numsinlist]

        except:
            break

        numsinlist += 1

    return numsinlist

def shuffle_list(oldlist):
    num = -1
    newlist = []

    while num < lengthoflist(oldlist) - 1:
        newlist.append(oldlist[num])
        num += 1

    return newlist


def randomize_list(numlist):
    global i, numtoadd

    numsinlist = lengthoflist(numlist)

    randomnum = ' '

    counter = 0

    if i >= numsinlist:
        while i >= numsinlist:
            i = i - (maxnum - minnum)

    if numtoadd >= numsinlist:
        numtoadd = numtoadd - numsinlist

    randomnum = numlist[i]

    i += numtoadd

    numtoadd += 1

    counter += 1

    return randomnum


j = 0

numtoadd = 44

numscalled = ' '

numlist = shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(numlist)))))))

counter = 0

countedlist = ' '

numscalled = 0

totalnums = 0

while True:
    blah = randomize_list(numlist)

    totalnums += 1

    if not ' ' + str(blah) + ' ' in countedlist:
        countedlist = countedlist + ' ' + str(blah) + ' '

        numscalled += 1

    print('Random number ' + str(blah))

    print(countedlist)

    print(' ', numscalled, ' ', totalnums)

    time.sleep(0.02)

    if numscalled >= maxnum - minnum + 1:
        break

    if counter >= 5:
        numlist = shuffle_list(
            shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(shuffle_list(numlist))))))))
        counter = 0

    counter += 1
    j += 1

print('Took ', totalnums, ' tries')
