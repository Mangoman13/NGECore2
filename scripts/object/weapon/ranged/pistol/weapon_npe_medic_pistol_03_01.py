import sys
from resources.datatables import WeaponType

def setup(core, object):
	object.setStfFilename('static_item_n')
	object.setStfName('weapon_npe_medic_pistol_03_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('weapon_npe_medic_pistol_03_01')
	object.setStringAttribute('class_required', 'Medic')
	object.setIntAttribute('required_combat_level', 1)
	object.setAttackSpeed(0.4);
	object.setMaxRange(35);
	object.setDamageType("energy");
	object.setMinDamage(13);
	object.setMaxDamage(27);
	object.setWeaponType(WeaponType.PISTOL);
	return