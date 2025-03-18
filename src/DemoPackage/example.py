import os
import io
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from DemoPackage.furtune_cookie import dev_fortune_cookie
from DemoPackage.generate_emoji import generate_emoji  
from DemoPackage.owl_banner import gl_banner
from DemoPackage.daily_planner import daily_planner
from DemoPackage.password_strength import password_strength

print('\n\033[33mExample Usage of DemoPackage\033[0m')

# Owl Banner
print('\n\033[33m<<< Owl Banner >>>\033[0m')
print('\033[33mDisplaying the owl banner in style A...\033[0m')
gl_banner(1)

# Fortune Cookie
print('\n\033[33m<<< Fortune Cookie >>>\033[0m')
print('\033[33mGetting a random furtune cookie...\033[0m')
print(dev_fortune_cookie('general'))

# Generate Emoji
print('\n\033[33m<<< Generate Emoji >>>\033[0m')
print('\033[33mGenerating a love emoji...\033[0m')
print('Your emoji:', generate_emoji('love'))

# Daily Planner
print('\n\033[33m<<< Daily Planner >>>\033[0m')
print('\033[33mCreating a daily planner for foobar...\033[0m')
print('\033[33m(Grocery Shopping: medium priority, Go to gym: low priority, Study for midterm: high priority)\033[0m')
example_input = ['Grocery Shopping\n', '2\n', 'Go to gym\n', '3\n', 'Study for midterm\n', '1\n', 'done\n']
sys.stdin = io.StringIO("".join(example_input))
print(daily_planner('foobar'))
sys.stdin = sys.__stdin__

# Password Strength Checker
print('\n\033[33m<<< Password Strength Checker >>>\033[0m')
print('\033[33mEvaluating the strength for this password \'ABCdef&123456!\'...\033[0m')
print(password_strength('ABCdef&123456!'))
print()