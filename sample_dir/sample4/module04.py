__all__ = ['hello1', 'hello2']
#___all__はすべてのファイルで定義可能。
#form module04.py import *でimport される
#関数を制限しているに過ぎない。（使い道はないかも）
def hello1():
    print('this is helo1')

def hello2():
    print('this is hello2')

def hello3():
    print('this is hello3')