import math
import matplotlib.pyplot as plt
import numpy as np

def toto(self):
    buffer = []
    for s in self:
        #s = s.replace('.', ',')
        if s.find('E') > 0:
            num = float(s.split('-')[1])
            s = float(s.split('E')[0])
            s = round(s/(10**num), 4)
            buffer.append(s)
        else:
            buffer.append(round(float(s), 4))
    return buffer


def main():
    V = []
    I = []
    with open('ВАХ диода.txt', 'r') as f:
        size = 1
        strs = f.readlines()
        for str in strs:
            str = str.replace('   ', '').replace('\n', '').replace('E+00', '')
            if str.find('(') < 0:
                V.append(str.split('  ')[0])
                I.append(str.split('  ')[1])
        f.close()
    V = toto(V)
    I = toto(I)
    # for i in range(1, len(V)):
    #     print('I:', I[i], ' V:', V[i])
    # print(len(V))
    x = np.arange(0., 2., 0.002)
    # print(10**(-9))
    Rb = 1.106
    print('Rb = ', Rb)
    Is = 1.331*10**(-8)
    print('Is = ', Is)
    NFt = 0.044
    print('NFt = ', NFt)
    y = x*Rb + np.log((x + Is)/Is)*NFt
    # print(y)
    plt.title('ВАХ')
    plt.xlabel('V, B')
    plt.ylabel('I, A')
    plt.plot(V, I)
    plt.plot(y, x, 'r--')
    plt.axis([0, 2, 0, 1.25])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
