from colorama import Fore
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
ascii_sword=f'''
        {colors[-2]}
                __
               || \\ 
               ||{colors[5]}○{colors[-2]} \\
               ||  |
               ||  |
               ||  |
               ||{colors[5]}_/{colors[-2]}|
               ||{colors[5]}_/{colors[-2]}|
               ||{colors[5]}_/{colors[-2]}|
               ||  |
               ||  |
               ||  |
               ||  |
               ||  |
               ||  |
               ||  |
               || {colors[5]}-{colors[-2]}|
               || {colors[5]}-{colors[-2]}|
               || {colors[5]}-{colors[-2]}|
               ||  |
               ||  |
               ||  |
               \___/
               |{colors[5]}___{colors[-2]}|
               \___/
               |{colors[5]}__{colors[-2]}||
               |{colors[5]}__{colors[-2]}||
               |{colors[5]}__{colors[-2]}||
               |{colors[5]}__{colors[-2]}||
               |{colors[5]}__{colors[-2]}||
               |{colors[5]}__{colors[-2]}||
               \__//
               
      '''
print(f'{colors[1]}{ascii_sword}')