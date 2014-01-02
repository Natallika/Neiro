import sys
import random

# Входные данные
CountOfEnrty = 100 # Количество входов в перцептронe
maxW = 16
minW = -15
RandomW = [k for k in range(minW, maxW + 1)] # Все возможные веса
Tacks = [10, 50, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

dict_w = {
          -15:0b11111, -14:0b11110, -13:0b11101, -12:0b11100, -11:0b11011,
          -10:0b11010,  -9:0b11001,  -8:0b11000,-7:0b10111, -6:0b10110,
          -5:0b10101, -4:0b10100, -3:0b10011, -2:0b10010, -1:0b10001,
          0: 0b00000, 1: 0b00001, 2: 0b00010, 3: 0b00011, 4: 0b00100,
          5: 0b00101, 6: 0b00110, 7: 0b00111, 8: 0b01000, 9: 0b01001,
          10:0b01010, 11:0b01011, 12:0b01100, 13:0b01101, 14:0b01110,
          15:0b01111, 16:0b10000
          }

bits_mask = 0b11111



def CountEqualBits(value1, value2):
    equal_bits = 0
    r = ((value1 ^ value2)^bits_mask)
    for m in range(5):
        if (r >> m) & 0b1:
            equal_bits +=1
    return equal_bits

def Perceptron(X, W):
    SUMM_A = 0
    for i in range(len(X)):
        SUMM_A += int(X[i]*W[i])

    if(SUMM_A >= 0 ):
        sig = 1
    else:
        sig = -1
    return(sig)

def EditW(W, X, O):
    for i in range(len(W)):
        W[i] = W[i] + (O * X[i])
        if(W[i] > maxW):
            W[i] = maxW
        if(W[i] < minW):
            W[i] = minW

    return W

def GenerateX(X, len):
    X = []
    for i in range(len):
        X.append(random.choice([1,-1]))
    return X

def GenerateW(W, len):
    W = []
    for i in range(len):
        W.append(random.choice(RandomW))
    return W

def CompareList(Wa,Wb):
    a = enumerate(Wa)
    b = enumerate(Wb)
    return len(set(a) & set(b))

def CompareList1(Wa, Wb):
    comp = 0
    for i in range(len(Wa)):
        if Wa[i] == Wb[i]:
            comp +=1
    return comp

def main(output_file):
    Work = True
    Count = 1

    # Инициализация данных
    X1 = [] # 
    X2 = [] # 
    X3 = [] #

    Wa1 = [] # Вес связи для первый сети
    Wa2 = [] # Вес связи для первый сети
    Wa3 = [] # Вес связи для первый сети

    Wb1 = [] # Вес связи для первый сети
    Wb2 = [] # Вес связи для первый сети
    Wb3 = [] # Вес связи для первый сети

    X1 = GenerateX(X1, CountOfEnrty)
    X2 = GenerateX(X2, CountOfEnrty)
    X3 = GenerateX(X3, CountOfEnrty)

    Wa1 = GenerateW(Wa1, CountOfEnrty)
    Wa2 = GenerateW(Wa2, CountOfEnrty)
    Wa3 = GenerateW(Wa3, CountOfEnrty)

    Wb1 = GenerateW(Wb1, CountOfEnrty)
    Wb2 = GenerateW(Wb2, CountOfEnrty)
    Wb3 = GenerateW(Wb3, CountOfEnrty)


    while(Work):
     
        SIGa1 = Perceptron(X1, Wa1)
        SIGa2 = Perceptron(X2, Wa2)
        SIGa3 = Perceptron(X3, Wa3)


        SIGb1 = Perceptron(X1, Wb1)
        SIGb2 = Perceptron(X2, Wb2)
        SIGb3 = Perceptron(X3, Wb3)

        Oa = SIGa1 * SIGa2 * SIGa3
        Ob = SIGb1 * SIGb2 * SIGb3

        if(Oa == Ob):
            if(SIGa1 == Oa):
                Wa1 = EditW(Wa1, X1, Oa)
            if(SIGa2 == Oa):
                Wa2 = EditW(Wa2, X2, Oa)
            if(SIGa3 == Oa):
                Wa3 = EditW(Wa3, X3, Oa)
            if(SIGb1 == Ob):
                Wb1 = EditW(Wb1, X1, Ob)
            if(SIGb2 == Ob):
                Wb2 = EditW(Wb2, X2, Ob)
            if(SIGb3 == Ob):
                Wb3 = EditW(Wb3, X3, Ob)

        if Count in Tacks:
            CompW1 = CompareList(Wa1, Wb1)
            CompW2 = CompareList(Wa2, Wb2)
            CompW3 = CompareList(Wa3, Wb3)
            Equal_bits_W = 0
            
            for j in range(len(Wa1)):
                Equal_bits_W += CountEqualBits(dict_w[Wa1[j]],dict_w[Wb1[j]])
                Equal_bits_W += CountEqualBits(dict_w[Wa2[j]],dict_w[Wb2[j]])
                Equal_bits_W += CountEqualBits(dict_w[Wa3[j]],dict_w[Wb3[j]])
                
            print('На {0} такте совпадают:{1} весов и {2} бит'.format(Count, CompW1+CompW2+CompW3, Equal_bits_W), file=output_file)
            print('Веса A:\nWa1 = {0}\nWa2 = {1}\nWa3 = {2}\n'.format(Wa1,Wa2,Wa3), file=output_file)
            print('Веса B:\nWb1 = {0}\nWb2 = {1}\nWb3 = {2}\n'.format(Wb1,Wb2,Wb3), file=output_file)
      
        if((Wa1 == Wb1) and (Wa2 == Wb2) and (Wa3 == Wb3)):
            Work = False
        else:
            X1 = GenerateX(X1, len(X1))
            X2 = GenerateX(X2, len(X2))
            X3 = GenerateX(X3, len(X3))
        Count += 1

        

    print("Диапазон весов: {0}".format(RandomW), file=output_file)
    print("Количество входов в перцептрон {0}".format(CountOfEnrty), file=output_file)
    print("Количество циклов: {0}".format(Count), file=output_file)

if __name__ == '__main__':
    result_file = open('result.txt', 'w')
    for i in range(10):
        print('Test {0} started'.format(i + 1))
        print('Тест номер {0}:'.format(i + 1), file = result_file)
        main(result_file)
        print('-'*80, file = result_file)
        print('Test {0} finished'.format(i + 1))
    result_file.close()

