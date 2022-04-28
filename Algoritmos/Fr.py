def fr_rn(respiraciones):
    fr = int(respiraciones)
    if fr < 40:
        print(f"""
        La edad del paciente pertenece al grupo recien nacido.
              
        La frecuencia respiratoria de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 45:
        print(f"""
        La edad del paciente pertenece al grupo recien nacido.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo recien nacido.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_preescolar(respiraciones):
    fr = int(respiraciones)
    if fr < 20:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 30:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo pre-escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_escolar(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo escolar.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_adolecente(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo adolecente.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def fr_adulto(respiraciones):
    fr = int(respiraciones)
    if fr < 12:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra bradipneico.""")

    elif fr > 20:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra taquipneico.""")

    else:
        print(f"""
        La edad del paciente pertenece al grupo adulto.
              
        La frecuencia cardiaca de tu paciente es {str(fr)}.
        
        Tu paciente se encuentra en los rangos normales de frecuencia respiratoria.""")


def run():
    edad_paciente = int(input("Edad de tu paciente: "))
    respiraciones_paciente = int(input("Respiraciones contadas en 1 minuto: "))

    if edad_paciente <= 1:
        respiraciones = respiraciones_paciente
        fr_rn(respiraciones)

    elif edad_paciente <= 6:
        respiraciones = respiraciones_paciente
        fr_preescolar(respiraciones)

    elif edad_paciente <=13:
        respiraciones = respiraciones_paciente
        fr_escolar(respiraciones)

    elif edad_paciente <= 17:
        respiraciones = respiraciones_paciente
        fr_adolecente(respiraciones)

    elif edad_paciente >= 18:
        respiraciones = respiraciones_paciente
        fr_adulto(respiraciones)

    else:
        print("Esta opción es erronea, intenta de nuevo.")
        run()


if __name__ == "__main__":
    run()