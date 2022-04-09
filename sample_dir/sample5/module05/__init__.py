#print("in __init__.py")
#__init__.pyでの同ディレクトリのファイル名の表記方法は
#cd "."を明記する。
from .module05 import hello as hello05
from .module06 import hello as hello06
#ワイルドカードで呼び出し可能な関数の定義
__all__ = ["hello05", 'hello06']

#hello05("__init__.py")
#hello06("__init__.py")