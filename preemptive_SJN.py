import time
from prettytable import *

def preemptive_SJN(procesos):
    final = [0 for i in range(len(procesos))]
    espera = [0 for i in range(len(procesos))]
    en_proceso = []
    en_espera = []
    instante = 0
    instantes = 0
    for i in range(len(procesos)):
        instantes += procesos[i][2]
    while instante != instantes:
        print(f'Instante {instante}', end=' ')
        for i in range(len(procesos)):
            if procesos[i][1] == instante:
                if len(en_proceso) == 0:
                    en_proceso = procesos[i]
                elif procesos[i][2] < en_proceso[2]:
                    print(en_proceso[0], end = ' ')
                    en_espera.append(en_proceso)
                    en_proceso = procesos[i]
                else:
                    en_espera.append(procesos[i])
                    continue
            if en_proceso[2] == 0:
                final[procesos.index(en_proceso)] = instante
                print(en_proceso[0], end=' ')
                en_proceso = []
                if len(en_espera) > 0:
                    min = en_espera[0][2]
                    for j in range(len(en_espera)):
                        if en_espera[j][2] < min:
                            min = en_espera[j][2]
                            min_index = en_espera.index(en_espera[j])
                    en_proceso = en_espera[min_index]
                    del en_espera[min_index]
                    continue
                else:
                    continue
            else:
                continue
        #time.sleep(1)
        print(en_proceso[0])
        en_proceso[2] -= 1
        if len(en_espera) > 0:
            min_index = 0
            min = en_proceso[2]
            for i in range(len(en_espera)):
                if en_espera[i][2] < min:
                    min = en_espera[i][2]
                    min_index = en_espera.index(en_espera[i])
            if en_espera[min_index][2] < en_proceso[2]:
                en_proceso = en_espera[min_index]
                del en_espera[min_index]
            for i in range(len(en_espera)):
                espera[procesos.index(en_espera[i])] += 1
        instante += 1
    final[procesos.index(en_proceso)] = instante
    return espera, final
procesos = [['PA', 0, 3],['PB', 1, 5],['PC', 4, 2],['PD', 5, 6], ['PE', 8, 4], ['PF', 9, 10]]
tiempo = [procesos[i][2] for i in range(len(procesos))]
espera, final = preemptive_SJN(procesos)
labels = ['Nombre', 'Llegada', 'Tiempo', 'Espera', 'Final']
table = PrettyTable(labels)
for i in range(len(final)):
    table.add_row([procesos[i][0], procesos[i][1], tiempo[i], espera[i], final[i]])
print(table)
