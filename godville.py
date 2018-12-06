#!/usr/bin/python2
# -*- coding: utf-8 -*-
import requests

username = ''
token = ''

resp = requests.get("http://godville.net/gods/api/"+username+"/"+token)
data = resp.json()

if not token:
  ### GENERAL
  print "Героиня:" if data["gender"] == "female" else "Герой:",(data["name"].encode('utf-8'))
  print 'Гильдия: %s в %s' % (data["clan_position"].encode('utf-8'),data["clan"].encode('utf-8')) if data["clan"] else 'Гильдия: нет'
  print 'Характер:',data["alignment"].encode('utf-8')
  print 'Девиз:',data["motto"].encode('utf-8')
  print "Уровень: %.0f" % (data["level"])
  print 'Золотых:',data["gold_approx"].encode('utf-8')
  ##Temple
  if data["bricks_cnt"] < 1000:
    print "Кирпичей: %.0f/1000" % (data["bricks_cnt"])
  elif data["wood_cnt"] < 1000:
    print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
  else:
    print "Храм и ковчег достроены"
    print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
    print "Тварей по паре: %.0fм, %.0fж" % (data["ark_m"],data["ark_f"])
    print "Сбережения: %s/30М" % (data["savings"].encode('utf-8'))
    print

  ### PET
  if "pet" in data:
    print "   Питомец:"
    print "Имя:",data["pet"]["pet_name"].encode('utf-8')
    #print "Вид:",data["pet"]["pet_class"].encode('utf-8') #temporary removed due undocumented changes in Godville API
    print "Уровень:",data["pet"]["pet_level"]
    if "wounded" in data["pet"]:
      print "!!! Контужен !!!"
    print

  ### Arena
  print "Арена: %.0f побед, %.0f поражений" % (data["arena_won"],data["arena_lost"])
  if "fight_type" in data:
    if data["fight_type"] == "sail":
      print "Заплыв!"
    elif data["fight_type"] == "arena":
      print "На арене!"
    elif data["fight_type"] == "challenge":
      print "Тренируется!"
    elif data["fight_type"] == "dungeon":
      print "В подземелье!"

else:
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
  elif "t_level" in data:
    print "Храм, ковчег и лавка достроены. Пенсия..."
    print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
    print "Тварей по паре: %.0fм, %.0fж" % (data["ark_m"],data["ark_f"])
    print "Уровень героя-торговца: %.0f" % (data["t_level"])
    print
  else:
    print "Храм и ковчег достроены"
    print "Дерева гофер: %.0f/1000" % (data["wood_cnt"])
    print "Тварей по паре: %.0fм, %.0fж" % (data["ark_m"],data["ark_f"])
    print "Сбережения: %s/30М" % (data["savings"].encode('utf-8'))
    print
  print 'Задание:',data["quest"].encode('utf-8'),"(%.0f/100)" % (data["quest_progress"])
  print 'Последняя запись:',data["diary_last"].encode('utf-8')

  if "town_name" in data: #if no town_name key present we suppose hero is on arena
    if data["town_name"]:
      print "Город:",data["town_name"].encode('utf-8')
    else:
      print "Столбов от столицы:",data["distance"]
  print

  ### Arena
  print "Арена: %.0f побед, %.0f поражений" % (data["arena_won"],data["arena_lost"])
  print

  ### PET
  if "pet" in data:
    print "   Питомец:"
    print "Имя:",data["pet"]["pet_name"].encode('utf-8')
    # print "Вид:",data["pet"]["pet_class"].encode('utf-8') #temporary removed due undocumented changes in Godville API
    print "Уровень:",data["pet"]["pet_level"]
    if "wounded" in data["pet"]:
      print "!!! Контужен !!!"
    print

  ### INVENTORY
  # if data["activatables"]:
  #   print "В карманах можно найти: %.0f/%.0f" % (data["activatables_num"],data["activatables_max_num"])
  #   activatables={}
  #   for n, v in data["activatables"].iteritems():
  #     activatables[v["pos"]] = "  %s %s" % (v['pos']+1, n.encode('utf-8'))
  #   print "\n".join([activatables[i] for i in sorted(activatables.keys())])

  # else:
  #   print "В карманах героини пусто" if data["gender"] == "female" else "В карманах героя пусто"
