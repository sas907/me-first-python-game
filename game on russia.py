import sys
import time

while True:
    user_input = input("Введите команду (quest, quit, menu): ").strip().lower()
    
    if user_input == "quest":
        print("Для начала квеста введите 'start'")
        quest_input = input("Введите команду: ").strip().lower()
        if quest_input == "start":
            print("Квест начался!")
            # Здесь можно добавить логику квеста
        else:
            print("Неверная команда для квеста!")
    
    elif user_input == "quit":
        print("Выход из игры...")
        time.sleep(2)
        sys.exit()
    
    elif user_input == "menu":
        print("Доступные команды: quest, quit, menu")
    
    else:
        print("Неизвестная команда! Попробуйте снова.")
