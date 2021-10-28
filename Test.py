from typing import TYPE_CHECKING, Optional



# if TYPE_CHECKING:
from multiple.levels.of.folders.code import Other
    


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
    """It's an apple.
    
    Using ``i_have_an_apple = property(_get_apple, _set_apple)`` and putting the docstring after that line.
    """

    _uh: str

    def _get_uh(self) -> str:
        """It's an uh.
        
        Using ``uh = property(_get_uh, _set_uh)`` and putting the docstring in the getter.
        """
        return self._uh

    def _set_uh(self, uh: str):
        self._uh = uh

    uh = property(_get_uh, _set_uh)

    _apple_pen: int

    @property
    def apple_pen(self) -> str:
        """It's an apple-pen!
        
        Using ``@property`` and ``@apple_pen.setter`` and putting the docstring in the "getter".
        """
        return self._uh

    @apple_pen.setter
    def apple_pen(self, apple_pen: str):
        self._uh = apple_pen

    def a_method(self, val: int, undoc: str) -> Optional["Other"]:
        """A method with a documented parameter and an undocumented parameter.

        :param val: a documented parameter
        """
        return None

