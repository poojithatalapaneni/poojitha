def birthday(inp):
    if inp == "revs":
        print(inp,'bithday is',data['revs'])
    elif inp == 'pooji':
        print(inp,'birthday is',data['pooji'])
    elif inp  == 'pavs':
        print(inp,'birthday is',data['pavs'])
    else:
        print("the input you give is not in your dictionary please recheck")


data = {'revs':'12/05/200','pooji':'14/09/1999','pavs':'15/08/200'}
print('welcome to the birthday dictionary.we know the birthday of:\nrevs\npooji\npavs')
inp=input("who's birthday do you want to loop up")
birthday(inp)

