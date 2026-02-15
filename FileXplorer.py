import os
import string

def get_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

def list_directory_contents(path):
    try:
        print(f"\nДиск {path}")
        items = os.listdir(path)
        
        if not items:
            print("  [Пусто]")
            return

        for index, item in enumerate(items, 1):
            full_path = os.path.join(path, item)
            item_type = "папка" if os.path.isdir(full_path) else "файл"
            print(f"{index} {item_type}: {item}")
            
    except PermissionError:
        print("Ошибка: Нет доступа к этому диску (требуются права администратора).")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    drives = get_drives()
    
    if not drives:
        print("Диски не найдены.")
        return

    print("Выберите диск:")
    for i, drive in enumerate(drives, 1):
        print(f"{i} {drive}")

    try:
        choice = int(input("Вариант: "))
        if 1 <= choice <= len(drives):
            selected_drive = drives[choice - 1]
            list_directory_contents(selected_drive)
        else:
            print("Неверный номер варианта.")
    except ValueError:
        print("Пожалуйста, введите число.")

main()