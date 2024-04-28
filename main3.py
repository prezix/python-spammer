# Import necessary libraries
import pyautogui
import time
import threading
import win32gui
import win32con



# Function to bring Telegram window to the foreground

def bring_telegram_to_foreground():
    telegram_handle = 0
    # Loop until Telegram window is found or maximum retries reached
    max_retries = 5  # Adjust as needed
    retry_count = 0
    while telegram_handle == 0 and retry_count < max_retries:
        # Find the Telegram window
        telegram_handle = win32gui.FindWindow(None, "название процесса")
        # If not found, wait for a moment before trying again
        if telegram_handle == 0:
            print("Telegram window not found. Retrying...")
            time.sleep(1)
            retry_count += 1

    # If Telegram window is found, bring it to the foreground
    if telegram_handle != 0:
        # Check if the Telegram window is currently active
        if win32gui.GetForegroundWindow() == telegram_handle:
            win32gui.ShowWindow(telegram_handle, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(telegram_handle)
        else:
            print("Telegram window is not currently active. Please switch to Telegram.")
    else:
        print("Telegram window not found or not open.")

    # If Telegram window is found, bring it to the foreground
    if telegram_handle != 0:
        win32gui.ShowWindow(telegram_handle, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(telegram_handle)
    else:
        print("Telegram window not found or not open.")

    # Bring the Telegram window to the foreground
    win32gui.ShowWindow(telegram_handle, win32con.SW_NORMAL)
    win32gui.SetForegroundWindow(telegram_handle)



# Функция для чтения одной строки из текстового файла, вставки её, ввода "rodinabox", нажатия Enter и удаления строки
def read_paste_and_delete_code(file_path):
    with open(file_path, 'r+') as file:
        # Считать одну строку из файла
        lines = file.readlines()
        # Проверить, что список строк не пуст
        if lines:
            # Получить первую строку и удалить её из списка
            code = lines[0].strip()
            del lines[0]
            # Перезаписать оставшиеся строки в файл
            file.seek(0)
            file.writelines(lines)
            file.truncate()
            # Проверить, что строка не пустая
            if code:
                # Принести окно Telegram на передний план
                bring_telegram_to_foreground()
                # Подождать некоторое время перед вставкой, чтобы окно Telegram было в фокусе
                time.sleep(1)
                # Ввести "rodinabox"
                pyautogui.typewrite("rodinabox ")
                time.sleep(1)
                # Симулировать ввод кода
                pyautogui.typewrite(code)
                # Нажать Enter
                pyautogui.press('enter')


# Function to run the thread
def run_thread(file_path):
    while True:
        # Read, paste, and delete code
        read_paste_and_delete_code(file_path)
        # Wait for a moment before proceeding to the next line
        time.sleep(1)

if __name__ == "__main__":
    # File path containing the codes
    file_path = "code_examples.txt"  # Update with your file path
    # Specify the number of threads to start
    num_threads = 1  # Adjust as needed
    # Create and start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=run_thread, args=(file_path,))
        thread.start()
        threads.append(thread)
    # Join threads
    for thread in threads:
        thread.join()
