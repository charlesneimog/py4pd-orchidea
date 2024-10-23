## py4pd-orchidea

`py4pd-orchidea` allows to use Orchidea Sol inside PureData.

## List of Objects

`orchidea`:

  - **Methods**:
      - `get`: get valid configurations;
        - `key`: get all valid keys;
        - `inst`: get valid instruments keys;
        - `dyn`: set dynamic;
        - `...`
      - `set`: set configurations;
        - `inst`: set instruments;
        - `dyn`: set dynamic;
        - `...`
      - `sample`: get all samples that pass the filter setted;
      
<p align="center">
    <img width="80%" src=resources/help.png>
</p>
        
## Install

1. Create a new Pure Data patch.
2. Create a `py4pd` object.
3. Send a message with `pip install git+https://github.com/charlesneimog/py4pd-orchidea`.
4. Restart Pure Data.
5. Create a new object `py4pd -lib orchidea`.

All the objects must be avaiable to use now.

