import os
import sys
import time
import mslxl

def get_download_path(filename):
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            download_dir = winreg.QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    else:
        android_download = "/storage/emulated/0/Download"
        if os.path.exists(android_download):
            download_dir = android_download
        else:
            download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    return os.path.join(download_dir, filename)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 45)
    print("mslxl")
    print("=" * 10)
    print("Создано mt.co / szx.pythonanywhere.com")
    print("=" * 10)
    print("Доступные действия:")
    print(" 1 — Запаковать текст в .mslxl (в Загрузки)")
    print(" 2 — Распаковать и прочитать файл из Загрузок")
    print(" 3 — Выйти из программы")
    print("=" * 45)

    mode = input("Выбери режим (1, 2 или 3): ").strip()
    print("-" * 45)

    if mode == "1":
        filename = input("Придумай имя для файла (без расширения): ").strip()
        if not filename:
            print("! Имя файла не может быть пустым!")
            time.sleep(2)
            continue

        if not filename.endswith(".mslxl"):
            filename += ".mslxl"

        text_content = input("Введи или вставь текст, который нужно сжать: ")
        full_path = get_download_path(filename)

        try:
            mszx.compress(text_content, full_path)
            print(f":) Всё готово! Текст успешно упакован.")
            print(f"? Файл лежит тут: {full_path}")
        except Exception as e:
            print(f"!!! Не удалось сохранить файл: {e}")

        input("Нажми Enter, чтобы вернуться в главное меню...")

    elif mode == "2":
        filename = input("Введи имя файла из Загрузок (например, secret.mslxl): ").strip()
        if not filename:
            print("! Ты не ввёл имя файла!")
            time.sleep(2)
            continue

        if not filename.endswith(".mslxl"):
            filename += ".mslxl"

        full_path = get_download_path(filename)

        if not os.path.exists(full_path):
            print(f"!! Файл не найден. Проверь, лежит ли он в Загрузках под именем {filename}")
        else:
            try:
                decrypted_text = mszx.decompress(full_path)
                print("" + "="*12 + " РАСШИФРОВАННЫЙ ТЕКСТ " + "="*12)
                print(decrypted_text)
                print("="*45 + "")
            except Exception as e:
                print(f"!!! Ошибка чтения структуры .mslxl: {e}")

        input("Нажми Enter, чтобы вернуться в главное меню...")

    elif mode == "3":
        print(":) Спасибо за использование формата .mslxl! До встречи.")
        time.sleep(1.5)
        break

    else:
        print("!!! Неверный выбор. Пожалуйста, введи 1, 2 или 3.")
        time.sleep(2)
