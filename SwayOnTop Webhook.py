print("""

▄██████░██░██░██░▄████▄░██░░██░░░▄█████▄░██████▄░░░████████░▄█████▄░█████▄
██░░░░░░██░██░██░██░░██░██░░██░░░██░░░██░██░░░██░░░░░░██░░░░██░░░██░██░░██
▀█████▄░██░██░██░██░░██░▀████▀░░░██░░░██░██░░░██░░░░░░██░░░░██░░░██░█████▀
░░░░░██░██░██░██░██████░░░██░░░░░██░░░██░██░░░██░░░░░░██░░░░██░░░██░██░░░░
██████▀░▀██▀▀██▀░██░░██░░░██░░░░░▀█████▀░██░░░██░░░░░░██░░░░▀█████▀░██░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        the best discord webhook spammer you will ever need


""")
#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent.")