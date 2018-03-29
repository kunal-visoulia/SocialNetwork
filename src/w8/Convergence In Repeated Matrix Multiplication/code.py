import numpy

A=numpy.mat('1 2;3 4')

#v=numpy.mat('1;1')
v=numpy.mat('3;11')
#it doesn't matter what vector you choose it always converges
#to a constant vector

print v
for i in range(10):
    z=A*v
    #normalization
    z=z/numpy.linalg.norm(z)
    print z
    v=z
    print "*********"