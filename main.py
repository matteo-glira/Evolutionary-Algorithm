import random
import math

DEBUG = False

bot_list = []
auswertung_list = []
best_bots = []
max_random_num = 1000
num_bots = 1000
generations = 10
length = int(num_bots/10)

def debug(var="", activated=True):
    if DEBUG:
        if activated:
            print(var)

def auswertung(a, b, c, d, e):
    return -math.pow(a - 3, 2) - math.pow(b - 5, 2) - math.pow(
    c - 7, 2) - math.pow(d - 9, 2) - math.pow(e - 11, 2)

def average(n1, n2):
   return (n1 + n2) / 2

def swap(arr1, arr2, point):
    aa = arr1[:]
    bb = arr2[:]
    for i in range(point):
        #aa[i], bb[i] = bb[i], aa[i]
        aa[i], bb[i] = random.randint(0, bb[i]), random.randint(0, aa[i]) 
        #aa[i], bb[i] = random.randint(0, max_random_num), random.randint(0, max_random_num) 
        #aa[i], bb[i] = bb[i], aa[i]
    auswertung_aa = auswertung(aa[0], aa[1], aa[2], aa[3], aa[4])
    auswertung_bb = auswertung(bb[0], bb[1], bb[2], bb[3], bb[4])
    best_child = aa if auswertung_aa > auswertung_bb else bb
    return best_child

class Bot:
  def __init__(self, a, b, c, d, e):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e

class Evolution:
   def __init__(self, bot_list=bot_list, 
                auswertung_list=auswertung_list, 
                max_random_num=max_random_num, 
                num_bots=num_bots,
                generations=generations):
    self.bot_list = bot_list
    self.auswertung_list = auswertung_list
    self.max_random_num = max_random_num
    self.num_bots = 10**math.ceil(math.log10(num_bots))

    self.generations = generations
    generation = 0

    for i in range(num_bots):
       bot = Bot(random.randint(0, max_random_num), 
                 random.randint(0, max_random_num), 
                 random.randint(0, max_random_num), 
                 random.randint(0, max_random_num), 
                 random.randint(0, max_random_num))
       bot_list.append([bot.a, bot.b, bot.c, bot.d, bot.e])
    
    debug("Botlist:")
    for bot in bot_list:
       debug(bot)
    debug()

    for bot in bot_list:
       result = auswertung(bot[0], bot[1], bot[2], bot[3], bot[4])
       auswertung_list.append(result)
    
    debug("Auswertungen:")
    for i in auswertung_list:
        debug(i)
    debug()
    
    zipped = zip(auswertung_list, bot_list)
    sort = sorted(zipped, reverse=True)
    tuples = zip(*sort)

    auswertung_list, bot_list = [list(i) for i in tuples]
    best_bots.append([bot_list[0], auswertung_list[0] * -1, f"Gen: {generation}"])

    ten_perc = round(int(len(bot_list) * 0.1)) if round(int(
    len(bot_list) * 0.1)) != 0 and round(int(len(bot_list) * 0.1)) != 1 else 2 
    bot_list = bot_list[0:ten_perc]

    debug("10% that survive:")
    debug(bot_list)
    debug()

    auswertung_list = []

    for gen in range(0, generations):
        for i in range(0, length):
          arr1 = bot_list[i]
          arr2 = bot_list[(i + 1) % length]
          point = random.randint(0, 5)

          for j in range(0, length):
            if i == j:
                debug(f"Array {i} swap {j}: {25 * '-'}")
            else:
                arr2 = bot_list[j]
                swapped = swap(arr1, arr2, point)
                bot_list.append(swapped)
                debug(f"Array {i} swap {j}: {swapped}")
        
        for bot in bot_list:
            result = auswertung(bot[0], bot[1], bot[2], bot[3], bot[4])
            auswertung_list.append(result)
    
        debug()
        debug("Auswertungen:")
        for x in auswertung_list:
            debug(x)
    
        zipped = zip(auswertung_list, bot_list)
        sort = sorted(zipped, reverse=True)
        tuples = zip(*sort)

        auswertung_list, bot_list = [list(i) for i in tuples]
        best_bots.append([bot_list[0], auswertung_list[0] *-1, f"Gen: {gen + 1}"])

        ten_perc = round(int(len(bot_list) * 0.1)) if round(int(
        len(bot_list) * 0.1)) != 0 and round(int(len(bot_list) * 0.1)) != 1 else 2 
        bot_list = bot_list[0:ten_perc]
        
        debug()
        debug("10% that survive:")
        debug(bot_list)
        debug()

        print(f"Generation: {gen}\tFitness: {auswertung_list[0] * -1}\tBest: {best_bots[gen]}")
        auswertung_list = []

evolution = Evolution()
