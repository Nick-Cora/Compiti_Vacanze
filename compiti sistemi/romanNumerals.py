u = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
d = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
m = ["", "M", "MM", "MMM"]

romanNumber = []
indice = 0
def conversion(number):
    mCounter = int(number / 1000) # migliaia
    cCounter = int((number - mCounter * 1000) / 100) # centinaia
    dCounter = int((number - mCounter * 1000 - cCounter * 100) / 10) # decine
    uCounter = int(number - mCounter * 1000 - cCounter * 100 - dCounter * 10) # unità
    mm = m[mCounter]
    cc = c[cCounter]
    dd = d[dCounter]
    uu = u[uCounter]
    return (mm + cc + dd + uu)

def main():
    num = int(input("Inserire num: "))

    print(conversion(num))

if __name__=="__main__":
    main()