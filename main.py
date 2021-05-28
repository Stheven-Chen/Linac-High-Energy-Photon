from os import system
import platform


#clean consule function
def clean ():
    clean = platform.system().lower()
    if 'windows' in clean:
        system('cls')
    else:
        system('clear')

def v1andMU (MU, v1):
    v1andMU = v1/MU
    return v1andMU

def KTP (p, T):
    KTP = ((273.2+T)*p0)/((273.2+T0)*p)
    return KTP

def Kpol (M1, M2):
    Kpol = ((M1)+(M2))/(2*M1)
    return Kpol

def Ks (v1, v2):
    Ks = 1.198+(-0.8753)*(v1/v2)+0.6773*(v1/v2)**2
    return Ks

def Dzref (M1, ndw, kQ):
    Dzref = M1*Kpol(M1, M2)*Ks(v1,v2)*KTP(p,T)*ndw*kQ
    return Dzref
def Dzmax (PDD):
    Dzmax =( 100 * (Dzref (M1, ndw, kQ)/PDD))*100
    return Dzmax

def main():
    hasilRatio = v1andMU(MU, v1)
    print(f"Ratio of dosimeter reading and monitor unit: {hasilRatio} nC/MU")
    hasilKTP = KTP (p, T)
    print(f"Temperature and presure correction: {hasilKTP}")
    hasilKpol = Kpol (M1, M2)
    print(f"Polarization correction: {hasilKpol}")
    hasilKs = Ks (v1, v2)
    print(f"Saturation correction: {hasilKs}")
    hasilDzref = Dzref (M1, ndw, kQ)
    print(f"Dose at Z ref: {hasilDzref} Gy/MU")
    hasilDzmax = Dzmax (PDD)
    print(f"Dose at Z Max: {hasilDzmax} cGy/MU")

#variabel needed
MU = None; p=None; T=None; T0=20; p0=101.3; M1= None; M2=None;
v1=None; v2=None; ndw=None; kQ=None; PDD=None

# MU
while MU is None:
    value = input('MU value: ')
    try:
        MU = float(value)
    except ValueError:
        print(f"{value} is not a number")
        print(20*'=')
        continue
# v1
while v1 is None:
    value = input('v1 value: ')
    try:
        v1 = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# v2
while v2 is None:
    value = input('v2 value: ')
    try:
        v2 = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# M1
while M1 is None:
    value = input('M1 value: ')
    try:
        M1 = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# M2
while M2 is None:
    value = input('M2 value: ')
    try:
        M2 = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# p
while p is None:
    value = input('p value: ')
    try:
        p = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# T
while T is None:
    value = input('T value: ')
    try:
        T = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# PDD
while PDD is None:
    value = input('PDD value: ')
    try:
        PDD = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# KQ
while kQ is None:
    value = input('kQ value: ')
    try:
        kQ = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
# ndw
while ndw is None:
    value = input('ndw value: ')
    try:
        ndw = float(value)
    except ValueError:
        print(f"{value} is not a number")
        continue
    
# Main program loop
while True:
    clean()
    main()
    while True:
        answer = str(input('\nLagi? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Cek Kembali Input")
    if answer == 'y':
        clean()
        continue
    else:
        print("Dadah")
        break



