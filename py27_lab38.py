# encoding=UTF-8
def sample_variable_arguments(fix1, fix2, *args):
    print('fix part=%s,%s' % (fix1, fix2))
    for arg in args:
        print('variable part:%s' % arg)


sample_variable_arguments("hello", 'world!!!')
sample_variable_arguments("hello", 'world', 300)
sample_variable_arguments("hello", 'welcome', 3, 'hello', 'hi', 123.45, None, 5 + 4j)
l1 = [3, 'hello', 'hi', 123.45, None, 5 + 4j]
sample_variable_arguments("welcom", '中文', l1)
sample_variable_arguments("welcom", '中文list_expanded', *l1)
t1 = (3, 'hello', 'hi', 123.45, None, 5 + 4j, 7)
sample_variable_arguments("welcom", '中文tuple', *t1)
s1 = {3, 'hello', 'hi', 123.45, None, 5 + 4j, "git"}
sample_variable_arguments("welcom", '中文set', *s1)