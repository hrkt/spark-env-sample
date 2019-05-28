import random
MAX=1000000
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(xrange(0, MAX)) \
             .filter(inside).count()
print "Pi is roughly %f" % (4.0 * count / MAX)
