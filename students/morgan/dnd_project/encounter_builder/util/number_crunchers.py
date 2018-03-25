# import pkgutil
# import encounter_builder
import csv
import math
import random

def establish_budgets(infile, party):
    difficulty_sheet = {}
    with open(infile, 'r') as f:
        read_data = csv.reader(f,delimiter=',')
        next(read_data, None)
        for entry in read_data:
            # entry = line.split(",")
            # print('entry',entry)
            level = entry[0]
            easy = int(entry[1])
            medium = int(entry[2])
            hard = int(entry[3])
            deadly = int(entry[4])
            difficulty_sheet[level] =[easy,medium,hard,deadly]

    # for key, val in difficulty_sheet.items():
    #     print(key, val)

    # print(party)
    PCs = party.members

    for x in range(1,20+1):
        level_key = str(x)
        party.easy += (PCs.count(x) * difficulty_sheet[level_key][0])
        party.medium += (PCs.count(x) * difficulty_sheet[level_key][1])
        party.hard += (PCs.count(x) * difficulty_sheet[level_key][2])
        party.deadly += (PCs.count(x) * difficulty_sheet[level_key][3])
    #
    # print(party.easy)
    # print(party.medium)
    # print(party.hard)
    # print(party.deadly)


def CR_ranges(xp_by_cr, monster_multiplier, party, group_size):
    """
    
    :param xp_by_cr: file that lists out how much XP each CR value is worth before any modifictation
    :param monster_multiplier: file that translates a desired enemy force size and modifies XP budgets accordingly
    :param party: the PC party class object
    :param group_size: How many monsters to fight
    :return: CR ranges for party class are updated
    
    1. Difficulty XP budgets are defined by number and level of PCs  (total xp budget)
    2. The XP value of monsters is increased based on how many will be in the fight  (multiplier)
    3. The ((total xp budget) / multipler) / number of monsters gives you the maximum XP value, per monster, that can be used
    4. That max XP value determines what CR range the monsters can come from
    5. If no CR is valid for any fight, then it is deemed "Deadly" with a CR range of only CR 0 monsters, overriding the xp value of 10
    6. These values are updated in the Party class for later use
    
    example: 4x lvl 1 
    """

    cr_values = {}
    mon_multiplier = []
    cr_divider = 0
    cr_list_in_order = []



    with open(xp_by_cr, 'r')as f:
        cr_csv = csv.reader(f, delimiter=',')
        next(cr_csv, None)
        for entry in cr_csv:
            cr = str(entry[0])
            xp = int(entry[1])
            cr_values[cr]=xp
            cr_list_in_order.append(cr)

    # print(cr_values)



    with open(monster_multiplier, 'r') as f:
        multiplier_csv = csv.reader(f, delimiter=',')
        next(multiplier_csv, None)
        # print('groupsize', group_size)

        # print('test', multiplier_csv)

        for x in multiplier_csv:
            mon_multiplier.append(x)

        # print('cr', mon_multiplier)

        for x in mon_multiplier:
            for i, value in enumerate(x):
                if x[i].strip() == 'None':
                    x[i] = math.inf
                    print(x[i])
                else:
                    x[i] = float(x[i])

        # for x in mon_multiplier:
        #     print(x)

        for x in mon_multiplier:
            if x[0] <= group_size <= x[1]:
                cr_divider = x[2]




    # print('divider',cr_divider)

    # print(party.easy)
    # print(type(cr_divider))

    easy_mon_xp_pool = party.easy / cr_divider
    medium_mon_xp_pool = party.medium / cr_divider
    hard_mon_xp_pool = party.hard / cr_divider
    deadly_mon_xp_pool = party.deadly / cr_divider

    # print('deadly pool', deadly_mon_xp_pool)

    easy_mon_max_xp = easy_mon_xp_pool / group_size
    medium_mon_max_xp = medium_mon_xp_pool / group_size
    hard_mon_max_xp = hard_mon_xp_pool / group_size
    deadly_mon_max_xp = deadly_mon_xp_pool / group_size

    # print('dead max', deadly_mon_max_xp)

    easy_cr_range=[]
    medium_cr_range=[]
    hard_cr_range=[]
    deadly_cr_range=[]




    for key, val in cr_values.items():
        # print(key, val)
        if val <= easy_mon_max_xp:
            easy_cr_range.append(key)
        if val <= medium_mon_max_xp:
            medium_cr_range.append(key)
        if val <= hard_mon_max_xp:
            hard_cr_range.append(key)
        if val <= deadly_mon_max_xp:
            deadly_cr_range.append(key)

    if deadly_cr_range == []:
        deadly_cr_range.append(cr_list_in_order[0])

    party.set_cr_ranges(easy_cr_range, medium_cr_range, hard_cr_range, deadly_cr_range)
    # print(easy_cr_range.values())

    # print('easy xp total{}, easy pool after multi{}, easy XP max{}, easy CR range{}'.format(party.easy, easy_mon_xp_pool, easy_xp_max, easy_cr_range))
    # print('medium fight',medium_cr_range)
    # print('hard fight', hard_cr_range)
    # print('easy fight', easy_cr_range)
    # print('deadly', deadly_cr_range)


def monster_stat_ranges(infile):
    # print('stats start here')
    the_dict = {}
    with open(infile, 'r') as f:
        cr_stats = csv.reader(f,delimiter=',')
        # next(cr_stats, None)
        for entry in cr_stats:
            the_dict[entry[0]]=entry[1:]
            # print(entry)

    # print(the_dict)
    for key, val in the_dict.items():
        for index, entry in enumerate(val):
            if entry.startswith('<'):
                holder = int(entry.strip('<'))
                val[index] = holder - random.randint(0, math.ceil(.5 * holder))
            try:
                val[index] = int(entry)
            except: ValueError


    # print(the_dict)
    return the_dict