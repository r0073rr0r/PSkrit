# PSkrit

## Install

```
pip install skrit-r0073rr0r
``` 

or

```
pip install -i https://test.pypi.org/simple/ skrit-r0073rr0r==0.1.9
``` 

## Features

- [ ] Litrovacki
- [ ] Utrovachki
- [x] Satrovacki (need upgrade for samoglasnici and serbian letters)


## Example:

```
from skrit_r0073rr0r import skrit
print(skrit.Skrit().satrovacki('rucka'))
```

***Output***:

`` ckaru ``