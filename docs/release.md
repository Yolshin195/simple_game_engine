# Release

## required
```commandline
    pip install twine
    pip install wheel  
```

## in testpypi
```commandline
    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/*
```

## in pypi
```commandline
    python setup.py sdist bdist_wheel
    twine upload --repository pypi dist/*
```

