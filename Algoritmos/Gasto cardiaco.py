def cardiac_output(heart_frequency, ejection_volume):
        cardiac_output = round(heart_frequency * ejection_volume, 1)
        if cardiac_output < 4:
            print(f"""
                  El gasto cardiaco de tu paciente es {str(cardiac_output)} L/min
                  
                  Tu paciente se encuentra con valores bajos de gasto cardiaco
                  """)
        
        elif cardiac_output > 6.5:
            print(f"""
                  El gasto cardiaco de tu paciente es {str(cardiac_output)} L/min
                  
                  Tu paciente se encuentra con valores altos de gasto cardiaco
                  """)
        
        else:
            print(f"""
                  El gasto cardiaco de tu paciente es {str(cardiac_output)} L/min
                  
                  Tu paciente se encuentra con valores normales de gasto cardiaco
                  """)
            
        return cardiac_output
    
    
def body_surface_algoritm(weight):
    if weight < 10:
        body_sf = round((((weight * 4)+ 9)/ 100), 2)
        return body_sf
    
    else:
        body_sf = round((((weight * 4)+ 7)/ 90), 2)
        return body_sf


def cardiac_index(body_surface, heart_output):
    heart_index = round((heart_output / body_surface), 1)
    if heart_index < 2.2:
        print(f"""Tu paciente tiene un indice cardiaco de {str(heart_index)} L/min/m²
              
              Tu paciente esta en estado se shock
              Se recomienda iniciar monitorizacion y maniobras de reanimación y estabilización de signos vitales""")
    
    elif heart_index < 3:
        print(f"""Tu paciente tiene un indice cardiaco de {str(heart_index)} L/min/m²
              
              Tu paciente presenta un indice cardiaco bajo""")
        
    elif heart_index > 5:
        print(f"""Tu paciente tiene un indice cardiaco de {str(heart_index)} L/min/m²
              
              Tu paciente presenta un indice cardiaco alto""")
        
    else:
        print(f"""Tu paciente tiene un gasto cardiaco de {str(heart_index)}
              
              Tu paciente presenta un indice cardiaco normal""")
    
           
def run():
    try:    
        heart_frequency = int(input("Cual es la frecuencia cardiaca de tu paciente?: "))
        ejection_volume = float(input("Cual es el volumen de eyección de tu paciente?: "))
        weight = int(input("Cual es el peso de tu paciente?: "))
        heart_output = cardiac_output(heart_frequency, ejection_volume)
        body_surface = body_surface_algoritm(weight)
        cardiac_index(body_surface, heart_output)
        
    
    except ValueError:
        print(f"Por favor inserta los valores correctos de tu paciente")
        return run()
    
    
if __name__ == "__main__":
    run()