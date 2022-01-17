def pam(systolic, dyastolic):
    pam = round(((dyastolic * 2) + systolic) / 3, 1)
    return pam


def run():
    systolic = int(input("Cual es la presión sistolica de tu paciente?: "))
    dyastolic = int(input("Cual esla presión diastolica de tu paciente?: "))
    pression = pam(systolic, dyastolic)
    if pression < 70:
        print(f"""
        La presion arterial media de tu paciente es {str(pression)}.
        Se encuentra en niveles bajos alarmantes de presión arterial media.""")

    elif pression > 100:
        print(f"""
        La presion arterial media de tu paciente es {str(pression)}.
        Se encuentra en niveles altos alarmantes de presión arterial media.""")

    else:
        print(f"""
        La presion arterial media de tu paciente es {str(pression)}.
        Se encuentra en niveles normales de presión arterial media.""")
    

if __name__ == "__main__":
    run()