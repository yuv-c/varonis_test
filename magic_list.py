class MagicList(list):
    def __init__(self, **kwargs):
        super().__init__()
        self._cls_type = kwargs.get("cls_type")

    def __setitem__(self, i, item):
        if len(self) == i or i == -1:
            self.append(item)
        else:
            super().__setitem__(i, item)

    def __getattr__(self, item):
        return getattr(self._cls_type, item)
