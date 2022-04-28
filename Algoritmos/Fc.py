def fc_lactantes(latidos):
    fc = int(latidos * 4)
    if fc < 100:
        print(f"""
        La edad del paciente pertenece al grupo lactante.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 140:
        print(f"""
        La edad del paciente pertenece al grupo lactante.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo lactante.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_preescolar(latidos):
    fc = int(latidos * 4)
    if fc < 80:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.      
        
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 120:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_escolar(latidos):
    fc = int(latidos * 4)
    if fc < 80:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_adolecente(latidos):
    fc = int(latidos * 4)
    if fc < 70:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def fc_adulto(latidos):
    fc = int(latidos * 4)
    if fc < 60:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra bradicardico.""")

    elif fc > 100:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra taquicardico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fc)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia cardiaca.""")


def run():
    try:
        edad_paciente = int(input("Años de tu paciente: "))
        latidos_paciente = int(input("Cuantos latidos encontraste en 15 segundos: "))

        if edad_paciente <= 1:
            latidos = latidos_paciente
            fc_lactantes(latidos)

        elif edad_paciente <= 6:
            latidos = latidos_paciente
            fc_preescolar(latidos)

        elif edad_paciente <= 13:
            latidos = latidos_paciente
            fc_escolar(latidos)

        elif edad_paciente <= 17:
            latidos = latidos_paciente
            fc_adolecente(latidos)

        elif edad_paciente >= 18:
            latidos = latidos_paciente
            fc_adulto(latidos)

        else:
            print("Esta opción es erronea, intenta de nuevo.")
            run()

    except ValueError:
        print(f"Por favor inserta el valor correcto de latidos encontrados en 15 segundos en tu paciente")
        return run()
    

if __name__ == "__main__":
    run()