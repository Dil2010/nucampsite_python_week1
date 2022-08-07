"""
Python BattleGame by Dilan Udawattha
"""
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage=50

print("1)  Wizard")
print("2)  Elf")
print("3)  Human")

character = input("Choose your character: ")

while True:
    if character=="1":
        character = wizard
        my_hp=wizard_hp
        my_damage=wizard_damage
        print("You have chosen the character:"+character)
        print("Health:"+str(my_hp))
        print("Damage:"+str(my_damage)+"\n")
        break
        
    elif character=="2":
        character = elf
        my_hp=elf_hp
        my_damage=elf_damage
        print("You have chosen the character:"+character)
        print("Health:"+str(my_hp))
        print("Damage:"+str(my_damage)+"\n")
        break

    elif character=="3":
        character = human
        my_hp=human_hp
        my_damage=human_damage
        print("You have chosen the character:"+character)
        print("Health:"+str(my_hp))
        print("Damage:"+str(my_damage)+"\n")
        break

    else :
        print("Unkown Character:")
        print('Choose your character:')
        character=input()
        

while True:
    if dragon_hp>0 and my_hp>0:
        dragon_hp =dragon_hp- my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:"+str(dragon_hp)+"\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break
      
        my_hp=my_hp-dragon_damage
        print("The Dragon strikes back at", character)
        print("The", character,"'s hitpoints are now:"+str(my_hp)+"\n")
        if my_hp <= 0:
            print("The",character,"has lost the battle.")
            break
