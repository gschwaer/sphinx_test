# Undocumented return type

Using
```python
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
```
suppresses type annotation for undocumented parameters and return values (only annotates `"documented"` elements).

This test shows a new option `"documented_params"`, which suppresses type annotation only for undocumented parameters. Return types are still added even if they are undocumented.


## Testing this

To build the html:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
```
