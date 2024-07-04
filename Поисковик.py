import webbrowser
import time

delay = 1

print('Поисковая система в пайтон')
time.sleep(delay)

url_input = str(input('Введите https адрес сайта: '))
print('Идет запрос...')
time.sleep(delay)

webbrowser.open(url_input)
