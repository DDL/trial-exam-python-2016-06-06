pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

def get_pirates_with_wooden_legs(list_of_pirates):
    list_of_pirates_with_wooden_leg = []
    for pirate in list_of_pirates:
        if pirate['has_wooden_leg'] is True and pirate['gold'] > 15:
            list_of_pirates_with_wooden_leg.append(pirate['Name'])
    return list_of_pirates_with_wooden_leg

print(get_pirates_with_wooden_legs(pirates))
