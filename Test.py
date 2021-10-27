class Test:
    """This is a test class with some attributes and some properties."""
    
    i_have_a_pen: int
    """It's a pen."""

    _i_have_an_apple: str

    def _get_apple(self) -> str:
        return self._i_have_an_apple

    def _set_apple(self, apple: str):
        self._i_have_an_apple = apple

    i_have_an_apple = property(_get_apple, _set_apple)
    """It's an apple."""

    _uh: str

    def _get_uh(self) -> str:
        return self._uh

    def _set_uh(self, uh: str):
        self._uh = uh
    
    uh = property(_get_uh, _set_uh)
    """Say it!"""

    apple_pen: int
    """It's an apple-pen!"""

