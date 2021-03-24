import os

p_l = {'my project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def create_dir(f_l):
    for f, f_s in f_l.items():
        if not os.path.exists(f):
            for i in range(len(f_s)):
                os.makedirs(os.path.join(f, f_s[i]))


create_dir(p_l)