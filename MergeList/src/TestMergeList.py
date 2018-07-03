#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrMergeList as corr
import mergeList


class TestMergeList(unittest.TestCase):
    def test_empty(self):
        ans = _("The lists may be empty.")
        stud_ans = mergeList.merge([], [])
        self.assertEqual([], stud_ans, ans)
        
    def test_only_one(self):
        ans = _("One list may be empty.")
        my_list = [['Charles', random.randint(40, 50)],
                   ['Siegfried', random.randint(50, 60)],
                   ['Kim', random.randint(60, 70)]]
        stud_ans1 = mergeList.merge(my_list, [])
        self.assertEqual(my_list, stud_ans1, ans)
        
    def test_merge_list(self):
        ans = _("The two lists are {} and {} and you returned {}.")
        my_list1 = [['Charles', random.randint(20, 50)],
                    ['Siegfried', random.randint(50, 70)],
                    ['Kim', random.randint(70, 90)]]
        my_list2 = [['Olivier', random.randint(40, 50)],
                    ['Peter', random.randint(50, 60)],
                    ['Yves', random.randint(60, 70)]]
        stud_ans1 = mergeList.merge(my_list1, my_list2)
        correct = corr.merge(my_list1, my_list2)
        self.assertEqual(correct, stud_ans1, ans.format(my_list1, my_list2, correct))
