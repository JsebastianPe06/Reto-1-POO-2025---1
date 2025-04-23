#Esta función verifica si dos cadenas tienen los mismos caracteres
def mismos_caracteres(string1, string2):
    if(len(string1)!=len(string2)):
        return False
    cop1 = list(string1)
    cop2 = list(string2)
    for char in cop1:
        if char in cop2:
            cop2.remove(char)
        else:
            return False
    return True

#Esta función forma grupos de cadenas con los mismos caracteres en una lista
def grupos_mismos_caracteres(lis):
    s = lis.copy()
    nueva_lista = []
    while(len(s)!=0):
        grupo = [s[0]]
        for i in range(1,len(s)):
            if(mismos_caracteres(s[0], s[i])):
                grupo.append(s[i])
        nueva_lista.append(grupo)
        for i in grupo:
            s.remove(i)
    return nueva_lista

#Esta función elimina sublistas de una lista que contienen solo un elemento
def mantener_grupos(lis):
    t = len(lis)
    i = 0
    while(i < t):
        if(len(lis[i])==1):
            lis.remove(lis[i])
            t -= 1
        else:
            i += 1
    return lis 

lista_cadenas = ["roma", "amor", "perro", "uno", "onu", "nou", "sol", "los"]
grupos_formados = mantener_grupos(grupos_mismos_caracteres(lista_cadenas))
for i in range(len(grupos_formados)):
    print(grupos_formados[i])
