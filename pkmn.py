def hp(p,i,e,l,r):
    BaseHP = getHP(p,r)
    IV = i
    EV = e
    Level = l
    hp = ((2 * BaseHP + IV + (EV / 4.0)) * Level / 100.0 + Level + 10)
    return hp

def statAtk(p,i,e,l,n,r):
    BaseAtk = getAtk(p,r)
    IV = i
    EV = e
    Level = l
    Nature = n
    Atk = (((2 * BaseAtk + IV + (EV / 4.0)) * Level / 100.0 + 5) * natureMod('Attack',Nature))
    return Atk

def statDef(p,i,e,l,n,r):
    BaseDef = getDef(p,r)
    IV = i
    EV = e
    Level = l
    Nature = n
    Def = (((2 * BaseDef + IV + (EV / 4.0)) * Level / 100.0 + 5) * natureMod('Defense',Nature))
    return Def

def statSpAtk(p,i,e,l,n,r):
    BaseSpAtk = getSpAtk(p,r)
    IV = i
    EV = e
    Level = l
    Nature = n
    SpAtk = (((2 * BaseSpAtk + IV + (EV / 4.0)) * Level / 100.0 + 5) * natureMod('Sp. Attack',Nature))
    return SpAtk

def statSpDef(p,i,e,l,n,r):
    BaseSpDef = getSpDef(p,r)
    IV = i
    EV = e
    Level = l
    Nature = n
    SpDef = (((2 * BaseSpDef + IV + (EV / 4.0)) * Level / 100.0 + 5) * natureMod('Sp. Defense',Nature))
    return SpDef

def statSpd(p,i,e,l,n,r):
    BaseSpd = getSpd(p,r)
    IV = i
    EV = e
    Level = l
    Nature = n
    Spd = (((2 * BaseSpd + IV + (EV / 4.0)) * Level / 100.0 + 5) * natureMod('Speed',Nature))
    return Spd

def pkmn(p,r):
    if (r == 3):
        db = open('pkmn_genVI.csv','r')
    elif (r == 2):
        db = open('pkmn_genII-V.csv','r')
    elif (r == 1):
        db = open('pkmn_genI.csv','r')
    n = int(db.readline())
    for i in xrange(n):
        lst = db.readline().split(',')
        lst[0] = int(lst[0])
        for j in range(2,8):
            lst[j] = int(lst[j])
        while (p == lst[1]):
            return lst
    db.close()

def calcStat(p,hp_i,atk_i,def_i,spatk_i,spdef_i,spd_i,hp_e,atk_e,def_e,spatk_e,spdef_e,spd_e,l,n,r):
    return [hp(p,hp_i,hp_e,l,r),
            statAtk(p,atk_i,atk_e,l,n,r),
            statDef(p,def_i,def_e,l,n,r),
            statSpAtk(p,spatk_i,spatk_e,l,n,r),
            statSpDef(p,spdef_i,spdef_e,l,n,r),
            statSpd(p,spd_i,spd_e,l,n,r)]
    
def getHP(p,r):
    HP = pkmn(p,r)[2]
    return HP

def getAtk(p,r):
    Atk = pkmn(p,r)[3]
    return Atk

def getDef(p,r):
    Def = pkmn(p,r)[4]
    return Def

def getSpAtk(p,r):
    SpAtk = pkmn(p,r)[5]
    return SpAtk

def getSpDef(p,r):
    SpDef = pkmn(p,r)[6]
    return SpDef

def getSpd(p,r):
    Spd = pkmn(p,r)[7]
    return Spd
               
def nature(nat):
    db = open('nature.csv','r')
    n = int(db.readline())
    for i in xrange(n):
        lne = db.readline().split(',')
        while (nat == lne[0]):
            lst = [j.rstrip() for j in lne]
            return lst

def natureMod(s,nat):
    if (s == nature(nat)[1]):
        mod = 1.1
    elif (s == nature(nat)[2]):
        mod = 0.9
    else:
        mod = 1.0
    return mod
