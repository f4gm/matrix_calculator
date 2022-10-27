# Made by: f4gm
# github.com/f4gm

#Funcion para validar un entero
def validint(number):
    valid = True
    while valid:
        valid_int = True
        for character in number:
            if character == ".":
                valid_int = False
        if valid_int:
            valid = False
            return number
        else:
            error("EL NÚMERO INGRESADO NO CORRESPONDE A UN NÚMERO ENTERO.")
            text("INGRESE UN NÚMERO CORRECTO:")
            number = input(">> ")

#Funcion para validar que son numeros
def validnumber(number):
    valid = True
    while valid:
        count = 0
        for character in number:
            if character != "0" and character != "1" and character != "2" and character != "3" and character != "4" and character != "5" and character != "6" and character != "7" and character != "8" and character != "9" and character != "." and character != "-":
                count = count + 1
        if count > 0:
            error("EL VALOR - " + number + " - NO CORRESPONDE A UN NÚMERO.")
            text("INGRESE UN VALOR CORRECTO:")
            number = input(">> ")
        else:
            valid = False
            return number

#Funcion para validar caracter vacio
def validempty(valor):
    valid = True
    while valid:
        if valor == "":
            error("NO INGRESÓ NINGÚN VALOR.")
            text("INGRESE UN VALOR CORRECTO:")
            valor = input(">> ")
        else:
            valid = False
            return valor

#Funcion para validar una suma o resta y una multiplicacion a partir de las dimensiones de sus matrices
def validim(matrix1, matrix2, parameter):
    rows_matrix1, columns_matrix1 = matrixdim(matrix1)
    rows_matrix2, columns_matrix2 = matrixdim(matrix2)
    if parameter == 1:
        #Valida la dimension en suma o resta
        if rows_matrix1 == rows_matrix2 and columns_matrix1 == columns_matrix2:
            return True
        else:
            return False
    elif parameter == 2:
        #Valida la dimension en una multiplicacion
        if columns_matrix1 == rows_matrix2:
            return True
        else:
            return False

#Funcion para generar matrices
def matrixgen(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append([None]*columns)
    return matrix

#Funcion para encontrar la dimension de una matriz
def matrixdim(matrix):
    dimrow = len(matrix) 
    dimcolumns = len(matrix[0])
    return dimrow, dimcolumns

#Llenar matrices
def matrixfill(matrix):
    rows, columns = matrixdim(matrix)
    for row in range(rows):
        for column in range(columns):
            text("INGRESE EL VALOR DE LA FILA " + str(row + 1) + " Y LA COLUMNA " + str(column + 1))
            matrix[row][column] = float(validnumber(validempty(input(">> "))))
    return matrix

#Operaciones

#Suma de matrices
def matrixplus():
    message("SUMA DE MATRICES")

    #Definimos la dimension de la primer matriz
    text("INGRESE LA DIMENSIÓN DE LA PRIMERA MATRIZ")
    text("FILAS:")
    rows_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))

    #Definimos la dimension de la segunda matriz
    text("INGRESE LA DIMENSIÓN DE LA SEGUNDA MATRIZ")
    text("FILAS:")
    rows_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))

    valid = True
    while valid:
        #Genera las matrices con los datos ingresados para comprobar posteriormente que tengan la misma dimension
        matrix1 = matrixgen(rows_matrix1, columns_matrix1)
        matrix2 = matrixgen(rows_matrix2, columns_matrix2)

        if validim(matrix1, matrix2, 1):
            #Cuando las dimensiones de las matrices son iguales, procede a solitar el llenado de las matrices
            message("INGRESE LOS DATOS DE LA PRIMERA MATRIZ")
            matrix1 = matrixfill(matrix1)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix1)

            message("INGRESE LOS DATOS DE LA SEGUNDA MATRIZ")
            matrix2 = matrixfill(matrix2)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix2)
            
            #Ademas se genera la matrices resultado para ser llenada posteriormente con la suma de los elementos de las matrices ingresadas
            matrix_result = matrixgen(rows_matrix1, columns_matrix1)
            for row in range(rows_matrix1):
                for column in range(columns_matrix1):
                    matrix_result[row][column] = matrix1[row][column] + matrix2[row][column]
            valid = False
            return matrix_result    
        else:
            #Si las dimensiones de las matrices no coinciden, se vuelven a pedir
            error("LAS MATRICES NO TIENEN LA MISMA DIMENSIÓN.")

            #Dimension de la primera matriz
            text("VUELVA A INGRESAR LA DIMENSIÓN DE LA PRIMERA MATRIZ")
            text("FILAS:")
            rows_matrix1 = int(float(validnumber(validempty(input(">> ")))))
            text("COLUMNAS:")
            columns_matrix1 = int(float(validnumber(validempty(input(">> ")))))

            #Dimension de la segunda matriz
            message("VUELVA A INGRESAR LA DIMENSIÓN DE LA SEGUNDA MATRIZ")
            text("FILAS:")
            rows_matrix2 = int(float(validnumber(validempty(input(">> ")))))
            text("COLUMNAS:")
            columns_matrix2 = int(float(validnumber(validempty(input(">> ")))))

