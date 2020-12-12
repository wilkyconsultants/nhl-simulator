#!/bin/usr/bin/python
#
# Works in python 2, not 3
#
import random
NUM_HORSES   = 8
HORSE_SPEEDS = 8
horses  = dict([('horse %s' % h, [random.randint(8,16) for n in range(HORSE_SPEEDS)]) for h in range(NUM_HORSES)])
for name, horse in horses.items():
    print("%s: %.3f" % (name, sum(horse) * 1.0 / HORSE_SPEEDS))


def race(horses, distance):
    positions = dict([(name, random.random()) for name, horse in horses.items()])
    
    running = True    
    while running:
        for name, horse in horses.items():
            positions[name] += random.choice(horse) + random.random()
            if positions[name] > distance:
                running = False
    return positions
positions = race(horses, 2000)
horse_order = horses.keys()
horse_order.sort(lambda x, y: cmp(positions[y], positions[x]))
for name in horse_order:
    print("%s: %.3f" % (name, sum(horses[name])*1.0/HORSE_SPEEDS))


NUM_PUNTERS  = 256
class Punter:
   max_skill = 4
        
   def __init__(self, horses):
        self.skill = random.randint(0,self.max_skill)
        self.money = random.randint(10, 20+self.skill*10)
        self.assessments = dict([(name, random.random() + sum(random.sample(horse, self.skill))) for name, horse in horses.items()])
        self.pick = self.pickHorse()
            
   def pickHorse(self):
        horses = self.assessments.keys()
        horses.sort(lambda x, y: cmp(self.assessments[y], self.assessments[x]))
        return horses[0]
punters = [Punter(horses) for n in range(NUM_PUNTERS)]


picks   = dict([(name, [punter.pick for punter in punters].count(name)) for name in horses.keys()])
for name in horse_order:
    print("%s: %.3f (%d)" % (name, sum(horses[name])*1.0/HORSE_SPEEDS, picks[name]))


skills  = dict([(name, [punter.skill for punter in punters if punter.pick == name]) for name in horses.keys()])
for name in horse_order:
    print("%s: %.3f (%d, %.2f)" % (name, sum(horses[name]) * 1.0 / HORSE_SPEEDS, picks[name], sum(skills[name]) * 1.0 / len(skills[name])))













