def confusion(score):
    present_confusion = int(input("""
                              Tu paciente presenta confusión?
                              
                              1 - SI
                              
                              2 - NO
                              
                              selecciona una opción: """))
    if present_confusion == 1:
        score.append(1)
        return score
    elif present_confusion == 2:
        score.append(0)
        return score
    else:
        print("Opción no valida, intenta de nuevo.")
        confusion(score)


def uremy(score):
    present_uremy = int(input("""
                              Tu paciente presenta unos niveles de uremia menores a 19 mg / mL?
                              
                              1 - SI
                              
                              2 - NO
                              
                              selecciona una opción: """))
    if present_uremy == 1:
        score.append(1)
        return score
    elif present_uremy == 2:
        score.append(0)
        return score
    else:
        print("Opción no valida, intenta de nuevo.")
        uremy(score)
        

def breaths(score):
    present_breaths = int(input("""
                              Tu paciente presenta respiraciones de 30 por minuto o más?
                              
                              1 - SI
                              
                              2 - NO
                              
                              selecciona una opción: """))
    if present_breaths == 1:
        score.append(1)
        return score
    elif present_breaths == 2:
        score.append(0)
        return score
    else:
        print("Opción no valida, intenta de nuevo.")
        uremy(score)


def blood_pressure(score):
    present_blood_pressure = int(input("""
                              Tu paciente presenta una tension arterial sistolica de 90 mmHg o menores
                              y una tension arterial diastolica de 60 mmHg o menor?
                              
                              1 - SI
                              
                              2 - NO
                              
                              selecciona una opción: """))
    if present_blood_pressure == 1:
        score.append(1)
        return score
    elif present_blood_pressure == 2:
        score.append(0)
        return score
    else:
        print("Opción no valida, intenta de nuevo.")
        uremy(score)


def age(score):
    present_age = int(input("""
                              Tu paciente tiene una edad de 65 años o más?
                              
                              1 - SI
                              
                              2 - NO
                              
                              selecciona una opción: """))
    if present_age == 1:
        score.append(1)
        return score
    elif present_age == 2:
        score.append(0)
        return score
    else:
        print("Opción no valida, intenta de nuevo.")
        uremy(score)


def run():
    score = []
    confusion(score)
    uremy(score)
    breaths(score)
    blood_pressure(score)
    age(score)
    test_result = sum(score)
    if test_result <= 1:
        print(f"""
              Tu paciente tiene un score de CURD 65 de {str(test_result)} 
              La mortalidad oscila entre 0,7% a 3%
              SE ACONSEJA MANEJO AMBULATORIO DEL PACIENTE
              """)
    elif test_result <= 3:
        print(f"""
              Tu paciente tiene un score de CURD 65 de {str(test_result)} 
              La mortalidad oscila entre 13% a 17%
              Por lo que se aconseja un manejo intrahospitalario
              SE ACONSEJA HOSPITALIZACION DEL PACIENTE
              """)
    else:
        print(f"""
              Tu paciente tiene un score de CURD 65 de {str(test_result)} 
              La mortalidad oscila entre 42% a 57%
              SE ACONSEJA HOSPITALIZACION EN UCI
              """)
    

if __name__ == "__main__":
    run()
        
    