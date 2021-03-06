import sys

def setup(core, object):
	object.setIntAttribute('required_combat_level', 80)
	object.setStringAttribute('required_faction', 'Rebel')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 15)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:luck_modified', 10)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:precision_modified', 20)
	object.setStringAttribute('armor_category', '@obj_attr_n:armor_assault')
	object.setIntAttribute('cat_armor_standard_protection.kinetic', 6440)
	object.setIntAttribute('cat_armor_standard_protection.energy', 4440)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_heat', 4440)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_cold', 4440)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_acid', 4440)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_electricity', 4440)
	return	