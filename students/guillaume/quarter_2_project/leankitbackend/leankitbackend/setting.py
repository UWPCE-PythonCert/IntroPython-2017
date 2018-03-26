from leankitbackend.util import import_data
from os import listdir, getcwd, path

needed_key = {"username",
              "company",
              "limit",
              "description",
              "password",
              "board",
              "output",
              "input",
              "cron_data",
              "teams_dic"}

input_n = 'input.json'
path_keys = ["input", "output", "cron_data"]


def init():
    global Leankit_input
    dir_c = listdir(getcwd())
    Leankit_input = {}
    if input_n in dir_c:
        tmp = import_data(input_n)
        if needed_key <= set(tmp) and check_path(path_keys, tmp):
            Leankit_input = tmp
    else:
        Leankit_input = {}
    return Leankit_input


def check_path(keys, dic):
    return all([path.exists(dic[key]) for key in keys])


if __name__ == '__main__':
    init()
    print(list(globals().keys()))
    # print('{} {}'.format(__name__, str(list(globals().keys()))))

