from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from Test import Test

class Other:
    """What a deep class definition!"""

    with_an_attribute: str
    """which is an attribute"""

    class InAClass:
        """A class in a class."""

        def with_a_method(self) -> "Test":
            """just a method"""
            return Test()
