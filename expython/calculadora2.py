from datetime import datetime, timedelta

def inserir_horarios_e_intervalo():
    entrada_inicio = input("Informe o horário de início (HH:mm): ")
    entrada_termino = input("Informe o horário de término (HH:mm): ")
    entrada_intervalo = input("Informe a duração do intervalo (HH:mm): ")

    if not validar_formato_hora(entrada_inicio) or not validar_formato_hora(entrada_termino) or not validar_formato_hora(entrada_intervalo):
        return "Formato de hora inválido. Use HH:mm."

    hora_inicio = datetime.strptime(entrada_inicio, "%H:%M")
    hora_termino = datetime.strptime(entrada_termino, "%H:%M")
    intervalo = timedelta(hours=int(entrada_intervalo.split(':')[0]), minutes=int(entrada_intervalo.split(':')[1]))

    horas_trabalhadas = calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo)

    return f"Horas trabalhadas: {horas_trabalhadas}"

def validar_formato_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def calcular_horas_trabalhadas(hora_inicio, hora_termino, intervalo):
    diferenca = hora_termino - hora_inicio
    total_minutos = diferenca.total_seconds() / 60 - intervalo.total_seconds() / 60

    horas = int(total_minutos // 60)
    minutos = int(total_minutos % 60)

    return "{} horas e {} minutos".format(horas, minutos)

if __name__ == "__main__":
    resultado = inserir_horarios_e_intervalo()
    print(resultado)
