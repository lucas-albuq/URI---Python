n = int(input())
for x in range(1, n + 1):
    sheldon, raj = input().split()
    if sheldon == raj:
        print(f'Caso #{x}: De novo!')
    elif raj == 'lagarto' and sheldon == 'Spock' or raj == 'lagarto' and sheldon == 'papel':
        print(f'Caso #{x}: Raj trapaceou!')
    elif raj == 'Spock' and sheldon == 'tesoura' or raj == 'Spock' and sheldon == 'pedra':
        print(f'Caso #{x}: Raj trapaceou!')
    elif raj == 'tesoura' and sheldon == 'papel' or raj == 'tesoura' and sheldon == 'lagarto':
        print(f'Caso #{x}: Raj trapaceou!')
    elif raj == 'papel' and sheldon == 'pedra' or raj == 'papel' and sheldon == 'Spock':
        print(f'Caso #{x}: Raj trapaceou!')
    elif raj == 'pedra' and sheldon == 'lagarto' or raj == 'pedra' and sheldon == 'tesoura':
        print(f'Caso #{x}: Raj trapaceou!')
    else:
        print(f'Caso #{x}: Bazinga!')