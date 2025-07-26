import requests
import os
import sys
import time
import json


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

       print("\n")
       print("=" * 30)
       print("Minecraft Java perfil")
       print(f"Name: {mcName}")
       print(f"Body URL: {mcBody}")
       print(f"Skin URL: {mcSkin}")
       print("=" * 30)
       print("\n")
       showInput()
    else:
       print("\n")
       print("=" * 30)
       print(" " * 5, "Failed user local")
       print("=" * 30)
       print("\n")
       showInput()


def showInput():
    edit = input("user-name: ")
    if not edit.startswith("exit"):
       getUser(edit)
    else:
       print("Success EXIT")
       sys.exit

if __name__ == "__main__":
   for i in range(101):
       bars = i // 2
       sys.stdout.write('\rloading data %d%%: %s' % (i, "#" * bars))
       sys.stdout.flush()
       time.sleep(0.1)
   print()
   print("Success")
   showInput()
