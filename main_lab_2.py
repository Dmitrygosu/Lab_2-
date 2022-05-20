import fileinput, time,os,re,psutil
start_time = time.time()
lst = []
# СЧитаем файл
with fileinput.FileInput('111.txt') as file:
    for line in file:
            for i in re.findall(r'\d+', line):
                lst.append(i)
    # Список возрастающих последовательностей
    list1 = []
    # Находим самую длинную последовательность
    for number, i in enumerate(lst):
        temp_s=''
        fl = True
        buff = 0
        # Проверяем только если больше одного символа
        if len(i) > 1:
            for j in i:
                if int(j) > buff:
                    # Накапливаем последовательность
                    temp_s += j
                    buff = int(j)
                else:
                    # Не возрастающая последовательность
                    fl= False
                    break
            # Запомнили последовательность и её номер
            if fl:
                list1.append((temp_s, number + 1))
# Находим самую длинную последовательность
longest=max(list1, key=lambda i: len(i[0]))

print(f'Полученные из файла последовательнности- {lst}\n'
      f'Самая длинная восх. посл. - {longest[0]}\n'
      f'Длина последовательности - {len(longest[0])}\n'
      f'Номер последовательности - {longest[1]}')
process = psutil.Process(os.getpid())
print("Программа занимает ", process.memory_info().rss /1048576,"мбайт")  # in bytes
print("--- %s Секунд выполнялась программа  ---" % (time.time() - start_time))
