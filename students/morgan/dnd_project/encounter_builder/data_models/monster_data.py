class Monster():
    def __init__(self, cr, ac, hp_min, hp_max, attack_bonus, damage_rnd_min, damage_rnd_max, save_dc ):
        self.cr = cr
        self.ac = ac
        self.hp_min = hp_min
        self.hp_max = hp_max
        self.attack_bonus = attack_bonus
        self.damage_rnd_min = damage_rnd_min
        self.damage_rnd_max = damage_rnd_max
        self.save_dc = save_dc
        self.str = None
        self.dex = None
        self.con = None
        self.int = None
        self.wis = None
        self.cha = None