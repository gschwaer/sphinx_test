# Long types

Sphinx processes type hints differently depending on

* the use of quotes on type hints (`"Type" vs Type`),
* if `__future__.annotations` is present, and
* on the type of import
    * plain import: `import module`
    * from import: `from module import name`
    * type checking import:
      ```python
      from typing import TYPE_CHECKING
      if TYPE_CHECKING:
          from module import name
      ```

In some cases the full canonical path including all levels of module path is
shown (like: `module.Name`), some others show only the class name
(like: `Name`). Some of the combinations also break links.

Here is what I found:
```
                                | __future__.annotations  | no __future__.annotations |
                                |  unquoted   |  quoted   |  unquoted    |   quoted   |
--------------+-----------------+-------------+-----------+--------------+------------|
plain import  | module function |    F, L     |   F, L    |     F, L     |    F, L    |
              | class attribute |    F, L     |   F, L    |     F, L     |    F, L    |
              | class property  |    F, L     |   F, L    |     F, L     |    F, L    |
              | class method    |    F, L     |   F, L    |     F, L     |    F, L    |
from import   | module function |    F, L     |   C, L    |     F, L     |    F, L    |
              | class attribute |    F, L     |   C, N    |     F, L     |    F, L    |
              | class property  |    F, L     |   C, N    |     F, L     |    F, L    |
              | class method    |    F, L     |   C, L    |     F, L     |    F, L    |
type checking | module function |    C, L     |   C, L    |     n/a      |    C, L    |
              | class attribute |    C, N     |   C, N    |     n/a      |    C, N    |
              | class property  |    C, N     |   C, N    |     n/a      |    C, N    |
              | class method    |    C, L     |   C, L    |     n/a      |    C, L    |
```

`F` == full path,
`C` == class-only,
`L` == link works,
`N` == no link,
`n/a` == does not apply (`__future__.annotations` is required)

**Observations:**

* Plain imports always generate canonical paths and working links.
* with future annotations, quoted types that were imported with the from-import
  schema behave differently that unquoted types and some links are broken
* the same behavior occurs if type checking imports are used no matter if quoted
  or not

## Testing this

To build the html:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
```
