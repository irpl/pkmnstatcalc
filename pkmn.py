def hp(p,i,e,l):
    BaseHP = getHP(p)
    IV = i
    EV = e
    Level = l
    hp = ((2 * BaseHP + IV + (EV / 4.0)) * Level / 100.0 + Level + 10)
    return hp

def statAtk(p,i,e,l,n):
    BaseAtk = getAtk(p)
    IV = i
    EV = e
    Level = l
    Nature = n
    stat = (((2 * BaseAtk + IV + (EV / 4.0)) * Level / 100.0 + 5) * float(natureMod('Attack',Nature)))
    return stat

def statDef(p,i,e,l,n):
    BaseDef = getDef(p)
    IV = i
    EV = e
    Level = l
    Nature = n
    stat = (((2 * BaseDef + IV + (EV / 4.0)) * Level / 100.0 + 5) * float(natureMod('Defense',Nature)))
    return stat

def statSpAtk(p,i,e,l,n):
    BaseSpAtk = getSpAtk(p)
    IV = i
    EV = e
    Level = l
    Nature = n
    stat = (((2 * BaseSpAtk + IV + (EV / 4.0)) * Level / 100.0 + 5) * float(natureMod('Sp. Attack',Nature)))
    return stat

def statSpDef(p,i,e,l,n):
    BaseSpDef = getSpDef(p)
    IV = i
    EV = e
    Level = l
    Nature = n
    stat = (((2 * BaseSpDef + IV + (EV / 4.0)) * Level / 100.0 + 5) * float(natureMod('Sp. Defense',Nature)))
    return stat

def statSpd(p,i,e,l,n):
    BaseSpd = getSpd(p)
    IV = i
    EV = e
    Level = l
    Nature = n
    stat = (((2 * BaseSpd + IV + (EV / 4.0)) * Level / 100.0 + 5) * float(natureMod('Speed',Nature)))
    return stat

def pkmn(p):
    db = open('pkmn_genVI.csv','r')        
    n = int(db.readline())
    for i in xrange(n):
        lst = db.readline().split(',')
        lst[0] = int(lst[0])
        for j in range(2,8):
            lst[j] = int(lst[j])
        while (p == lst[1]):
            return lst
    db.close()

def calcStat(p,hp_i,atk_i,def_i,spatk_i,spdef_i,spd_i,hp_e,atk_e,def_e,spatk_e,spdef_e,spd_e,l,n):
    return [hp(p,hp_i,hp_e,l),statAtk(p,atk_i,atk_e,l,n),statDef(p,def_i,def_e,l,n),statSpAtk(p,spatk_i,spatk_e,l,n),statSpDef(p,spdef_i,spdef_e,l,n),statSpd(p,spd_i,spd_e,l,n)]
    
def getHP(p):
    HP = pkmn(p)[2]
    return HP

def getAtk(p):
    Atk = pkmn(p)[3]
    return Atk

def getDef(p):
    Def = pkmn(p)[4]
    return Def

def getSpAtk(p):
    SpAtk = pkmn(p)[5]
    return SpAtk

def getSpDef(p):
    SpDef = pkmn(p)[6]
    return SpDef

def getSpd(p):
    Spd = pkmn(p)[7]
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
