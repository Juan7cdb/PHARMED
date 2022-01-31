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
    menu = int(input("""
    Selecciona el rango en el que se encuentra tu paciente:
    
    1 Recien Nacido (Nacimiento - 6 semanas).
    
    2 Lactante Menor (7 semanas - 11 meses).
    
    3 Lactante Mayor (1 año - 2 años).
    
    4 Pre-escolar (3 años - 6 años).
    
    5 Escolar (7 años - 13 años).
    
    6 Adolecente (14 años - 17 años).
    
    7 Adulto (18 años en adelante).
    
    Cual es tu opción?: """))

    if menu == 1:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_rn(latidos)

    elif menu == 2:
        latidos = int(input("Cuantos latidos encotraste en tu paciente en 15 segundos?: "))
        fc_lactante_menor(latidos)

    elif menu == 3:
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