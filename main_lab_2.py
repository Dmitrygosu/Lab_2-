import fileinput,time,os,psutil,re
start_time = time.time()
lst = []
s,l,n=' '*3

with fileinput.FileInput('111.txt') as file: # Считываем файл
    for line in file:
            for i in re.findall(r'\d+', line):
                lst.append(i)

if not lst: # Если нет результата(проверка на пустой файл)
    print('\nФайл text.txt пустой.')
else:    # Находим самую длинную последовательность
    for number, i in enumerate(lst):
        buff = 0
        for j in i:
            if int(j) > buff:
                buff = int(j)
                s = i
                l = len(i)
                n = number + 1
            else:
                break

print(f'Список всех последовательностей - {lst}\n'
      f'Самая длинная восх. посл. - {s}\n'
      f'Длинна последовательности - {l}\n'
      f'Номер последовательности - {n}')
process = psutil.Process(os.getpid())
print("Программа занимает ", process.memory_info().rss /1048576,"мбайт")  # in mbytes
print("--- %s Секунд выполнялась программа  ---" % (time.time() - start_time))
