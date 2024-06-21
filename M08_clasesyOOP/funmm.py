class Funmm:

    def __init__(self,lista):
        self.lista = lista

    def ver_primo(self,nu):
        
        p=True
        for i in range(2,nu):

            a=nu%i

            if a==0:
                p=False
                break

        return p
    
    def ver_primo_l(self):

        print('Numeros primos:')

        for i in self.lista:

            if self.ver_primo(i):
                print(i, ' es un numero primo')
            else:
                print(i,' no es un numero primo')
    
    def val_modal(self):

        print('Valor modal:')
        lista_unicos = []
        lista_repeticiones = []

        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)

        mx=max(lista_repeticiones)
        p=lista_repeticiones.index(mx)
        num=lista_unicos[p]

        print('el valor modal es ',num,' se repite ',mx,' veces')
        return num,mx
    
    def conv_temp(self,uo,ud):

        print('Conversion de temperatura:')

        for t in self.lista:

            if uo == 'C' and ud =='F':
                tf = 32+(t*(9/5))
            elif uo == 'C' and ud == 'K':
                tf = t + 273.15
            elif uo == 'K' and ud == 'F':
                tf = 32+((t-273.15)*(9/5))
            elif uo == 'F' and ud == 'K':
                tf = (t - 32)*(5/9) + 273.15
            elif uo == 'K' and ud == 'C':
                tf = t-273.15
            elif uo == 'F' and ud == 'C':
                tf = (t - 32)*(5/9)
            print(t,' grados ', uo, ' son ', tf, ' grados ', ud)
    
    def facto(self,num):

        f=1

        if num<=0 or type(num)!=int:
            return 'El numero no es valido'
        elif num >1:
            f=num*self.facto(num-1)
        return f
    
    def facto_l(self):

        print('Factoriales:')

        for i in self.lista:

            print('El factorial de ', i, ' es ', self.facto(i))
