#-*- coding: utf-8 -*-

def check(a, n):
    for i in xrange(1, n):
        if abs(a[i] - a[n]) == abs(i - n) or a[i] == a[n]: return False
    return True

# 1.循环
def find1():
    a = [1] * 9
    t  = 1
    for a[1] in xrange(1, 9):
        for a[2] in xrange(1, 9):
            if not check(a, 2): continue
            for a[3] in xrange(1, 9):
                if not check(a, 3): continue
                for a[4] in xrange(1, 9):
                    if not check(a, 4): continue
                    for a[5] in xrange(1, 9):
                        if not check(a, 5): continue
                        for a[6] in xrange(1, 9):
                            if not check(a, 6): continue
                            for a[7] in xrange(1, 9):
                                if not check(a, 7): continue
                                for a[8] in xrange(1, 9):
                                    if not check(a, 8): continue
                                    else:
                                        print "第%d种解法，" % t, a
                                        t += 1


# 2.递归
t = 1
def find(i, n, a):
    global t
    for j in xrange(1, n+1):
        a[i] = j
        if check(a, i):
            if i < n:
                find(i+1, n, a)
            else:
                print "第%d种解法，" % t, a
                t += 1

find(1, 9, [1]*10)
