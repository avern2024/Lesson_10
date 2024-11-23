# Импорты необходимых модулей и функций
from time import sleep, time
from threading import Thread


# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


# Взятие текущего времени
start_time = time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time()

# Вывод разницы начала и конца работы функций
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Взятие текущего времени
start_time_threads = time()

# Создание и запуск потоков с аргументами из задачи
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in thread_args:
    thread = Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Остановка основного потока до завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени
end_time_threads = time()

# Вывод разницы начала и конца работы потоков
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
