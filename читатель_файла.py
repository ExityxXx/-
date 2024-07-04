try:
	with open('text.txt', 'r', encoding='utf-8') as file:
		print(file.read())
	#Открываем файл
	print('file: text.txt')
except:
		print('файл не найден')
finally:
	file.close()