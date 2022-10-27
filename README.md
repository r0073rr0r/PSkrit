# PSkrit

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/skrit-r0073rr0r)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/skrit-r0073rr0r)
[![GitHub forks](https://img.shields.io/github/forks/r0073rr0r/PSkrit)](https://github.com/r0073rr0r/PSkrit/network)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/skrit-r0073rr0r)
[![PyPI version](https://badge.fury.io/py/skrit-r0073rr0r.svg)](https://badge.fury.io/py/skrit-r0073rr0r)
[![GitHub issues](https://img.shields.io/github/issues/r0073rr0r/PSkrit)](https://github.com/r0073rr0r/PSkrit/issues)
[![GitHub stars](https://img.shields.io/github/stars/r0073rr0r/PSkrit)](https://github.com/r0073rr0r/PSkrit/stargazers)

## Install

```
pip install skrit-r0073rr0r
``` 

or

```
pip install -i https://test.pypi.org/simple/ skrit-r0073rr0r
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