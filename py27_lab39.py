def sample_key_arguments(fix1, fix2, **kargs):
    print("fix part=%s,%s" % (fix1, fix2))
    for k, v in kargs.items():
        print('k=%s, v=%s' % (str(k), str(v)))


sample_key_arguments('hello', 'world')
sample_key_arguments('hello', 'world', name='BDPY', duration=35, instructor='Mark',
                     schedule=['M', 'T', 'W'])
course1 = {'name': 'BDPY', 'duration': 35, 'instructor': 'Mark', 'schedule': ['M', 'T', 'W']}
sample_key_arguments('use a dict','to tramit', **course1)