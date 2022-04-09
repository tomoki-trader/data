#__init__.pyにimportすることで、インスタンス形式で関数を呼べる。
from .api import show_today as date
__all__ = ["date"]