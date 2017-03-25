import numpy as np

def get_max_index(a):
    return (a.argmax())

def test_run():
    a = np.array([2, 3, 4, 5, 6, 2, 7, 1], dtype = np.int32)
    print ("Array:", a)

    #Find Maximum in array
    print ("Array:", a.max())
    print ("Index of Maximum:", get_max_index(a))

if __name__ == "__main__":
    test_run()
