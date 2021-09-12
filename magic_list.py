class MagicList(list):
    def __init__(self, **kwargs):
        super().__init__()
        self._cls_type = kwargs.get("cls_type")
        print("SELF: %s" % self)
        print("LEN: %s" % len(self))


    def __setitem__(self, i, item):
        if len(self) == i or i == -1:
            self.append(item)
        else:
            super().__setitem__(i, item)

    # def __getitem__(self, i):
    #     if len(self) == i or i == -1:
    #         self.append(self._cls_type())
    #     return super().__getitem__(i)


class A(object):
    def __init__(self):
        self.__prop = None

    @property
    def prop(self):
        return self.__prop

    @prop.setter
    def prop(self, value):
        self.__prop = value

class B(A):

    def __init__(self):
        super(B, self).__init__()

    @property
    def prop(self):
        value = A.prop.fget(self)
        value['extra'] = 'stuff'
        return value

    @prop.setter
    def prop(self, value):
        A.prop.fset(self, value)

if __name__ == "__main__":
    MagicList()
