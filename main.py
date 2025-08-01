import requests
import os
import sys
import json
from colorama import Fore, Back, Style
from time import strftime, localtime, sleep


def getUser(name):
    api_url = f"https://japi.rest/minecraft/v1/username/{name}"

    response = requests.get(api_url)
    data = response.json()
    user = data.get("data", {})

    mcId = user.get("id")
    mcName = user.get("name")

    if mcId:
       mcList = f"https://mc-heads.net"
       mcBody = f"{mcList}/body/{mcId}"
       mcSkin = f"{mcList}/skin/{mcId}"

       print(f"{Fore.MAGENTA}\n")
       print("=" * 30)
       print("Minecraft Java perfil")
       print(f"Name: {mcName}")
       print(f"Body URL: {Fore.CYAN}{mcBody}{Fore.MAGENTA}")
       print(f"Skin URL: {Fore.CYAN}{mcSkin}{Fore.MAGENTA}")
       print("=" * 30)
       print("\n")
       showInput()
    else:
       print(f"{Fore.RED}\n")
       print("=" * 30)
       print(" " * 5, "Failed user local")
       print("=" * 30)
       print("\n")
       showInput()


def showInput():
    edit = input(f"{Fore.GREEN}{strftime('%H:%M.%S', localtime())} | user-name: ")
    if not edit.lower().startswith("exit"):
       getUser(edit)
    else:
       print(f"{Fore.YELLOW}Success EXIT{Style.RESET_ALL}")
       sys.exit

if __name__ == "__main__":
   for i in range(101):
       bars = i // 2
       sys.stdout.write('\rloading data %d%%: %s' % (i, "#" * bars))
       sys.stdout.flush()
       sleep(0.1)
   print()
   print(f"""{Fore.CYAN}
   
 ****     ****   ******                  ** 
/**/**   **/**  **////**                *** 
/**//** ** /** **    //        **    **//** 
/** //***  /**/**             /**   /** /** 
/**  //*   /**/**             //** /**  /** 
/**   /    /**//**    **       //****   /** 
/**        /** //******         //**    ****
//         //   //////           //    //// 
            {Fore.YELLOW}/BY YURIZZJAXX:::...
   """)
   showInput()
