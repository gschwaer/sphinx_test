"""I annotated on every method/attribute/property if the full (canonical) path
or just the class was shown. The default test case is with
``from __future__ import annotations`` present. In brackets I noted if the
result changes in case this import is commented out."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, cast



from multiple.levels.of.folders.code import FromImport

import multiple.levels.of.folders.code

if TYPE_CHECKING:
    from multiple.levels.of.folders.code import CheckingFromImport





def test_plain_import() -> multiple.levels.of.folders.code.PlainImport:
    pass

class TestPlainImport:
    test_attr_opt: Optional[multiple.levels.of.folders.code.PlainImport] = None

    def _get_prop_opt(self) -> Optional[multiple.levels.of.folders.code.PlainImport]:
        return self._prop_opt

    def _set_prop_opt(self, p: Optional[multiple.levels.of.folders.code.PlainImport]):
        self._prop_opt = p

    test_prop_opt = property(_get_prop_opt, _set_prop_opt)

    def test_meth(self, a: multiple.levels.of.folders.code.PlainImport) -> multiple.levels.of.folders.code.PlainImport:
        pass


def test_plain_import_quoted() -> "multiple.levels.of.folders.code.PlainImport":
    pass

class TestPlainImportQuoted:
    test_attr_opt: Optional["multiple.levels.of.folders.code.PlainImport"] = None

    def _get_prop_opt(self) -> Optional["multiple.levels.of.folders.code.PlainImport"]:
        return self._prop_opt

    def _set_prop_opt(self, p: Optional["multiple.levels.of.folders.code.PlainImport"]):
        self._prop_opt = p

    test_prop_opt = property(_get_prop_opt, _set_prop_opt)

    def test_meth(self, a: "multiple.levels.of.folders.code.PlainImport") -> "multiple.levels.of.folders.code.PlainImport":
        pass






def test_from_import() -> FromImport:
    pass

class TestFromImport:
    test_attr_opt: Optional[FromImport] = None

    def _get_prop_opt(self) -> Optional[FromImport]:
        return self._prop_opt

    def _set_prop_opt(self, p: Optional[FromImport]):
        self._prop_opt = p

    test_prop_opt = property(_get_prop_opt, _set_prop_opt)

    def test_meth(self, a: FromImport) -> FromImport:
        pass


def test_from_import_quoted() -> "FromImport":
    pass

class TestFromImportQuoted:
    test_attr_opt: Optional["FromImport"] = None

    def _get_prop_opt(self) -> Optional["FromImport"]:
        return self._prop_opt

    def _set_prop_opt(self, p: Optional["FromImport"]):
        self._prop_opt = p

    test_prop_opt = property(_get_prop_opt, _set_prop_opt)

    def test_meth(self, a: "FromImport") -> "FromImport":
        pass






try:
    # This whole example is not valid without __future__.annotations.

    def test_from_import_checking() -> CheckingFromImport:
        pass

    class TestCheckingFromImport:
        test_attr_opt: Optional[CheckingFromImport] = None

        def _get_prop_opt(self) -> Optional[CheckingFromImport]:
            return self._prop_opt

        def _set_prop_opt(self, p: Optional[CheckingFromImport]):
            self._prop_opt = p

        test_prop_opt = property(_get_prop_opt, _set_prop_opt)

        def test_meth(self, a: CheckingFromImport) -> CheckingFromImport:
            pass

except NameError:
    pass


def test_from_import_quoted_checking() -> "CheckingFromImport":
    pass

class TestCheckingFromImportQuoted:
    test_attr_opt: Optional["CheckingFromImport"] = None

    def _get_prop_opt(self) -> Optional["CheckingFromImport"]:
        return self._prop_opt

    def _set_prop_opt(self, p: Optional["CheckingFromImport"]):
        self._prop_opt = p

    test_prop_opt = property(_get_prop_opt, _set_prop_opt)

    def test_meth(self, a: "CheckingFromImport") -> "CheckingFromImport":
        pass
