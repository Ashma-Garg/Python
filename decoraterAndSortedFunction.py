import operator

def person_lister(f):

    def inner(people):
        # people.sort(key=lambda x:x[2])
        # sorted(people,key=lambda x:x[2])
        #{sorted function can not be implemented directly on function because functions are not iterable.
        #To iterate through functions we use map function.
        #So if you want to use sort on functions then first use map and then sort}
        return map(f, sorted(people, key=lambda x: int(x[2])))
        #dont forget to use int before x[2] otherwise it will consider it as string and all cases wont pass as expected.
        return res
    return inner
# here @person_lister is a decorater which actually means:
# name_format=person_lister(name_format)
#whenever name_format will be called form main file then person_lister will be called which will have name_format as an its arguement.
#inner function will return to person_lister and person_lister will return to name_format
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))
