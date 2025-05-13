import shlex


for case in [
    "1 2 '3 4'"
]:
    print('`{}` => `{!r}`'.format(case, shlex.split(case)))