#Resta de matrices
def matrixminus():
    #Las funciones de suma y resta de matrices son, en escencia, iguales
    message("RESTA DE MATRICES")

    text("INGRESE LA DIMENSIÓN DE LA MATRIZ MINUENDO")
    text("FILAS:")
    rows_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))

    text("INGRESE LA DIMENSIÓN DE LA MATRIZ SUSTRAENDO")
    text("FILAS:")
    rows_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))

    valid = True
    while valid:
        matrix1 = matrixgen(rows_matrix1, columns_matrix1)
        matrix2 = matrixgen(rows_matrix2, columns_matrix2)
        if validim(matrix1, matrix2, 1):
            message("INGRESE LOS DATOS DE LA MATRIZ MINUENDO")
            matrix1 = matrixfill(matrix1)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix1)

            message("INGRESE LOS DATOS DE LA MATRIZ SUSTRAENDO")
            matrix2 = matrixfill(matrix2)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix2)

            matrix_result = matrixgen(rows_matrix1 , columns_matrix1)
            for row in range(rows_matrix1):
                for column in range(columns_matrix1):
                    matrix_result[row][column] = matrix1[row][column] - matrix2[row][column]
            valid = False
            return matrix_result
        else:
            error("LAS MATRICES NO TIENEN LA MISMA DIMENSIÓN.")

            text("VUELVA A INGRESAR LA DIMENSIÓN DE LA MATRIZ MINUENDO")
            text("FILAS:")
            rows_matrix1 = int(float(validnumber(validempty(input(">> ")))))
            text("COLUMNAS:")
            columns_matrix1 = int(float(validnumber(validempty(input(">> ")))))

            message("VUELVA A INGRESAR LA DIMENSIÓN DE LA MATRIZ SUSTRAENDO")
            text("FILAS:")
            rows_matrix2 = int(float(validnumber(validempty(input(">> ")))))
            text("COLUMNAS:")
            columns_matrix2 = int(float(validnumber(validempty(input(">> ")))))

#Multiplicacion por un escalar
def matrixsca():
    message("MATRIZ POR UN ESCALAR")

    #Se define la dimension de la matriz
    text("INGRESE LA DIMENSIÓN DE LA MATRIZ")
    text("FILAS:")
    rows = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns = int(float(validint(validnumber(validempty(input(">> "))))))

    #Se llena la matriz
    message("INGRESE LOS DATOS DE LA MATRIZ")
    matrix = matrixfill(matrixgen(rows, columns))
    text("LA MATRIZ INGRESADA FUE:")
    matrixprint(matrix)

    #Se define el escalar
    message("INGRESE EL ESCALAR")
    scalar = float(validnumber(validempty(input(">> "))))

    #Se define la matrix resultado para posteriormente llenarla
    matrix_result = matrixgen(rows, columns)
    for row in range(rows):
        for column in range(columns):
            matrix_result[row][column] = scalar*(matrix[row][column])
    return matrix_result

#Producto de matrices

#Funcion para extraer una fila o una columna de una matriz
def extract(matrix, index, parameter):
    rows, columns = matrixdim(matrix)
    if parameter == 1:
        #Extrae una fila de una matriz
        extraction = matrix[index]
    elif parameter == 2:
        #Extrae una columna de una matriz
        extraction = [None]*rows
        for row in range(rows):
            for column in range(columns):
                extraction[row] = matrix[row][index]
    return extraction

#Producto punto de listas
def dotproduct(list1, list2):
    #Ambas listas tienen el mismo numero de elementos
    list_result = [None]*len(list1)
    for index in range(len(list1)):
        list_result[index] = (list1[index])*(list2[index])
    sum = 0
    for element in list_result:
        sum = sum + element
    return sum

