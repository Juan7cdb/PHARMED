def fc_rn(latidos):
    fc = int(latidos * 4)
    if fc < 120:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 140:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_lactante_menor(latidos):
    fc = int(latidos * 4)
    if fc < 100:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 130:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_lactante_mayor(latidos):
    fc = int(latidos * 4)
    if fc < 100:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 120:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_preescolar(latidos):
    fc = int(latidos * 4)
    if fc < 80:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 120:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_escolar(latidos):
    fc = int(latidos * 4)
    if fc < 80:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_adolecente(latidos):
    fc = int(latidos * 4)
    if fc < 70:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_adulto(latidos):
    fc = int(latidos * 4)
    if fc < 60:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def run():
    edad_paciente = int(input("Años de tu paciente: "))
    latidos_paciente = int(input("Cuantos latidos encontraste en 15 segundos: "))

    if edad_paciente == 1:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_rn(latidos)

    elif edad_paciente == 2:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_lactante_menor(latidos)

    elif edad_paciente == 3:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_lactante_mayor(latidos)

    elif menu == 4:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_preescolar(latidos)

    elif menu == 5:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_escolar(latidos)

    elif menu == 6:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_adolecente(latidos)

    elif menu == 7:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_adulto(latidos)

    else:
        print("Esta opción es erronea, intenta de nuevo.")
        run()


if __name__ == "__main__":
    run()