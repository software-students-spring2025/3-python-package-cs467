import os
import time
import datetime
import platform
from DemoPackage.furtune_cookie import dev_fortune_cookie
from DemoPackage.generate_emoji import generate_emoji  # 新增导入


def gl_banner():
    print("\n")
    seed = "490000514095612094711092719200618300609300923300527300409400454500"
    length = len(seed)

    for i in range(11):
        
        start_index = length - 6 * (i + 1)
        end_index = length - 6 * i
        seed_cup = seed[start_index:end_index]

        sub_seed = int(seed_cup)
      
        for _ in range(3):
            emp = sub_seed % 10   
            sub_seed //= 10       

            print(" " * emp, end="")  

            star = sub_seed % 10    
            sub_seed //= 10

            print("*" * star, end="") 

        time.sleep(0.05)
        print()  
    
    projectName = "Project Name"
    db_name = "None"
    environment = "Testing"
    version = "1.0"
    extra_info = "Web Crawlers"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os_info = platform.platform()

    banner = f"""

-- PROGRAM INITIALIZATION --

   PROJECT      : {projectName}
   DB NAME      : {db_name}
   ENVIRONMENT  : {environment}
   VERSION      : {version}
   DATE & TIME  : {current_time}
   OS           : {os_info}
   INFO         : {extra_info}

"""
    print(banner.strip())


def main():
    gl_banner()

    # Fortune Cookie
    category = input("🔮 Choose fortune category (general, bug, debug, success): ") or "general"
    print(dev_fortune_cookie(category))

    # Generate Emoji
    emotion = input("😊 Enter an emotion (laugh, cry, love, etc.): ") or "happy"
    print(f"Your emoji: {generate_emoji(emotion)}")  # 调用 generate_emoji() 方法

if __name__ == "__main__":
    main()
