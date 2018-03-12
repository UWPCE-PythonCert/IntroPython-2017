import random
import math

class Monster():

    def __init__(self, cr, stat_list):
        self.cr = cr
        self.proficiency = stat_list[0]
        self.ac = stat_list[1]
        self.hp_min = stat_list[2]
        self.hp_max = stat_list[3]
        self.attack_bonus = stat_list[4]
        self.damage_rnd_min = stat_list[5]
        self.damage_rnd_max = stat_list[6]
        self.save_dc = stat_list[7]
        self.hp = random.randint(self.hp_min, self.hp_max)
        self.damage_rnd = random.randint(self.damage_rnd_min, self.damage_rnd_max)
        self.str = None
        self.dex = None
        self.con = None
        self.int = None
        self.wis = None
        self.cha = None
        self.size = None
        self.multi_attack = None
        self.dmg_per_attack = None

    # @classmethod
    def generate_stats(cls):
        sizes = ['tiny', 'small', 'medium', 'large', 'huge', 'gargantuan']
        stat_focus = ['str', 'dex']
        # print('cr', cls.cr)

        try:
            cr = float(cls.cr)
        except ValueError:
            cr = 0


        if 0 <= cr <= 1:
            cls.size = sizes[random.randrange(0, 1+1)]
            this_mon_focus = stat_focus[1]
        elif 1 < cr <= 5:
            cls.size = sizes[random.randrange(1, 3+1 )]
            this_mon_focus = stat_focus[random.randrange(0,1+1)]
        elif 6 <= cr <= 10:
            cls.size = sizes[random.randrange(2, 4+1)]
            this_mon_focus = stat_focus[random.randrange(0, 1 + 1)]
        elif 11 <= cr:
            cls.size = sizes[random.randrange(2, 5+1)]
            this_mon_focus = stat_focus[0]

        random.randint(0,10)

        # print('str before',cls.str)
        # print(this_mon_focus)
        # print(cls.attack_bonus)

        # print('focus', this_mon_focus)

        if this_mon_focus == 'str':
            # print('attack',cls.attack_bonus,'prof', cls.proficiency)
            cls.str = math.floor((cls.attack_bonus - cls.proficiency)*2 )
            cls.dex = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.str)
            cls.con = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.str)
            cls.wis = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.str)
            cls.int = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.str)
            cls.cha = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.str)
        elif this_mon_focus == 'dex':
            # print('attack',cls.attack_bonus,'prof', cls.proficiency)

            cls.dex = math.floor((cls.attack_bonus - cls.proficiency)*2 )
            cls.str = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.dex)
            cls.con = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.dex)
            cls.wis = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.dex)
            cls.int = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.dex)
            cls.cha = random.randint(math.floor(-5 + (cr/random.randint(3,10))), cls.dex)

        # print(cls.str, cls.dex)

        if cr < 3:
            cls.multi_attack = 1
            cls.dmg_per_attack = cls.damage_rnd
        else:
            cls.multi_attack = math.ceil(cr/6)
            cls.dmg_per_attack = cls.damage_rnd / cls.multi_attack

class Enemy_Force():
    def __init__(self, group_size, enemy_types, cr_range_easy, cr_range_medium, cr_range_hard, cr_range_daedly):
        self.group_size = group_size
        self.enemy_types = enemy_types
        self.cr_range_easy = cr_range_easy
        self.cr_range_medium = cr_range_medium
        self.cr_range_hard = cr_range_hard
        self.cr_range_deadly = cr_range_daedly
        self.final_force = []
        print('size', group_size)
        print('types', enemy_types)

    def build_force(self, cr_stats, difficulty):
        # print(cr_stats)
        if difficulty   == 1:
            self.build_mon(stat_options=cr_stats, cr_range=self.cr_range_easy)
        elif difficulty == 2:
            self.build_mon(stat_options=cr_stats, cr_range=self.cr_range_medium)
        elif difficulty == 3:
            self.build_mon(stat_options=cr_stats, cr_range=self.cr_range_hard)
        elif difficulty == 4:
            self.build_mon(stat_options=cr_stats, cr_range=self.cr_range_deadly)


    def build_mon(self, stat_options, cr_range):
        # print(cr_range)
        # print('types', self.enemy_types)
        for x in range(self.enemy_types):
            # print('yerp', cr_range[-1])
            self.final_force.append(Monster(cr_range[-1], stat_options[cr_range[-1]]))

        for x in self.final_force:
            print(vars(x))
            x.generate_stats()




    def print_mons(self):
        for index, mon in enumerate(self.final_force):
            print("Statistics for Monster {}".format(index+1))
            print('cr:     ', mon.cr)
            print('prof:   ', mon.proficiency)
            print('ac:     ', mon.ac)
            print('hp:     ', mon.hp)
            print('attacks:', mon.multi_attack)
            print("To-Hit: ", mon.attack_bonus)
            print('save:   ', mon.save_dc)
            print('damage: ', mon.damage_rnd)

            print('str:    ', mon.str)
            print('dex:    ', mon.dex)
            print('con:    ', mon.con)
            print('int:    ', mon.int)
            print('wis:    ', mon.wis)
            print('cha:    ', mon.cha)
            print('size:   ', mon.size)


