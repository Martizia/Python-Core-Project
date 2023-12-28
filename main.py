from Bot import Bot
from dashtable import data2rst
from help import help

if __name__ == "__main__":
    bot = Bot()
    while True:
        table = [["1. Contacts", "2. Notes", "3. Help", "4. Exit"]]
        print(data2rst(table))
        action = int(input('What action do you want to choose?\n'))
        if action in [1, 2]:
            bot.run(action)
        elif action == 3:
            help()
        elif action == 4:
            break
