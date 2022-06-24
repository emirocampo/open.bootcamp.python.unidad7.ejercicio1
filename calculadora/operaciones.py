def sumar(*args):
    """
        suma consecutivamene los 'n>=2' elementos que se pasen por la funcion 'sumar(a,b,...,z)'
    """
    if(len(args)<=1):
        return "minimo dos argumentos"
    else:
        sum = args[0]
        for i in range(2,len(args)+1):
            sum += args[i-1]
        return sum

def restar(*args):
    """
        resta consecutivamene los 'n>=2' elementos que se pasen por la funcion 'restar(a,b,...,z)'
    """
    if(len(args) <= 1):
        return "minimo dos argumentos"
    else:
        res = args[0]
        for i in range(2,len(args)+1):
            res -= args[i-1]
        return res

def multiplicar(*args):
    """
        multiplica consecutivamene los 'n>=2' elementos que se pasen por la funcion 'multiplicar(a,b,...,z)'
    """
    if(len(args)<=1):
        return "minimo dos argumentos"
    else:
        pro = args[0]
        for i in range(2,len(args)+1):
            pro *= args[i-1]
        return pro

def dividir(*args):
    """
        divide consecutivamene los 'n>=2' elementos que se pasen por la funcion 'dividir(a,b,...,z)'
    """
    if(len(args)<=1):
        return "minimo dos argumentos"
    else:
        div = args[0]
        for i in range(2,len(args)+1):
            div /= args[i-1]
        return div