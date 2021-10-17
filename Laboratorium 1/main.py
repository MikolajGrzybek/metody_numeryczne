import math
import numpy as np

def cylinder_area(r:float, h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0:
        bases_area = 2 * math.pi * math.pow(r, 2)
        wall_area = 2 * math.pi * r * h
    else:
        return np.nan

    print(type(bases_area + wall_area))
    return bases_area + wall_area

def fib(n:int):
    a, b = 1, 1
    fib_arr = [a, b]

    for i in range(2, n + 1):
        c = fib_arr[-1] + fib_arr[-2]
        fib_arr.append(c)

    result = np.ndarray(fib_arr)
    return result

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[2*a, 1, -a],[0, 1, 1],[-a, a, 1]])

    M_det = np.linalg.det(M)
    
    if(M_det == 0):
        M_trnp = np.nan
    else:
        M_trnp = np.transpose(M)

    M_inv = np.linalg.inv(M)
    
    print("Macierz:\n {0}".format(M))
    print("Macierz odwrócona:\n {0}".format(M_inv))
    print("Macierz transponowana:\n {0}".format(M_trnp))
    
    return (M_inv, M_trnp, M_det)


def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """

    if n < 0 or m < 0:
        return None
    
    M = np.zeros((m,n))
    # m - wiersz
    # n - kolumna
                 
    for x in range(0, n):
        for i in range(0, m):
            if x > i:
                M[x, i] = x
            else:
                M[x, i] = i
                
    print("{0}".format(M))
    return M
