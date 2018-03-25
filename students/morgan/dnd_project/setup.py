from setuptools import setup

setup(
	name='5e_encounter_builder',
	author='Morgan H',
	packages=['encounter_builder'],
	# include_package_data=True,
	# package_data={'CR_vals':['resource_files/cr_guide.csv'],
     #              'adventuring_day_by_level':['resource_files/exp_by_level.csv'],
     #              'monster_multiplier':['resource_files/monster_multiplier.csv'],
	# 			  'encounter_budget_by_level':['resource_files/xp_budget_by_level.csv']},
	version="0.1",
	scripts=['bin/generator.py']
	)