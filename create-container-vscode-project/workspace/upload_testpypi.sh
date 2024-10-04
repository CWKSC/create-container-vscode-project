python3 -m twine upload \
    --config-file .pypirc \
    --repository testpypi \
    --verbose \
    dist/*
