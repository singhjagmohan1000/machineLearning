''' Using Numpy Arrays'''

import numpy as np


def test_run():
    # print (np.array([(2, 3, 4),(5, 6, 7)]))
    # print (np.empty((5,4,3)))
    # print(np.ones((5, 4, 3)))
    x =  np.random.rand(5,4)
    print (np.random.normal(50,10,size=(2,3)))
    print (np.random.randint(0, 10, size=(2, 3)))
    print (x.shape)


if __name__ == "__main__":
   test_run()