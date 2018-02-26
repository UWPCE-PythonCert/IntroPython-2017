import random

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
        if difficulty == 1:
            self.build_easy(cr_stats)



    def build_easy(self, cr_stats):
        for x in range(self.enemy_types):
            print('yerp', cr_stats[self.cr_range_easy[-1]])
            self.final_force.append(Monster(self.cr_range_easy[-1] ,cr_stats[self.cr_range_easy[-1]]))

    def print_mons(self):
        for mon in self.final_force:
            print('cr', mon.cr)
            print('prof', mon.proficiency)
            print('ac', mon.ac)
            print('hp', mon.hp)
            print("atk", mon.attack_bonus)
            print('save', mon.save_dc)
            print('damage', mon.damage_rnd)


