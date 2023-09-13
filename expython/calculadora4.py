from datetime import datetime, timedelta

def inserir_horarios_e_intervalo():
    entrada_inicio = input("Informe o horário de início (HH:mm ou H:mm): ")
    entrada_termino = input("Informe o horário de término (HH:mm ou H:mm): ")
    entrada_intervalo = input("Informe a duração do intervalo (HH:mm ou H:mm): ")

    entrada_inicio = entrada_inicio.replace(":", "")
    entrada_termino = entrada_termino.replace(":", "")
    entrada_intervalo = entrada_intervalo.replace(":", "")

    if not validar_formato_hora(entrada_inicio) or not validar_formato_hora(entrada_termino) or not validar_formato_hora(entrada_intervalo):
        return "Formato de hora inválido. Use H:mm ou HH:mm."

    hora_inicio = datetime.strptime(entrada_inicio, "%H%M")
    hora_termino = datetime.strptime(entrada_termino, "%H%M")
    intervalo = timedelta(hours=int(entrada_intervalo[:-2]), minutes=int(entrada_intervalo[-2:]))

    horas_trabalhadas = calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo)

    return f"Horas trabalhadas: {horas_trabalhadas}"

def validar_formato_hora(hora):
    try:
        datetime.strptime(hora, "%H%M")
        return True
    except ValueError:
        return False

def calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo):
    if hora_inicio > hora_termino:
        
        diferenca = (hora_termino + timedelta(hours=24)) - hora_inicio - intervalo
    else:
        diferenca = hora_termino - hora_inicio - intervalo

    total_minutos = diferenca.total_seconds() / 60

    horas = int(total_minutos // 60)
    minutos = int(total_minutos % 60)

    return "{} horas e {} minutos".format(horas, minutos)

if __name__ == "__main__":
    resultado = inserir_horarios_e_intervalo()
    print(resultado)
