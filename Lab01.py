import string
letras_reemplazar = [('j','i'),('h','i'),('ñ','n'),('k','l'),('u','v'),('w','v'),('y','z')]
tildes =[('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u')]
signo = ['?', '¿','¡','!',' ',',','.',';',':','\n']
UTF_8 = [('A','41'),('B','42'),('C','43'),('D','44'),('E','45'),
         ('F','46'),('G','47'),('H','48'),('I','49'),('J','4a'),
         ('K','4b'),('L','4c'),('M','4d'),('N','4e'),('O','4f'),
         ('P','50'),('Q','51'),('R','52'),('S','53'),('T','54'),
         ('U','55'),('V','56'),('W','57'),('X','58'),('Y','59'),('Z','5a')]
texto = open("POEMA.txt",encoding='utf-8')
linea = texto.read()
texto.close()
resultado= open("POEMA_pre.txt", 'w')

#1 Reeemplazar j->i  h->i  ñ->n  k->l  u->v w->v  y->z
def reemplazar():
    global linea
    for i,j in letras_reemplazar:
        linea= linea.replace(i,j)
                  
#2 Eliminar las tildes de las vocales
def tilde():
    global linea
    for i,j in tildes:
        linea= linea.replace(i,j)
        
#3 Todas las letras a Mayusculas
def mayuscula():
    global linea
    for letra in linea :
            linea= linea.replace(letra,letra.upper())
            
#4 Elimine los espacios en blanco y signos de puntuacion

def signos():
    global linea
    for s in signo:
            linea= linea.replace(s,"")

# Guardar en "POEMA_pre.txt"
def guardar():
    resultado.write(linea)
    resultado.close()

#5 Tabla de frecuencias (diccionario ) - 5 mayor frecuencia

def frecuencias(archivo):
    global lineaP,s2
    texto = open(archivo+".txt")
    lineaP = texto.read()
    texto.close()
    #Diccionario de frecuencias
    DiccFrecuencias ={}
    for i in lineaP:
        DiccFrecuencias[i]=DiccFrecuencias.get(i,0)+1
    print('*Frecuencias : '+str(DiccFrecuencias))
    #Ordenar    
    s1= sorted(DiccFrecuencias.values())
    s1.reverse()
    D ={}
    for i in s1:
        for j in DiccFrecuencias.keys():
            if DiccFrecuencias[j]==i:
                D[j]=DiccFrecuencias[j]   
    s2=list(D.keys())
    s3 =s2[:5]
    print('*Mayor frecuencia:'+str(s3))


#6 Aplicar el método Kasiski
def kasiski():
    C=[]
    dic={}
    txt = lineaP
    for i in range(len(txt)-2):
        C.append(txt[i:i+3])
    for k in C:
        a = C.count(k)
        if a > 1:
            dic[k]=a
    print('*Kasiski')
    print(dic)
#7 UNICODE-8
def utf8():
    l = lineaP
    for i,j in UTF_8:
        l= l.replace(i,j)
    print("*UNICODE-8")
    print(l)

#8 UNICODE-8230

#9 AQUÍ cada 20 caracteres
def aqui():
    global lineaP
    n=len(lineaP)
    d=20
    r=n//d
    l1=""
    for i in range(d, n+1, d):
        l1 = l1+lineaP[i-20:i]+'MANI'
    l1 = l1+lineaP[r*d:]
    n1=len(l1)
    if (n1%4 != 0):
        rr=(n1//4+1)*4
        for i in range(rr-n1):
            l1=l1+'X'
    print("*Insertar cada 20 -> MANI")
    print(l1)
    
def main():
    #1era Parte
    reemplazar()
    tilde()
    mayuscula()
    signos()
    guardar()
    #2da Parte
    frecuencias("POEMA_pre")
    #frecuencias("proba")
    kasiski()
    utf8()
    aqui()
    
if __name__ == '__main__':
    main()