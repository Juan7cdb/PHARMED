def imc(weight, height):
    height = height * 0.01
    imc = float(round(weight / (height ** 2), 2))
    return imc
    

def run():
    weight = float(input("cual es el peso de tu paciente (en kilogramos): "))
    height = float(input("Cual es la altura de tu paciente (en centimetros): "))
    result = imc(weight, height)

    if result <= 16.00:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una desnutrición grave.""")

    elif result <= 16.99:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una desnutrición moderada.""")

    elif result <= 18.49:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una desnutrición aceptable.""")

    elif result <= 24.99:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta un peso normal.""")

    elif result <= 29.99:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta sobrepeso.""")
    
    elif result <= 34.99:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una obesidad tipo 1, riesgo moderado.""")

    elif result >= 39.99:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una obesidad tipo 2, riesgo grave.""")

    elif result >= 40.00:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta una obesidad tipo 3, riesgo muy grave.""")

    else:
        print(f"""
        Tu paciente tiene un indice de masa corporal de {str(result)}.
        
        Presenta unos niveles muy alterado, revisalo bien.""")


if __name__ =="__main__":
    run()