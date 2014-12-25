# Copyright (c) Dec 24, 2014 CareerMonk Publications and others.
# E-Mail                   : info@careermonk.com 
# Creation Date            : 2014-01-10 06:15:46 
# Last modification        : 2008-10-31 
#               by         : Narasimha Karumanchi 
# Book Title               : Data Structures And Algorithmic Thinking With Python
# Warranty                 : This software is provided "as is" without any 
#                            warranty; without even the implied warranty of 
#                             merchantability or fitness for a particular purpose. 


import operator

class Point():
    def __init__(self, x, y):
        """Init"""
        self.x = x
        self.y = y

    def __repr__(self):
        return '<{0}, {1}>'.format(self.x, self.y)


def distance(a, b):
    return abs((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def closestPoints(points):
    """Time complexity: O(nlogn)"""
    n = len(points)
    if n <= 1:
        print 'Invalid input'
        raise Exception
    elif n == 2:
        return (points[0], points[1])
    elif n == 3:
        # Calc directly
        (a, b, c) = points
        ret = (a, b) if distance(a, b) < distance(a, c) else (a, c)
        ret = (ret[0], ret[1]) if distance(ret[0], ret[1]) < distance(b, c) else (b, c)
        return ret
    else:
        points = sorted(points, key=operator.attrgetter('x'))
        leftPoints = points[ : n / 2]
        rightPoints = points[n / 2 : ]
        
        # Devide and conquer.
        (left_a, left_b) = closestPoints(leftPoints)
        (right_a, right_b) = closestPoints(rightPoints)

        # Find the min distance for leftPoints part and rightPoints part.
        d = min(distance(left_a, left_b), distance(right_a, right_b))
        # Cut the point set into two.
        mid = (points[n / 2].x + points[n / 2 + 1].x) / 2

        # Find all points fall in [mid - d, mid + d]
        midRange = filter(lambda pt : pt.x >= mid - d and pt.x <= mid + d, points)
        # Sort by y axis.
        midRange = sorted(midRange, key=operator.attrgetter('y'))

        ret = None
        localMin = None
        # Brutal force, for each point, find another point and delta y less than d.
        # Calc the distance and update the global var if hits the condition.
        for i in xrange(len(midRange)):
            a = midRange[i]
            for j in xrange(i + 1, len(midRange)):
                b = midRange[j]
                if (not ret) or (abs(a.y - b.y) <= d and distance(a, b) < localMin):
                        ret = (a, b)
                        localMin = distance(a, b)
        return ret



points = [ Point(1, 2), Point(0, 0), Point(3, 6), Point(4, 7), Point(5, 5),
        Point(8, 4), Point(2, 9), Point(4, 5), Point(8, 1), Point(4, 3),
        Point(3, 3)]
print closestPoints(points)