#Producto de matrices
def matrixpro():
    #Definimos la dimension de la primer matriz
    text("INGRESE LA DIMENSIÓN DE LA PRIMERA MATRIZ")
    text("FILAS:")
    rows_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix1 = int(float(validint(validnumber(validempty(input(">> "))))))

    #Definimos la dimension de la segunda matriz
    text("INGRESE LA DIMENSIÓN DE LA SEGUNDA MATRIZ")
    text("FILAS:")
    rows_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))
    text("COLUMNAS:")
    columns_matrix2 = int(float(validint(validnumber(validempty(input(">> "))))))

    valid = True
    while valid:
        #Generamos las matrices para posteriormente verificar sus dimensiones
        matrix1 = matrixgen(rows_matrix1, columns_matrix1)
        matrix2 = matrixgen(rows_matrix2, columns_matrix2)

        if validim(matrix1, matrix2, 2):
            #Cuando las columnas de la primer matriz es igual a las filas de la segunda, procedemos a solicitar el llenado de las matrices
            message("INGRESE LOS DATOS DE LA PRIMERA MATRIZ")
            matrix1 = matrixfill(matrix1)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix1)

            message("INGRESE LOS DATOS DE LA SEGUNDA MATRIZ")
            matrix2 = matrixfill(matrix2)
            text("LA MATRIZ INGRESADA FUE:")
            matrixprint(matrix2)

            #Definimos la matrix resultado y procedemos a llenarla
            matrix_result = matrixgen(rows_matrix1, columns_matrix2)
            for row in range(rows_matrix1):
                for column in range(columns_matrix2):
                    matrix_result[row][column] = dotproduct(extract(matrix1, row, 1), extract(matrix2, column, 2))
            return matrix_result
        else:
            error("LAS COLUMNAS DE LA PRIMERA MATRIZ NO COINCIDE CON LAS FILAS DE LA SEGUNDA.")

            #Dimension de la primera matriz
            text("VUELVA A INGRESAR LA DIMENSIÓN DE LA PRIMERA MATRIZ")
            text("FILAS:")
            rows_matrix1 = int(float(validnumber(input(">> "))))
            text("COLUMNAS:")
            columns_matrix1 = int(float(validnumber(input(">> "))))

            #Dimension de la segunda matriz
            message("VUELVA A INGRESAR LA DIMENSIÓN DE LA SEGUNDA MATRIZ")
            text("FILAS:")
            rows_matrix2 = int(float(validnumber(input(">> "))))
            text("COLUMNAS:")
            columns_matrix2 = int(float(validnumber(input(">> "))))

#Interfaz

#Funcion para imprimir una matriz en el centro
def matrixprint(matrix):
    print()
    rows = len(matrix)
    for row in range(rows):
        print("{:^100}".format(str(matrix[row])))

#Funcion para imprimir mensajes con encabezados
def message(text):
    print()
    print("====================================================================================================")
    print()
    print("{:^100}".format(text))
    print()
    print("====================================================================================================")

#Funcion para imprimir errores y su descripcion
def error(text):
    print()
    print("====================================================================================================")
    print()
    print("{:^100}".format("ERROR"))
    print("{:^100}".format(text))
    print()
    print("====================================================================================================")

#Funcion para imprimir mensajes en el centro pero sin encabezados
def text(text):
    print()
    print("{:^100}".format(text))

#Funcion para desplegar el menu de operaciones
def menu():
    print()
    print("{:^100}".format("SUMA DE MATRICES ........... 1"))
    print("{:^100}".format("RESTA DE MATRICES .......... 2"))
    print("{:^100}".format("MATRIZ POR UN ESCALAR ...... 3"))
    print("{:^100}".format("PRODUCTO DE MATRICES ....... 4"))
    print("{:^100}".format("CERRAR PROGRAMA ............ 5"))

open = True
message("CALCULADORA DE MATRICES")
print()
print("====================================================================================================")
text("ELIJA UNA OPERACION:")
menu()
select = input(">> ")
while open:
    if select == "1":
        #Suma de matrices
        matrix_plus = matrixplus()
        message("RESULTADO")
        matrixprint(matrix_plus)
        message("ELIJA UNA OPERACION:")
        menu()
        select = input(">> ")
    elif select == "2":
        #Resta de matrices
        matrix_minus = matrixminus()
        message("RESULTADO")
        matrixprint(matrix_minus)
        message("ELIJA UNA OPERACION:")
        menu()
        select = input(">> ")
    elif select == "3":
        #Matriz por un escalar
        matrix_sca = matrixsca()
        message("RESULTADO")
        matrixprint(matrix_sca)
        message("ELIJA UNA OPERACION:")
        menu()
        select = input(">> ")
    elif select == "4":
        #Producto de matrices
        matrix_pro = matrixpro()
        message("RESULTADO")
        matrixprint(matrix_pro)
        message("ELIJA UNA OPERACION:")
        menu()
        select = input(">> ")
    elif select == "5":
        #Cerrar el programa
        message("PROGRAMA FINALIZADO")
        open = False
    else:
        #Valores no contemplados en la lista
        error("EL VALOR INGRESADO NO SE ENCUENTRA EN LA LISTA. ELIJA UN VALOR CORRECTO.")
        menu()
        select = input(">> ")