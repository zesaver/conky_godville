#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

username = 'ZESAVER'

resp = requests.get("http://godville.net/gods/api/"+username+".json")
data = resp.json()

### GENERAL
print "Героиня:" if data["gender"] == "female" else "Герой:",(data["name"].encode('utf-8'))
print 'Гильдия: %s в %s' % (data["clan_position"].encode('utf-8'),data["clan"].encode('utf-8')) if data["clan"] else 'Гильдия: нет'
print 'Характер:',data["alignment"].encode('utf-8')
print 'Девиз:',data["motto"].encode('utf-8')
print "Уровень: %.0f (%.0f/100)" % (data["level"],data["exp_progress"])
print "Здоровье: %.0f/%.0f" % (data["health"],data["max_health"])
print "Прана: %.0f/100" % (data["godpower"])
print 'Золотых:',data["gold_approx"].encode('utf-8')
##Temple
if data["bricks_cnt"] < 1000:
	print "Кирпичей: %.0f/1000" % (data["bricks_cnt"])
elif data["wood_cnt"] < 1000:
	print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
else:
	print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
	print "Храм и ковчег достроены"
print 'Задание:',data["quest"].encode('utf-8'),"(%.0f/100)" % (data["quest_progress"])
print 'Последняя запись:',data["diary_last"].encode('utf-8')

if "town_name" in data: #if no town_name key present we suppose hero is on arena
	if data["town_name"]:
		print "Город:",data["town_name"].encode('utf-8')
	else:
		print "Столбов от столицы:",data["distance"]

### PET
if "pet" in data:
	print "   Питомец:"
	print "Имя:",data["pet"]["pet_name"].encode('utf-8')
	print "Вид:",data["pet"]["pet_class"].encode('utf-8')
	print "Уровень:",data["pet"]["pet_level"]
	if "wounded" in data["pet"]:
		print "!!! Контужен !!!"
	print

### INVENTORY
if data["inventory"]:
	print "В карманах можно найти: %.0f/%.0f" % (data["inventory_num"],data["inventory_max_num"])
	inventory={}
	for n, v in data["inventory"].iteritems():
		inventory[v["pos"]] = "  %s %s" % (v['pos']+1, n.encode('utf-8'))
	print "\n".join([inventory[i] for i in sorted(inventory.keys())])

else:
	print "В карманах героини пусто" if data["gender"] == "female" else "В карманах героя пусто"
