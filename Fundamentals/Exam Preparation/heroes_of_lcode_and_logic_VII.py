n = int(input())

hp_by_hero = {}
mp_by_hero = {}

MAX_HP = 100
MAX_MP = 200

for _ in range(n):

    hero = input()
    hero_args = hero.split()
    hero_name = hero_args[0]
    hp = int(hero_args[1])
    mp = int(hero_args[2])

    hp_by_hero[hero_name] = hp
    mp_by_hero[hero_name] = mp

while True:
    comm = input()
    command_args = comm.split(" - ")
    command = command_args[0]

    if command == "End":
        break

    hero_name = str(command_args[1])

    if command == "CastSpell":
        needed_mp = int(command_args[2])
        spell_name = command_args[3]

        if mp_by_hero[hero_name] >= needed_mp:
            mp_by_hero[hero_name] -= needed_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {mp_by_hero[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]

        hp_by_hero[hero_name] -= damage

        if hp_by_hero[hero_name] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hp_by_hero[hero_name]} HP left!")
        else:
            hp_by_hero.pop(hero_name)
            mp_by_hero.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(command_args[2])
        mana = MAX_MP - mp_by_hero[hero_name]

        mp_by_hero[hero_name] = min(MAX_MP, mp_by_hero[hero_name] + amount)
        print(f"{hero_name} recharged for {min(amount, mana)} MP!")

    elif command == "Heal":
        amount = int(command_args[2])
        heal = MAX_HP - hp_by_hero[hero_name]

        hp_by_hero[hero_name] = min(MAX_HP, hp_by_hero[hero_name] + amount)
        print(f"{hero_name} healed for {min(amount, heal)} HP!")

for hero_name in hp_by_hero.keys():
    print(hero_name)
    print(f"  HP: {hp_by_hero[hero_name]}")
    print(f"  MP: {mp_by_hero[hero_name]}")
