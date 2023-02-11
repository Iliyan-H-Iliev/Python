electrons = int(input())
result = []
position_atom_shel = 1

while electrons > 0:
    electrons_in_atom_shel = 2 * (position_atom_shel**2)
    result.append(min(electrons_in_atom_shel, electrons))
    electrons -= electrons_in_atom_shel
    position_atom_shel += 1

print(result)