import numpy as np

def liste(min = 0, max = 10, uzunluk = 1):
    "min -> minumum rastgele sayı\nmax-> maximum rastgele sayı\nuzunluk -> dizinin boyutu"
 
    return list(np.sort(np.random.randint(min, max, uzunluk)))

