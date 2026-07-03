#!/usr/bin/env python3
# clc.py
# CaLCulator
import sys, os
cut='''
=========================
'''
rcut='''
====== R E S U L T ======
'''
ercut='''
======= E R R O R =======
'''
hello='''
Available operations: [+] [-] [*] [**] [/]'''
ops=('+','-','*','**','/')
def cl():
    os.system('cls'if os.name=='nt'else'clear')
def main():
    try:
        while True:
            while True:
                cl()
                print(hello)
                print(cut)
                try:
                    a=float(input(f'1st number: '))
                except ValueError:
                    cl()
                    continue
                try:
                    op=input(f'Operation: ')
                    if op in ops:
                        pass
                    else:
                        cl()
                        continue
                except ValueError:
                    cl()
                    continue
                try:
                    b=float(input(f'2nd number: '))
                except ValueError:
                    cl()
                    continue
                    
                if op in ops:
                    if op==ops[0]:
                        c=a+b
                        print(rcut)
                        print(c)
                        print(rcut)
                        c=0
                        usr_cnt=input(f'\n[A]gain / [Q]uit ').strip().lower()
                    if op==ops[1]:
                        c=a-b
                        print(rcut)
                        print(c)
                        print(rcut)
                        c=0
                        usr_cnt=input(f'\n[A]gain / [Q]uit ').strip().lower()
                    if op==ops[2]:
                        c=a*b
                        print(rcut)
                        print(c)
                        print(rcut)
                        c=0
                        usr_cnt=input(f'\n[A]gain / [Q]uit ').strip().lower()
                    if op==ops[3]:
                        c=a**b
                        print(rcut)
                        print(c)
                        print(rcut)
                        c=0
                        usr_cnt=input(f'\n[A]gain / [Q]uit ').strip().lower()
                    if op==ops[-1]:
                        if b==0:
                            print(ecut)
                            print(f"! YOU CAN'T DIVIDE BY ZERO! ")
                            input(f'\nPress ENTER to continue... ')
                            print(ecut)
                            cl()
                            continue
                        else:
                            c=a/b
                            print(rcut)
                            print(c)
                            print(rcut)
                            c=0
                            usr_cnt=input(f'\n[A]gain / [Q]uit ').strip().lower()
                    if usr_cnt=='a':
                        cl()
                        break
                    else:
                        sys.exit()
    except KeyboardInterrupt:
        print(f'\nCLC has been stopped... ')
    except Exception as e:
        print(f'\n[ERROR] -> {e} ')
main()
