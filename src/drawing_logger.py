
# Class that logs drawing operations to enable redo functionality
class DrawingLogger(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.hist = []
        self.undo_hist = []

    def __getattribute__(self, name: str):
        if name in ["hist", "undo_hist", "canvas", "undo", "redo"]:
            return object.__getattribute__(self, name)
        attr = getattr(self.canvas, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                special_id = kwargs.pop("special_id", None)
                result = attr(*args, **kwargs)
                self.hist.append((name, args, kwargs, result, special_id))
                return result
            return wrapper
        else:
            return attr

    def redo(self):
        if not self.undo_hist:
            return
        tup = self.undo_hist.pop()
        name, args, kwargs, result, special_id = tup
        result = getattr(self.canvas, name)(*args, **kwargs)
        self.hist.append((name, args, kwargs, result, special_id))
        for i in range(len(self.undo_hist)-1, -1, -1):
            name, args, kwargs, result, special_id2 = self.undo_hist[i]
            if special_id2 == special_id:
                result = getattr(self.canvas, name)(*args, **kwargs)
                self.undo_hist.pop()
                self.hist.append((name, args, kwargs, result, special_id2))
            else:
                break

    def undo(self):
        if not self.hist:
            return
        tup = self.hist.pop()
        self.undo_hist.append(tup)
        _, _, _, result, special_id = tup
        self.canvas.delete(result)
        for i in range(len(self.hist)-1, -1, -1):
            name, args, kwargs, result, special_id2 = self.hist[i]
            if special_id2 == special_id:
                self.canvas.delete(result)
                self.undo_hist.append(self.hist.pop(i))
            else:
                break
