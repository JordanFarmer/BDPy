day_of_week = ('Sunday', 'Monday')
day_of_week += ('Tuesday',)
# day_of_week += ('Tuesday')
print day_of_week
k1 = 'Tuesday'
k2 = ('Tuesday',)
print (type(k1), type(k2))
print(k1 * 5)
print(k2 * 5)
print(day_of_week[0], day_of_week[2], day_of_week[1])


def split_head(seq):
    return seq[0], seq[1:]


day_of_week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

head, remaining = split_head(day_of_week_list)
print(type(remaining), remaining)
print(type(head), head)