def SumarPares(num):
    resultado = num % 2
    if resultado == 0:
        if(num==2):
            return 2
        else:
            return SumarPares(num-2)+num
    else:
        return ('Es numero impar')
print(SumarPares(8))
