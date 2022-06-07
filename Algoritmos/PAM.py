def blood_pressure(func):
    def wrapper(systolic, dyastolic):
        func(systolic, dyastolic)
        mbp = round(((dyastolic * 2) + systolic) / 3, 1)
        if mbp < 70:
            print(f"""
                  La presion arterial media de tu paciente es {str(mbp)} mmHg
                  
                  Tu paciente se encuentra en los niveles bajos alarmantes de presion arterial
                  """)
        elif mbp >100:
            print(f"""
                  La presion arterial media de tu paciente es {str(mbp)} mmHg
                  
                  Tu paciente se encuentra en los niveles altos alarmantes de presion arterial
                  """)
        else:
            print(f"""
                  La presion arterial media de tu paciente es{str(mbp)} mmHg
                  
                  Tu paciente se encuentra en los rangos normales de presion arterial
                  """)
    return wrapper


@blood_pressure
def medial_blood_pressure_algoritm(systolic, dyastolic):
    print("""
          Rango normal de presion arterial media es 70 mmHg - 100 mmHg
          """)
    pass


def run():
    try:    
        systolic = int(input("Cual es la presion arterial sistlica de tu paciente?: "))
        dyastolic = int(input("Cual es la presion arterial diastolica de tu paciente?: "))
        medial_blood_pressure_algoritm(systolic, dyastolic)
    
    except ValueError:
        print(f"Por favor inserta los valores correctos de las presiones arteriales de tu paciente")
        return run()
    
    
if __name__ == "__main__":
    run()