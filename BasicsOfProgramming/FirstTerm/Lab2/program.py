import math


def sales_prediction():
    suma = float(input())
    print(suma*1.19)
pass
def yard_to_meter():
    W = int(input())
    metr = W * 0.914
    milim = W * 0.914 * 1000
    kilometrs = W * 0.914 / 1000
    print(milim)
    print(metr)
    print(kilometrs)
pass


def cashier():
    tovar1 = float(input())
    tovar2 = float(input())
    tovar3 = float(input())
    tovar4 = float(input())
    tovar5 = float(input())
    suma = tovar1 + tovar2 + tovar3 + tovar4 + tovar5
    pdv = suma*0.14
    razom = suma + pdv
    print(suma)
    print(pdv)
    print(razom)
pass

def odometer():
    V0=float(input())
    a=float(input())
    t1=float(input())
    t2=float(input())
    V = V0 + a*t1
    SzPr = V0*t1+((a*t1**2)/2)
    SbezPr = V*t2
    Szag = math.sqrt((SzPr + SbezPr)**2)
    print(Szag)
pass


def payment_instalments():
    suma1 = float(input())
    q_paym = float(input())
    suma_zag = suma1*1.05
    one_paym = suma_zag / q_paym
    print(suma_zag)
    print(one_paym)
pass


def miles_per_galon():
    Miles_driven = float(input())
    Gallons_of_gas_used = float(input())
    Mpg= Miles_driven / Gallons_of_gas_used
    print(Mpg)
    pass


def cookie():
    amount_of_pechenok = float(input())
    zyker = 1.5 / 48 * amount_of_pechenok
    versh_maslo = 1 / 48 * amount_of_pechenok
    cklyanka_boroshna = 2.75 / 48 * amount_of_pechenok
    print(zyker)
    print(versh_maslo)
    print(cklyanka_boroshna)
pass


def vineyard():
    R = float(input())
    E = float(input())
    S = float(input())
    V = int((R - 2*E ) / S)
    print(V)
pass


def compound_interest():
    P = float(input())
    Pr = float(input())
    n = float(input())
    t = float(input())
    r = Pr / 100
    A = P * (1+ (r/n))**(n*t)
    print(A)
pass


if __name__ == "__main__":
    eval(input() + "()")