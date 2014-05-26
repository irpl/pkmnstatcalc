from Tkinter import *
from ttk import *
from pkmn import *

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.pkmnthings()
        self.statthings()
        self.calcthings()

    def pkmnthings(self):
        self.hmm = Label(self, text = "pkmn", foreground = "#696969")
        self.hmm.grid(row = 0, column = 0, pady = (0,12), sticky = NW)

        self.pkmnlabel = Label(self, text = "Pokemon: ")
        self.pkmnlabel.grid(row = 1, column = 0, sticky = W, padx = (10,0))
        
        self.pkmn = Entry(self)
        self.pkmn.grid(row = 1, column = 0, padx = (70,20))

        self.lvllabel = Label(self, text = "Level: ")
        self.lvllabel.grid(row = 2, column = 0, sticky = W, padx = (10,0))
        
        self.lvl = Entry(self)
        self.lvl.grid(row = 2, column = 0, padx = (70,20))

        self.natlabel = Label(self,text = "Nature: ")
        self.natlabel.grid(row = 3, column = 0, sticky = W, padx = (10,0), pady = (0,12))
        
        self.nat = Entry(self)
        self.nat.grid(row = 3, column = 0, padx = (70,20), pady = (0,12))

    def statthings(self):
        self.hmm2 = Label(self, text = "calc", foreground = "#696969")
        self.hmm2.grid(row = 4, column = 1, sticky = NW, padx = (22,0), pady = (0,12))

        self.hplabel = Label(self, text = "HP")
        self.hplabel.grid(row = 5, column = 1, padx = (0,10), pady = (0,5))
        
        self.hp = Text(self, width = 3, height = 1)
        self.hp.grid(row = 5, column = 1, padx = (50,0), pady = (0,5))
        
        self.spatklabel = Label(self, text = "SpAtk")
        self.spatklabel.grid(row = 5, column = 2, padx = (0,70), pady = (0,5))

        self.spatk = Text(self, width = 3, height = 1)
        self.spatk.grid(row = 5, column = 2, padx = (0,0), pady = (0,5))

        self.atklabel = Label(self, text = "Atk")
        self.atklabel.grid(row = 6, column = 1, padx = (0,10), pady = (0,5))
        
        self.atk = Text(self, width = 3, height = 1)
        self.atk.grid(row = 6, column = 1, padx = (50,0), pady = (0,5))
        
        self.spdeflabel = Label(self, text = "SpDef")
        self.spdeflabel.grid(row = 6, column = 2, padx = (0,70), pady = (0,5))

        self.spdef = Text(self, width = 3, height = 1)
        self.spdef.grid(row = 6, column = 2, padx = (0,0), pady = (0,5))

        self.deflabel = Label(self, text = "Def")
        self.deflabel.grid(row = 7, column = 1, padx = (0,10))
        
        self.defn = Text(self, width = 3, height = 1)
        self.defn.grid(row = 7, column = 1, padx = (50,0))
        
        self.spdlabel = Label(self, text = "Spd")
        self.spdlabel.grid(row = 7, column = 2, padx = (0,70))

        self.spd = Text(self, width = 3, height = 1)
        self.spd.grid(row = 7, column = 2, padx = (0,))

    def calcthings(self):
        self.hmm1 = Label(self,text = "stat", foreground = "#696969")
        self.hmm1.grid(row = 0, column = 1, sticky = NW, padx =(22,0), pady = (0,0))

        self.ivlabel = Label(self,text = "IV:")
        self.ivlabel.grid(row = 0, column = 1, sticky = W, padx =(22,0), pady = (18,0))

        self.hpivlabel = Label(self,text = "HP")
        self.hpivlabel.grid(row = 1, column = 1, padx = (0,10))

        self.hpiv = Text(self, width = 3, height = 1)
        self.hpiv.grid(row = 1, column = 1, padx = (50,0))

        self.atkivlabel = Label(self,text = "Atk")
        self.atkivlabel.grid(row = 2, column = 1, padx = (0,10))

        self.atkiv = Text(self, width = 3, height = 1)
        self.atkiv.grid(row = 2, column = 1, padx = (50,0))

        self.defivlabel = Label(self,text = "Def")
        self.defivlabel.grid(row = 3, column = 1, padx = (0,10), pady = (0,12))

        self.defiv = Text(self, width = 3, height = 1)
        self.defiv.grid(row = 3, column = 1, padx = (50,0), pady = (0,12))

        self.spatkivlabel = Label(self,text = "SpAtk")
        self.spatkivlabel.grid(row = 1, column = 2, padx = (0,70))

        self.spatkiv = Text(self, width = 3, height = 1)
        self.spatkiv.grid(row = 1, column = 2, padx = (0,0))

        self.spdefivlabel = Label(self,text = "SpDef")
        self.spdefivlabel.grid(row = 2, column = 2, padx = (0,70))

        self.spdefiv = Text(self, width = 3, height = 1)
        self.spdefiv.grid(row = 2, column = 2, padx = (0,0))

        self.spdivlabel = Label(self,text = "Spd")
        self.spdivlabel.grid(row = 3, column = 2, padx = (0,70), pady = (0,12))

        self.spdiv = Text(self, width = 3, height = 1)
        self.spdiv.grid(row = 3, column = 2, padx = (0,0), pady = (0,12))

        self.evlabel = Label(self,text = "EV:")
        self.evlabel.grid(row = 0, column = 3, sticky = W, padx =(22,0), pady = (18,0))

        self.hpevlabel = Label(self,text = "HP")
        self.hpevlabel.grid(row = 1, column = 3, padx = (0,10))

        self.hpev = Text(self, width = 3, height = 1)
        self.hpev.grid(row = 1, column = 3, padx = (50,0))

        self.atkevlabel = Label(self,text = "Atk")
        self.atkevlabel.grid(row = 2, column = 3, padx = (0,10))

        self.atkev = Text(self, width = 3, height = 1)
        self.atkev.grid(row = 2, column = 3, padx = (50,0))

        self.defevlabel = Label(self,text = "Def")
        self.defevlabel.grid(row = 3, column = 3, padx = (0,10), pady = (0,12))

        self.defev = Text(self, width = 3, height = 1)
        self.defev.grid(row = 3, column = 3, padx = (50,0), pady = (0,12))

        self.spatkevlabel = Label(self,text = "SpAtk")
        self.spatkevlabel.grid(row = 1, column = 4, padx = (0,70))

        self.spatkev = Text(self, width = 3, height = 1)
        self.spatkev.grid(row = 1, column = 4, padx = (0,0))

        self.spdefevlabel = Label(self,text = "SpDef")
        self.spdefevlabel.grid(row = 2, column = 4, padx = (0,70))

        self.spdefev = Text(self, width = 3, height = 1)
        self.spdefev.grid(row = 2, column = 4, padx = (0,0))

        self.spdevlabel = Label(self,text = "Spd")
        self.spdevlabel.grid(row = 3, column = 4, padx = (0,70), pady = (0,12))

        self.spdev = Text(self, width = 3, height = 1)
        self.spdev.grid(row = 3, column = 4, padx = (0,0), pady = (0,12))        

        self.calc = Button(self, text = "calc", command=self.pull)
        self.calc.grid(row = 6, column = 3, sticky = S)

        self.reset = Button(self, text = "reset", command=self.reset)
        self.reset.grid(row = 7, column = 3, sticky = S)

        self.genI = Radiobutton(self, text = "Gen I", value = 1, variable = var)
        self.genI.grid(row = 5, column = 0, sticky = W, padx = (100,0))

        self.genII_V = Radiobutton(self, text = "Gen II-V", value = 2, variable = var)
        self.genII_V.grid(row = 6, column = 0, sticky = W, padx = (100,0))

        self.genVI = Radiobutton(self, text = "Gen VI", value = 3, variable = var)
        self.genVI.grid(row = 7, column = 0, sticky = W, padx = (100,0))
        
        self.hpiv.bind("<Tab>", self.focus_next_window)
        self.atkiv.bind("<Tab>", self.focus_next_window)
        self.defiv.bind("<Tab>", self.focus_next_window)
        self.spatkiv.bind("<Tab>", self.focus_next_window)
        self.spdefiv.bind("<Tab>", self.focus_next_window)
        self.spdiv.bind("<Tab>", self.focus_next_window)
        self.hpev.bind("<Tab>", self.focus_next_window)
        self.atkev.bind("<Tab>", self.focus_next_window)
        self.defev.bind("<Tab>", self.focus_next_window)
        self.spatkev.bind("<Tab>", self.focus_next_window)
        self.spdefev.bind("<Tab>", self.focus_next_window)

