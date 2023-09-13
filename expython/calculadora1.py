from datetime import datetime

def inserir_horarios():
    entrada_inicio = input("Informe o horário de início (HH:mm): ")
    entrada_termino = input("Informe o horário de término (HH:mm): ")

    if not validar_formato_hora(entrada_inicio) or not validar_formato_hora(entrada_termino):
        return "Formato de hora inválido. Use HH:mm."

    hora_inicio = datetime.strptime(entrada_inicio, "%H:%M")
    hora_termino = datetime.strptime(entrada_termino, "%H:%M")

    horas_trabalhadas = calcular_horas_trabalhadas([entrada_inicio, entrada_termino])

    return f"Horas trabalhadas: {horas_trabalhadas}"

def validar_formato_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def calcular_horas_trabalhadas(entradas):
    total_minutos = 0
    entrada_valida = False
    entrada_saida = []

    for entrada in entradas:
        try:
            hora = datetime.strptime(entrada, "%H:%M")
            entrada_saida.append(hora)
            entrada_valida = not entrada_valida
        except ValueError:
            return "Formato de hora inválido: {}".format(entrada)

    if entrada_valida:
        return "Entrada/Saída desbalanceadas"

    for i in range(0, len(entrada_saida), 2):
        diferenca = entrada_saida[i + 1] - entrada_saida[i]
        total_minutos += diferenca.total_seconds() / 60

    horas = int(total_minutos // 60)
    minutos = int(total_minutos % 60)

    return "{} horas e {} minutos".format(horas, minutos)

if __name__ == "__main__":
    resultado = inserir_horarios()
    print(resultado)
