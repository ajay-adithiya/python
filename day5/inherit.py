class GrandFather():
    def gfproperty(self):
        print("Grand Father property")
class Father(GrandFather):       # single
    def fproperty(self):
        print("Father property")
class Mother():
    def mproperty(self):
        print("mother property")
class son(Father , Mother):     # multilevel
    def sproperty(self):
        print("Son property")
class son2(GrandFather,Mother):     # multiple
    def s2property(self):
        print("ancient property")
class daughter(GrandFather):   # hierarchial
    def famproperty(self):
        print("family property")
class child(Father,Mother):    # hybrid
    def cproperty(self):
        print("All comes to child")

s1 = son()
s1.gfproperty()
s1.fproperty()
s1.sproperty()
s1.mproperty()
s2 = son2()
s2.s2property()
d = daughter()
d.famproperty()
c = child()
c.cproperty()