##        self.hpiv.insert('1.0', '9')
##        self.atkiv.insert('1.0', '24')
##        self.defiv.insert('1.0', '30')
##        self.spatkiv.insert('1.0', '27')
##        self.spdefiv.insert('1.0', '24')
##        self.spdiv.insert('1.0', '1')
##        self.hpev.insert('1.0', '18')
##        self.atkev.insert('1.0', '168')
##        self.defev.insert('1.0', '86')
##        self.spatkev.insert('1.0', '49')
##        self.spdefev.insert('1.0', '14')
##        self.spdev.insert('1.0', '136')
        
    def pull(self):
        self.hp.delete('0.0','end')
        self.atk.delete('0.0','end')
        self.defn.delete('0.0','end')
        self.spatk.delete('0.0','end')
        self.spdef.delete('0.0','end')
        self.spd.delete('0.0','end')
        p = self.pkmn.get()
        l = int(self.lvl.get())
        n = self.nat.get()
        if (self.hpiv.get('1.0','end') == u'\n'):
            hp_i = 0
        else:
            hp_i = int(self.hpiv.get('1.0','end'))
        if (self.atkiv.get('1.0','end') == u'\n'):
            atk_i = 0
        else:
            atk_i = int(self.atkiv.get('1.0','end'))
        if (self.defiv.get('1.0','end') == u'\n'):
            def_i = 0
        else:
            def_i = int(self.defiv.get('1.0','end'))
        if (self.spatkiv.get('1.0','end') == u'\n'):
            spatk_i = 0
        else:
            spatk_i = int(self.spatkiv.get('1.0','end'))
        if (self.spdefiv.get('1.0','end') == u'\n'):
            spdef_i = 0
        else:
            spdef_i = int(self.spdefiv.get('1.0','end'))
        if (self.spdiv.get('1.0','end') == u'\n'):
            spd_i = 0
        else:
            spd_i = int(self.spdiv.get('1.0','end'))
        if (self.hpev.get('1.0','end') == u'\n'):
            hp_e = 0
        else:
            hp_e = int(self.hpev.get('1.0','end'))
        if (self.atkev.get('1.0','end') == u'\n'):
            atk_e = 0
        else:
            atk_e = int(self.atkev.get('1.0','end'))
        if (self.defev.get('1.0','end') == u'\n'):
            def_e = 0
        else:
            def_e = int(self.defev.get('1.0','end'))
        if (self.spatkev.get('1.0','end') == u'\n'):
            spatk_e = 0
        else:
            spatk_e = int(self.spatkev.get('1.0','end'))
        if (self.spdefev.get('1.0','end') == u'\n'):
            spdef_e = 0
        else:
            spdef_e = int(self.spdefev.get('1.0','end'))
        if (self.spdev.get('1.0','end') == u'\n'):
            spd_e = 0
        else:
            spd_e = int(self.spdev.get('1.0','end'))
        r = var.get()
        stat = calcStat(p,hp_i,atk_i,def_i,spatk_i,spdef_i,spd_i,hp_e,atk_e,def_e,spatk_e,spdef_e,spd_e,l,n,r)
        self.hp.insert('1.0',int(stat[0]))
        self.atk.insert('1.0',int(stat[1]))
        self.defn.insert('1.0',int(stat[2]))
        self.spatk.insert('1.0',int(stat[3]))
        self.spdef.insert('1.0',int(stat[4]))
        self.spd.insert('1.0',int(stat[5]))
        print pkmn(p,r)
        print stat

    def reset(self):
        self.pkmn.delete(0,END)
        self.lvl.delete(0,END)
        self.nat.delete(0,END)
        self.hpiv.delete('0.0','end')
        self.atkiv.delete('0.0','end')
        self.defiv.delete('0.0','end')
        self.spatkiv.delete('0.0','end')
        self.spdefiv.delete('0.0','end')
        self.spdiv.delete('0.0','end')
        self.hpev.delete('0.0','end')
        self.atkev.delete('0.0','end')
        self.defev.delete('0.0','end')
        self.spatkev.delete('0.0','end')
        self.spdefev.delete('0.0','end')
        self.spdev.delete('0.0','end')
        self.hp.delete('0.0','end')
        self.atk.delete('0.0','end')
        self.defn.delete('0.0','end')
        self.spatk.delete('0.0','end')
        self.spdef.delete('0.0','end')
        self.spd.delete('0.0','end')

    def focus_next_window(self,event):
        event.widget.tk_focusNext().focus()
        return("break")

root = Tk()
var = IntVar()
root.title("pkmnstatcalc")
root.geometry("590x240")
root.resizable(False,False)
app = Application(root)
root.mainloop()
