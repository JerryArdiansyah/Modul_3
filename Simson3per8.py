#Metode Simpson 1/3
from math import e 

def f(x) :
    return e**x

def simpson38(x0,xn,n):
    h= (xn - x0) /n

    integration = f(x0) + f(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)

    # Final Integrasi
    integration = integration *3 * h/8

    return integration

# Sesi input
lower_limit = float(input("Masukkan Batas Bawah Daerah Integral: "))
upper_limit = float(input("Masukkan Batas Atas Daerah Integral: "))
sub_interval = int(input("Masukkan Jumlah Pias: "))

#Memanggil Simpson 1/3
result = simpson38(lower_limit, upper_limit, sub_interval)
print("\nHasil Integral dengan Metode Simpson 1/3: %0.6f" % (result))