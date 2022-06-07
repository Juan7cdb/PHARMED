def ckd_form(func):
    def wrapper(age, creatinine, expo, constant):
        func(age, creatinine, expo, constant)
        glomerular_filtration = constant * ((creatinine / 0.7) ** (-expo)) * (0.993 ** age)
        glomerular_filtration = round(glomerular_filtration, 1)
        print(f"La tasa de filtración glomerular es {str(glomerular_filtration)} mL/min/1,73 m2")
    return wrapper


@ckd_form
def glomerular_filtration_algoritm_1(age, creatinine, expo, constant):
    print("""
          Estimación de la tasa de filtración glomerular mediante la ecuación CKD-EPI en adultos
          """)
    pass


def run():
    index = int(input("""
    Escoge la opción del sexo de tu paciente:
    
    1 - Hombre
    
    2 - Mujer 
    
    Cual es tu respuesta: """))
    
    index_2 = int(input("""
    Que raza es tu paciente:
    
    1 - Blanca
    
    2 - Negra 
    
    Cual es tu respuesta: """))
    
    if index == 1 and index_2 == 1:
        constant = 144
        age = int(input("Edad de tu paciente: "))
        cretinine = float(input("Cuanto tiene de creatinina tu paciente?: "))
        if cretinine <= 0.9:
            expo = 0.411
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
        else:
            expo = 1.209
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)       
            
    elif index == 2 and index_2 == 1:
        constant = 144
        age = int(input("Edad de tu paciente: "))
        cretinine = float(input("Cuanto tiene de creatinina tu paciente?: "))
        if cretinine <= 0.7:
            expo = 0.329
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
        else:
            expo = 1.2
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
            
    elif index == 1 and index_2 == 2:
        constant = 163
        age = int(input("Edad de tu paciente: "))
        cretinine = float(input("Cuanto tiene de creatinina tu paciente?: "))
        if cretinine <= 0.9:
            expo = 0.411
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
        else:
            expo = 1.209
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
            
    elif index == 2 and index_2 == 2:
        constant = 166
        age = int(input("Edad de tu paciente: "))
        cretinine = float(input("Cuanto tiene de creatinina tu paciente?: "))
        if cretinine <= 0.7:
            expo = 0.320
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
        else:
            expo = 1.2
            glomerular_filtration_algoritm_1(age, expo, cretinine, constant)
            
    else:
        print("Error detectado por favor vuelve a intentar.")
        run()
            
        
if __name__ == "__main__":
    run()