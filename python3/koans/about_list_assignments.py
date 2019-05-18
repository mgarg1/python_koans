#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["J", "S"]
        self.assertEqual(["J", "S"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["S", "R", "B", "W"]
        self.assertEqual("S", title)
        self.assertEqual(["R","B"], first_names)
        self.assertEqual("W", last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["W", "R"], "J"]
        self.assertEqual(["W", "R"], first_name)
        self.assertEqual("J", last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "R"
        last_name = "S"
        first_name, last_name = last_name, first_name
        self.assertEqual("S", first_name)
        self.assertEqual("R", last_name)

