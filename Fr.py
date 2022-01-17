def fr_rn(respiraciones):
    fr = int(respiraciones)
    if fr < 40:
        print(f"""
        La frecuencia respiratoria de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 45:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_lactante_menor(respiraciones):
    fr = int(respiraciones)
    if fr < 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fr > 30:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_lactante_mayor(respiraciones):
    fr = int(respiraciones)
    if fr < 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 30:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_preescolar(respiraciones):
    fr = int(respiraciones)
    if fr < 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 300:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_escolar(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_adolecente(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_adulto(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def run():
    menu = int(input("""
    Selecciona el rango en el que se encuentra tu paciente:
    
    1 Recien Nacido (Nacimiento - 6 semanas).
    
    2 Lactante Menor (7 semanas - 1 año).
    
    3 Lactante Mayor (1 año - 2 años).
    
    4 Pre-escolar (2 años - 6 años).
    
    5 Escolar (6 años - 13 años).
    
    6 Adolecente (13 años - 17 años).
    
    7 Adulto (17 años en adelante).
    
    Cual es tu opción?: """))

    if menu == 1:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_rn(respiraciones)

    elif menu == 2:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_lactante_menor(respiraciones)

    elif menu == 3:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_lactante_mayor(respiraciones)

    elif menu == 4:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_preescolar(respiraciones)

    elif menu == 5:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_escolar(respiraciones)

    elif menu == 6:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_adolecente(respiraciones)

    elif menu == 7:
        respiraciones = int(input("Cuantas respiraciones encotraste en tu paciente durante 1 minuto?: "))
        fr_adulto(respiraciones)

    else:
        print("Esta opción es erronea, intenta de nuevo.")
        run()


if __name__ == "__main__":
    run()