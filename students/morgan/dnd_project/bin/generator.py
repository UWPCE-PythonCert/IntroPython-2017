from encounter_builder.interface import ui
from encounter_builder.data_models import party_data
from encounter_builder.util import number_crunchers
# import setup
# import encounter_builder.resource_files



if __name__ == "__main__":


    print("doo-da")
    # xp_budget_file = setup.package_data['encounter_budget_by_level']
    xp_budget_file = "encounter_builder/resource_files/xp_budget_by_level.csv"
    monster_multiplier = "encounter_builder/resource_files/monster_multiplier.csv"
    xp_by_cr = "encounter_builder/resource_files/xp_by_cr.csv"
    # print(xp_budget_file)

    the_party = party_data.Party(ui.Get_PCs())
    print(the_party.members, the_party.min, the_party.crowd)

    _ = number_crunchers.establish_budgets(xp_budget_file, the_party)

    # the_party.set_budgets(_)


    print('easy',the_party.easy)
    print('medium', the_party.medium)
    print('hard', the_party.hard)
    print('deadly', the_party.deadly)

    group_size = int(input("How many enemies should the party face?\n>"))




    number_crunchers.CR_ranges(xp_by_cr,monster_multiplier, the_party, group_size)
    # print(the_party.deadly)

    # the_party.monster_types(group_size)

    monster_variety = ui.monster_types(group_size)

    # print(monster_variety)

    # for x in range(monster_variety+1):
    #










