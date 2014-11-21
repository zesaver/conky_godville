#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

username = 'ZESAVER'

resp = requests.get("http://godville.net/gods/api/"+username+".json")
data = resp.json()

print "Героиня: " if data["gender"] == "female" else "Герой: ",(data["name"].encode('utf-8'))
print 'Клан:',data["clan"]
print 'Характер:',data["alignment"].encode('utf-8')
print 'Девиз:',data["motto"].encode('utf-8')
print "Уровень: %.0f (%.0f/100)" % (data["level"],data["exp_progress"])
print "Здоровье: %.0f/%.0f" % (data["health"],data["max_health"])
print "Прана: %.0f/100" % (data["godpower"])
print 'Золотых:',data["gold_approx"].encode('utf-8')
print "Кирпичей: %.0f/1000" % (data["bricks_cnt"])
print 'Задание:',data["quest"].encode('utf-8'),"(%.0f/100)" % (data["quest_progress"])
print 'Последняя запись:',data["diary_last"].encode('utf-8')
print "Инвентарь: %.0f/%.0f" % (data["inventory_num"],data["inventory_max_num"])

inventory={}
for n, v in data["inventory"].iteritems():
	inventory[v["pos"]] = "  %s %s" % (v['pos']+1, n.encode('utf-8'))

print "\n".join([inventory[i] for i in sorted(inventory.keys())])
