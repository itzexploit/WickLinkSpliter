from urllib.parse import urlparse
from colorama import Fore , init
from os import system , name
from pystyle import Colorate , Colors

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

init()

bann = '''                                                                       
        _                    _        _               _                _                  
        (_|   |   |_/o       | |    \_|_)  o          | |      ()      | | o               
        |   |   |      __  | |      |        _  _   | |      /\   _  | |   _|_  _   ,_   
        |   |   |  |  /    |/_)    _|    |  / |/ |  |/_)    /  \|/ \_|/  |  |  |/  /  |  
            \_/ \_/   |_/\___/| \_/  (/\___/|_/  |  |_/| \_/  /(__/|__/ |__/|_/|_/|__/   |_/
                                                                /|                        
                                                                \|                                                                                                                                                            
                             Created By John Wick Team Pytho Learn                        
'''

print(Colorate.Horizontal(Colors.red_to_blue,bann,2))

url = input(f'\n   {cyan}URL {red}:{green} ')

parsed_url = urlparse(url)
target = parsed_url.netloc

print(f'\n   {blue}Url {yellow}Splited {red}:{green} {target}')
