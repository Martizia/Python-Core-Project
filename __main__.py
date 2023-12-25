from Bot import Bot
from dashtable import data2rst

if __name__ == "__main__":
    bot = Bot()
    while True:
        table = [["1. Contacts", "2. Notes", "3. Game", "4. Help", "5. Exit"]]
        print(data2rst(table))
        action = int(input('What action do you want to choose?\n'))
        if action in [1, 2, 3]:
            bot.run(action)
        if action == 5:
            break
