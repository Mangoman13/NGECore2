import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('scyk')
	mobileTemplate.setLevel(11)
	mobileTemplate.setMinLevel(11)
	mobileTemplate.setMaxLevel(13)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(40)
	mobileTemplate.setHideType("Bristly Hide")
	mobileTemplate.setBoneAmount(25)	
	mobileTemplate.setBoneType("Animal Bone")
	mobileTemplate.setHideAmount(18)
	mobileTemplate.setSocialGroup("scyk")
	mobileTemplate.setAssistRange(10)
	mobileTemplate.setStalker(True)	
	mobileTemplate.setOptionsBitmask(Options.AGGRESSIVE + Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_scyk.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('scyk', mobileTemplate)
	return