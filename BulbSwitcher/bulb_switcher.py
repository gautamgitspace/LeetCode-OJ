#!/usr/bin/env python

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        # /*  0. turn on all
        #  *   1. turn off every 2nd (2,4,6... are turned off)
        #  *   2. 3rd Round: toggle every 3rd (3,6,9.. are turned on)
        #  *   3. 4th Round: toggle every ith (i, 2i, 3i, 4i...)
        #  *   4. this goes on
        #  *   5. for last, nth, toggle last bulb
        #  *   simple enough, and that number is determined by
        #  *   how many factors a number has.
        #  */

        initially all bulbs are off
        after all on-off sequences, if the #
        of these sequences was odd, the bulb
        be on:
        ([off]->t1[on]->t2[off]->t3[on])

        otherwise if the # of these sequences
        is evven, it will be off:
        ([off]->t1[on]->t2[off]->t3[on]->t4[on])

        1 --------- 1

        2 --------- 1, 2

        3 --------- 1, 3

        4 --------- 1, 2, 4

        5 --------- 1, 5

        6 --------- 1, 2, 3, 6

        7 --------- 1, 7

        8 --------- 1, 2, 4, 8

        9 --------- 1, 3, 9

        notice that only perfect squares have off number of factors.
        we are interested in odd only because we gotta count 'ON bulbs'
        so we gotta count : HOW MANY perfect squares until n

        which is nothing but sqrt(n)


        """
        return int(math.sqrt(n))
