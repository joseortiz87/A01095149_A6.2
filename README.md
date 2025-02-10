# A01095149_A6.2
6.2 Ejercicio de programación 3 y pruebas de unidad

## Pylint
```bash
m_853333@ambus119661 A01095149_A6.2 % pylint reservation_system.py
************* Module reservation_system
reservation_system.py:1:0: C0114: Missing module docstring (missing-module-docstring)
reservation_system.py:5:0: C0115: Missing class docstring (missing-class-docstring)
reservation_system.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:24:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:32:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:52:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:74:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:84:0: C0115: Missing class docstring (missing-class-docstring)
reservation_system.py:92:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:99:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:103:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:107:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:113:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:121:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:128:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:132:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:140:0: C0115: Missing class docstring (missing-class-docstring)
reservation_system.py:143:4: R0913: Too many arguments (7/5) (too-many-arguments)
reservation_system.py:152:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:163:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:164:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:168:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:172:17: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
reservation_system.py:178:4: C0116: Missing function or method docstring (missing-function-docstring)
reservation_system.py:178:4: R0913: Too many arguments (6/5) (too-many-arguments)
reservation_system.py:191:4: C0116: Missing function or method docstring (missing-function-docstring)
```


## Flake8
```bash
m_853333@ambus119661 A01095149_A6.2 % flake8 reservation_system.py
reservation_system.py:4:1: E302 expected 2 blank lines, found 1
reservation_system.py:6:1: W293 blank line contains whitespace
reservation_system.py:12:1: W293 blank line contains whitespace
reservation_system.py:25:1: W293 blank line contains whitespace
reservation_system.py:35:1: W293 blank line contains whitespace
reservation_system.py:39:80: E501 line too long (117 > 79 characters)
reservation_system.py:41:1: W293 blank line contains whitespace
reservation_system.py:51:1: W293 blank line contains whitespace
reservation_system.py:59:1: W293 blank line contains whitespace
reservation_system.py:69:1: W293 blank line contains whitespace
reservation_system.py:80:1: E302 expected 2 blank lines, found 1
reservation_system.py:82:1: W293 blank line contains whitespace
reservation_system.py:87:1: W293 blank line contains whitespace
reservation_system.py:89:80: E501 line too long (88 > 79 characters)
reservation_system.py:95:1: W293 blank line contains whitespace
reservation_system.py:109:80: E501 line too long (84 > 79 characters)
reservation_system.py:111:1: W293 blank line contains whitespace
reservation_system.py:115:80: E501 line too long (86 > 79 characters)
reservation_system.py:117:1: W293 blank line contains whitespace
reservation_system.py:121:1: W293 blank line contains whitespace
reservation_system.py:130:1: E302 expected 2 blank lines, found 1
reservation_system.py:132:1: W293 blank line contains whitespace
reservation_system.py:133:80: E501 line too long (101 > 79 characters)
reservation_system.py:140:1: W293 blank line contains whitespace
reservation_system.py:155:1: W293 blank line contains whitespace
reservation_system.py:167:80: E501 line too long (93 > 79 characters)
reservation_system.py:169:80: E501 line too long (181 > 79 characters)
reservation_system.py:171:1: W293 blank line contains whitespace
```

## Coverage
```bash
m_853333@ambus119661 A01095149_A6.2 % coverage run reservation_system_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.016s

OK
m_853333@ambus119661 A01095149_A6.2 % coverage report -m                     
Name                                                                                      Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------------------------
/Users/m_853333/Library/Python/3.8/lib/python/site-packages/_distutils_hack/__init__.py     101     96     5%   2-102, 112-240
reservation_system.py                                                                       139     17    88%   15, 30, 71, 78-80, 93, 105, 109-110, 122-125, 153, 170, 174-175
reservation_system_test.py                                                                   71      5    93%   24-28
-----------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                       311    118    62%
```