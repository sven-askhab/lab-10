#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
   u = set("abcdefghijklmnopqrstuvwxyz")
   
   a = {"a", "f", "I", "n", "o"}
   b = {"f", "g", "o", "p", "z"}
   c = {"i", "j", "u", "w"}
   d = {"f", "h", "n", "t", "u", "y", "z"}
   
   x = (a.intersection(b)).union(c)
   print(f"x = {x}")
   
   an = u.difference(a)
   bn = u.difference(b)
   
   y = (an.intersection(bn)).difference(c.union(d))
   print(f"y = {y}")