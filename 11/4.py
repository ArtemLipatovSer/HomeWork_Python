def removeElList(remEl, list):
    count = 0
    listRe = list.copy()
    for i in list:
        for j in remEl:
            if i == j:
                listRe.remove(j)
                count += 1
    return count


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

elements = [2, 3, 5]

print(f'Количество удаленных элементов - {removeElList(elements, arr)}')
