import calendar

def diasReunion(string):
    anio = ''
    mes = ''
    dia = ''
    contador = 0
    aux = 0
    hora = ''

    for x in string:
        if x == ' ':
            aux += 1
            hora = string[aux:]
            break
        else:
            aux += 1
        if x == '-':
            contador += 1
        elif contador == 0:
            anio = anio + x
        elif contador == 1:
            mes = mes + x
        elif contador == 2:
            dia = dia + x

    intAnio = int(anio)
    intMes = int(mes)
    intDia = int(dia)

    ultimoDiaMes = calendar.monthrange(intAnio, intMes)[1]
    fechaReunion = []
    fechaTemp = ''

    for i in range(16):
        if intDia + 7 <= ultimoDiaMes:
            intDia += 7
        else:
            intDia += 7
            intDia -= ultimoDiaMes
            if intMes == 12:
                intMes = 1
                intAnio += 1
            else:
                intMes += 1
            ultimoDiaMes = calendar.monthrange(intAnio, intMes)[1]
        
        anio = str(intAnio)
        mes = str(intMes)
        dia = str(intDia)

        if intMes < 10:
            mes = '0' + mes
        if intDia < 10:
            dia = '0' + dia

        fechaTemp = anio + '-' + mes + '-' + dia + ' ' + hora
        fechaReunion.append(fechaTemp)

    return fechaReunion

print(diasReunion('2018-06-28 09:00'))