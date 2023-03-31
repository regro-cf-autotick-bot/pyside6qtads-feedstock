FILES = [
    'CMakeLists.txt',
    'setup.cfg',
    'setup.py',
    'src/bindings.xml',
    'init.py'
]

print('## Starting replace Qt6/PySide6 by Qt5/PySide2')
for fname in FILES:
    print('### Processing ', fname, end='')
    with open(fname, 'r') as f:
        data = f.read()
        
    data = data.replace('PySide6::pyside6', 'PySide2::pyside2')
    data = data.replace('PySide6 6.0.0', 'PySide2 2.0.0')
    data = data.replace('PySide6', 'PySide2')
    data = data.replace('pyside6qtads', 'pyside2qtads')
    data = data.replace('Shiboken6 6.0.0', 'Shiboken2 2.0.0')
    data = data.replace('Shiboken6', 'Shiboken2')
    data = data.replace('shiboken6', 'shiboken2')
    data = data.replace('Qt6', 'Qt5')
    data = data.replace('QT6', 'QT5')
    data = data.replace('qt6advanceddocking', 'qt5advanceddocking')
    
    with open(fname, 'w') as f:
        f.write(data)
        
    print('OK')
print('## Qt6/PySide6 successfully replaced by Qt5/PySide2')