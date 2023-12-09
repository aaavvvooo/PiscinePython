from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.hair = "zibil"
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
print(1)
Joffrey.hairs("light")
print(2)
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)