#!/usr/bin/env python3
import unittest
import re
import random

def add_two_new(str):
    r = str.split(')')
    l = []
    for i in range(len(r)):
        if len(r[i]) > 0:
            l.append(r[i])
    l[0] = l[0].translate(str.maketrans('','','() ->+'))
    l[1] = l[1].translate(str.maketrans('','','() ->+'))
    l[0] = l[0][::-1]
    l[1] = l[1][::-1]
    r = int(l[0]) + int(l[1])
    r = '%d'%(r)
    r = ' -> '.join(r[::-1])
    return r


class _Test(unittest.TestCase):
    def inttostr(self, a):
        a = '%d'%(a)
        a = ' -> '.join(a[::-1])
        return a
    def test_add_two_new(self):
        a = add_two_new('(2 -> 4 -> 3) + (5 -> 6 -> 4)')
        self.assertEqual(a, '7 -> 0 -> 8')
    def test_add_two_new_rand(self):
        rd = random.Random()
        for i in range(10000):
            a = rd.randint(1, 1000000000000000000)
            b = rd.randint(1, 1000000000000000000)
            c = a + b
            str1 = '%s%s%s%s%s'%('(', self.inttostr(a), ')+(', self.inttostr(b), ')')
            str2 = self.inttostr(c)
            self.assertEqual(add_two_new(str1), str2)
            a = rd.randint(1, 1000000000000000000)
            b = rd.randint(1, 10000000000)
            c = a + b
            str1 = '%s%s%s%s%s'%('(', self.inttostr(a), ')+(', self.inttostr(b), ')')
            str2 = self.inttostr(c)
            self.assertEqual(add_two_new(str1), str2)
            a = rd.randint(1, 10000000000000)
            b = rd.randint(1, 1000000000000000000)
            c = a + b
            str1 = '%s%s%s%s%s'%('(', self.inttostr(a), ')+(', self.inttostr(b), ')')
            str2 = self.inttostr(c)
            self.assertEqual(add_two_new(str1), str2)

if __name__ == '__main__':
    unittest.main()
