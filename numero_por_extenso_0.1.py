unidades = {
    0:'zero', 1:'um', 2:'dois', 3:'três', 4:'quatro',
    5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9: 'nove'
}

conj_11_19 = {
    11:'onze', 12:'doze', 13:'treze', 14:'catorze', 15:'quinze',
    16:'dezesseis', 17:'dezessete', 18:'dezoito', 19:'dezenove'
}

dezenas = {
    10:'dez', 20:'vinte', 30:'trinta', 40:'quarenta', 50:'cinquenta',
    60:'sessenta', 70:'setenta', 80:'oitenta', 90:'noventa'
}

centenas = {
    100:'cem', 200:'duzentos', 300:'trezentos', 400:'quatrocentos', 500:'quinhentos',
    600:'seiscentos', 700:'setecentos', 800:'oitocentos', 900:'novecentos'

}

mil = ('mil')


lista = []

def num_extenso(num): 
    verificador(num)
    extenso = 'Voce digitou: ' + ' '.join(lista)
    print(extenso)
    return extenso

def verificador(num):
    num = sinal(num)
    if num >= 1000 and num <1000000:
        milhar(num)
    elif num >= 100 and num < 1000:
        centena(num)
    elif num >= 10 and num < 100:
        dezena(num)
    elif num < 10:
        unidade(num)
    else:
        lista.append('Número inválido')


def sinal(num):    
    if num < 0:
        lista.append('menos')
        num = num * -1
    return num

def unidade(num):
    num = num
    lista.append(unidades[num])

def dezena(num): 
    if num in range(11, 20):
        lista.append(conj_11_19[num])
    else:
        dz = (num // 10) * 10
        n = num % dz
        lista.append(dezenas[dz])
        if n != 0:
            lista.append('e')
            verificador(n)

def centena(num):
    ct = (num // 100) * 100
    dz = ((num % 100) // 10) * 10
    if dz != 0:
        n = (num % ct) % dz
    else:
        n = num % ct
    if dz != 0 and n != 0:
        centenas[100] = "cento"
    lista.append(centenas[ct])
    if dz != 0:
        lista.append('e')
        verificador(dz)
    if n != 0:
            lista.append('e')
            verificador(n)

def milhar(num):
    ml = (num // 1000)
    ct = ((num % 1000) // 100) * 100
    dz = (((num % 1000) % 100) // 10) * 10
    
    if ct != 0 and dz != 0:
        n = ((num % (ml * 1000)) % ct) % dz
    elif ct == 0 and dz != 0:
        n = (num % (ml * 1000)) % dz
    elif ct != 0 and dz == 0:
        n = (num % (ml * 1000)) % ct
    else:
        n = num % ml
    if ml > 1:
        verificador(ml)
    lista.append(mil)
    if ct != 0:
        lista.append('e')
        verificador(ct)
    if dz != 0:
        lista.append('e')
        verificador(dz)    
    if n != 0:
            lista.append('e')
            verificador(n)

num_extenso(100268)

