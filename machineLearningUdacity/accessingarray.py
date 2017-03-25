import numpy as np

def test_run():
    a = np.random.rand(10,40)
    print (a)

    element = a[3,2]
    print (element)

    print(a[:,0:30:3])


if __name__ == "__main__":
    test_run()