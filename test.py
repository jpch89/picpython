def release(self):
    if self._owner != get_ident():
        raise RuntimeError("cannot release un-acquired lock")
    self._count = count = self._count - 1
    if not count:
        self._owner = None
        self._block.release()