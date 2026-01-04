import time
import random

def package_size():
    return random.randint(500, 1500)

def title():
    print("""
█████   █████    █████   █████
█    █  █    █   █   █   █
█    █  █    █   █   █   █████               Made by feva123
█    █  █    █   █   █       █
█████   █████    █████   █████
""")

title()

while True:
    ip_attack = input("Enter IP: ")
    if not ip_attack.isdigit():
        print("Please enter a valid IP")
    else:
        break

ip_port = int(input("Please enter a port, default 80: "))

for x in range(9999999999999999):
    size = package_size()
    print(f"Attacking {ip_attack} | Package sent {size} Kb")
    time.sleep(0.1)

