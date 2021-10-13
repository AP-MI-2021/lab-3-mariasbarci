def is_prim(num):
    '''
    verifica daca un numar este prim
    :param num: natural number
    :return: True daca  numărul este prim sau False daca numărul nu este prim
    '''
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for divizor in range(3, num // 2, 2):
        if num % divizor == 0:
            return False

    return True
    pass


def verifica_numere_not_prime(lista: list):
    '''
    Verifică dacă toate numerele sunt neprime
    :param lista: Lista
    :return: True -> dacă toate numerele sunt neprime sau False -> dacă există numere prime
    '''
    for elem in lista:
        if is_prim(elem):
            return False
    return True
    pass


def test_get_longest_all_not_prime():
    assert verifica_numere_not_prime([8,6,18]) is True
    assert verifica_numere_not_prime([2,8,4]) is False
    assert verifica_numere_not_prime([10, 11, 12, 13, 14, 15]) is False



def get_longest_all_not_prime(lista):
    '''
    Afiseaza subsecventa cu numere prime
    :param lista:lista cu numere prime
    :return:
    '''
    subsecventa_finala = []
    subsecventa_temporala = []
    for inceput in range(0, len(lista)):
        for sfarsit in range(inceput + 1, len(lista)):
            if verifica_numere_not_prime(lista[inceput:sfarsit]) is True:
                subsecventa_temporala = lista[inceput:sfarsit]
                if len(subsecventa_finala) < len(subsecventa_temporala):
                    subsecventa_finala = subsecventa_temporala[:]
                    subsecventa_temporala = []
                pass
            else:
                break
    return subsecventa_finala
    pass


def verificare_cifre_prime(num):
    '''
    Toate numerele sunt formate din cifre prime.
    :param num: int numbers
    :return: False or True
    '''
    str_nr = str(num)
    for cifre in range(0, len(str_nr)):
        cifra_verificare = int(str_nr[cifre])
        if not is_prim(cifra_verificare):
            return False
    return True
    pass


def test_verificare_cifre_prime():
    assert verificare_cifre_prime(237) is True
    assert verificare_cifre_prime(427) is False
    assert verificare_cifre_prime(235) is True
    assert verificare_cifre_prime(423) is False


def subsecventa_verificare(lista: list):
    for ele in lista:
        if not verificare_cifre_prime(ele):
            return False

    return True
    pass


def get_longest_prime_digits(lista: list):
    '''
    Toate numerele sunt formate din cifre prime.
    :param lista:
    :return:
    '''
    subsecventa_finala = []
    subsecventa_temp = []
    for inceput in range(0, len(lista)):
        for sfarsit in range(inceput + 1, len(lista) + 1):
            if subsecventa_verificare(lista[inceput:sfarsit]) is True:
                subsecventa_temporala = lista[inceput:sfarsit]
                if len(subsecventa_finala) < len(subsecventa_temporala):
                    subsecventa_finala = subsecventa_temporala[:]
                    subsecventa_temporala = []
                pass
            else:
                break
    return subsecventa_finala
    pass


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([5, 3, 5, 3, 2, 1]) == [5,3,5,3,2]
    assert get_longest_prime_digits([ 7, 7, 2, 2, 2, 7, 1]) == [7,7,2,2,2,7]




def citire_lista():
    lista = [int(el) for el in input('Introduceti elementele separate prin spatiu: ').split(' ')]
    return lista
def get_longest_div_k(lst, k):
    '''
    Toate numerele sunt divizibile cu k (citit).
    :param lst:list with int elem
    :param k:int k
    :return:
    '''
    cea_mai_lunga_secventa = []
    secventa_actuala = []
    k = int(k)
    i = 0
    while i < len(lst):
        if int(lst[i]) % k == 0:
            secventa_actuala.append(lst[i])
            i+=1
        else:
            if len(secventa_actuala) > len(cea_mai_lunga_secventa):
                cea_mai_lunga_secventa = secventa_actuala.copy()
            secventa_actuala.clear()
            i+=1
    if len(secventa_actuala) > len(cea_mai_lunga_secventa):
        cea_mai_lunga_secventa = secventa_actuala.copy()
    return cea_mai_lunga_secventa

def test_get_longest_div_k():
    assert get_longest_div_k([2, 4, 13,3, 23], 2) ==[2, 4]

test_get_longest_div_k()

def citire_k_formare_secventa(lst):
    k = int(input('Introduceti numarul: '))
    print(get_longest_div_k(lst, k))

def meniul_programului():
    test_get_longest_all_not_prime()
    test_get_longest_prime_digits()
    test_verificare_cifre_prime()
    test_get_longest_prime_digits()


    enter = []
    while True:
        print('''
        1. Citire lista
        2.Cea mai lunga subsecventa cu proprietatea:Toate numerele sunt neprime.
        3.Cea mai lunga sbsecventa cu proprietatea:Toate numerele sunt formate din cifre prime.
        4.Toate numerele sunt divizibile cu k (citit).
        x.Iesire''')
        cmd = input('Comanda: ')

        if cmd == '1':
            pass
            enter = citire_lista()
        elif cmd == '2':
            print(get_longest_all_not_prime(enter))
        elif cmd == '3':
            print(get_longest_prime_digits(enter))
        elif cmd=='4':
            k=int(input("citeste k:"))
            print(get_longest_div_k(enter,k))
        elif cmd == 'x':
            break

    pass

meniul_programului()

def teste():
    test_get_longest_all_not_prime()
    test_verificare_cifre_prime()
    test_get_longest_prime_digits()
    test_get_longest_div_k()

teste()

