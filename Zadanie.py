def reading(perepis):
    people=[]
    f=open(perepis,'r',encoding='utf-8')
    for i in f:
        i = i.join(perepis.split())
        if i:
            parts = i.split()
            if len(parts) >= 4:
                surname = parts[0]
                name = parts[1]
                patronymic = parts[2]
                date = parts[3]
                year = date.split('.')[-1]
                year = int(year)

                people.append({
                    'surname': surname,
                    'name': name,
                    'patronymic': patronymic,
                    'birth_year': year
                })
    f.close()
    return people

def zadanie_a(people):
    c=0
    for i in people:
        if i[3]<1978:
            c+=1
            print(i[0])
    print('Людей всехоЖ ', str(c))

def zadanie_b(people):
    start=input('От ')
    finish=input('До ')

    if not start.isdigit() or not finish.isdigit():
        return

    start=int(start)
    finish=int(finish)

    if start > finish:
        start,finish=finish,start

    print('Результаты', str(start), '--', str(finish))

    count=0

    for i in people:
        if start<=i[3]<=finish:
            count +=1
            print(i[0],' ',i[1],' ',i[2],'--',str(i[3]))

    if count == 0:
        print('Нету')
    else:
        print('Есть стокаЖ ', str(count))

try:
    people=reading('perepis.txt')
    zadanie_a(people)
    zadanie_b(people)
except:
    print('Нормально сделай да')