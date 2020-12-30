#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar 
# de ese número, done n es el número introducido.
"""
def guardo_tabla(nro):
    archivo="tabla_"+nro+".txt"
    f = open(archivo, "w")
    for i in range(1, 11):
        texto=str(i)+" x "+nro+"="+str(i*int(nro))+"\n"
        print(texto)
        f.write(texto)

    f.close()


num=input("Ingrese un número para guardar su tabla de multiplicar en fichero tabla_n.txt ")
guardo_tabla(num)

#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def leo_tabla(nro):
    archivo="tabla_"+nro+".txt"
    try:
        f = open(archivo, "r")
    except FileNotFoundError:
        print("el archivo no existe")
    else:
        print(f.read())
        f.close()

num=input("Ingrese un número para leer su tabla de multiplicar en fichero tabla_n.txt ")
leo_tabla(num)        

#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def leo_tabla(nro, lin):
    archivo="tabla_"+nro+".txt"
    try:
        f = open(archivo, "r")
    except FileNotFoundError:
        print("el archivo no existe")
    else:
        for i in range(1, int(lin)):
            f.readline()
        print(f.readline())
        f.close()

num=input("Ingrese un número para leer su tabla de multiplicar en fichero tabla_n.txt ")
lin=input("Ingrese qué línea quiere mostrar (1 - 10): ")
leo_tabla(num, int(lin))

#Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

def words_file(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        file = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = file.read()
        return len(content.split())

print(words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))
print(words_file('https://no-existe.txt'))
"""
#Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
#  (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

def get_pib(url, country):
    '''
    Función que muestra por pantalla el pib per cápita un país dado de los años disponibles en un fichero dado.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
        country: Es una cadena con el código del país. 
    Devuelve:
        Un diccionario con pares año:pib del país country que hay en el fichero con la url dada.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        data = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista
        data = [i.split('\t') for i in data] # Dividir cada línea por el tabulador
        data = [list(map(str.strip, i)) for i in data] # Eliminar espacios en blanco
        for i in data:
            i[0] = i[0].split(',')[-1] # Obtener el código del país del primer elemento de la lista
        data[0][0] = 'years'
        data = {i[0]:i[1:] for i in data}
        result = {data['years'][i]:data[country][i] for i in range(len(data['years']))}
        return result

country = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', country)
print('Año', '\t', 'PIB')
for year, pib in get_pib('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true', country).items():
    print(year, '\t', pib)
