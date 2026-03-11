class people:

    def __init__(self, name, physical_hp, ishappy):
        self.name = name
        self.physical_hp = physical_hp
        self.ishappy = ishappy
    def xar(self):
        print(self.name, self.physical_hp, self.ishappy)
people1 = people("Иван", 12, True)
people1.xar()
