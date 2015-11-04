'''menu que recibira por parametro:
un titulo y un apuntador a una tupla que contendra las opciones
'''

def menu(principal,*opc):
    
    print(" MENU".center(45, "-"))
    print("\n\t\t -%s- \n"%(principal.upper().title())) # titulo centrado
    
    for i in range (len(opc)):            
        print("\t",i+1,"- ",str(opc[i]).capitalize()) # tabulado con primera letra en mayuscula
    print("".center(45, "-"))

#Ejemplo
men=("uno","dos","tres","cuarto","cinco") 
menu("principal",*men)
