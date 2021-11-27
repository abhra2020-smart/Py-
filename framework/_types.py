from .errors import *

Number = int | float
fastbool_convert = lambda x: not not x


class Object:
    def __new__(cls, *args, **kwargs):
        try:
            return object.__new__(cls)
        except:
            raise MemError("Not enough memory to create Object")
