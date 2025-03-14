import os
import sys
import time
import datetime
import platform
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from DemoPackage.furtune_cookie import dev_fortune_cookie
from DemoPackage.generate_emoji import generate_emoji  
from DemoPackage.owl_banner import gl_banner



def main():
   while True:

    choice = input("🦉 Choose Your Option (1: Owl Banner, 2: Fortune Cookie, 3: Generate Emoji, 4: Abort): ") or "1"
    
    try:
        choice = int(choice)
    except ValueError:
        print("[ERROR] Invalid input")
        choice = 1

    
    if choice == 4:
        print("*** PROGRAM TERMINATED ***")
        break  

    
    match choice:
        case 1:
            # Owl Banner
            para = int(input("🦉 Choose Your Style (0: Style A, 1: Style B, 2: Style C): ") or "0")
            gl_banner(para)

        case 2:
            # Fortune Cookie
            category = input("🔮 Choose fortune category (general, bug, debug, success): ") or "general"
            print(dev_fortune_cookie(category))

        case 3:
            # Generate Emoji
            emotion = input("😊 Enter an emotion (laugh, cry, love, etc.): ") or "happy"
            print(f"Your emoji: {generate_emoji(emotion)}")

        case _:
            print("[Invalid option] Please enter 1, 2, 3, or 4.")
    

if __name__ == "__main__":
    main()
