import numpy as np

def test_run():
    a = np.random.rand(5,4)
    #print (a)

    element = a[3,2]
    #print (element)

    #print(a[:,0:30:3])
    a[1,1] = 4
    #print (a)
    a[:,2] = [1, 2, 3, 6, 5]
    print (a)
    indices = np.array([1, 0, 2, 3])
    print (a[indices])

    b = np.array([(1,2,3,4,5,6,7,8,9),(9,8,7,6,5,4,3,2,1)])
    print (b)
    m = b.mean()
    b[b<m] = m
    print (b)

if __name__ == "__main__":
    test_run()