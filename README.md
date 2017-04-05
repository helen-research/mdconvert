
`mdconvert` uses a notebook's metadata to configure `nbconvert` actions.

# Usage

(Edit > Edit Notebook Metadata) and add a `nbconvert` key a notebook's `metadata`; the `value` is a list of lists - the `export_format` & an object with [`configurables`](http://nbconvert.readthedocs.io/en/latest/config_options.html), respectively.

> Edit the `metadata` with a cell magic.


```python
%reload_ext mdconvert
```


```python
%%metadata
nbconvert:
    - [markdown, {}]
```


    <IPython.core.display.Javascript object>



```python
!jupyter mdconvert README.ipynb
```

    <class 'list'>
    [NbConvertApp] Converting notebook README.ipynb to html
    [MDConvertApp] Writing 613 bytes to README.md
    [NbConvertApp] Conversions completed in 0.1194000244140625 seconds.



```python

```


```python
!jupyter serverextension enable --py jawn
```


```python
import mdconvert
```
