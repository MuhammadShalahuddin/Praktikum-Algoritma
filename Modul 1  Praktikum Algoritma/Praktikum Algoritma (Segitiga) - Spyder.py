# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:09:43 2022

@author: Muhammad Shalahuddin
"""

panjang = float (input("panjang ruangan?"))
lebar = float (input("lebar ruangan?"))
satuan = str (input("satuannya (meter/inchi)"))
hasil = panjang*lebar
print("luas ruangan dengan panjang", panjang)
print("dan lebar",lebar)
print("adalah ", float (hasil),(satuan))