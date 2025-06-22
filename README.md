# Pyright-cov

## Enforce minimum type coverage!

`pyright-cov` is a tool which you can use to enforce minimum type coverage in your projects.

![image](https://github.com/user-attachments/assets/03977f7d-ee29-45f1-b8a9-306ec539f8cf)

## Installation

```console
pip install pyright-cov
```

## Usage

In a virtual environment in which you have a local install of a library `foo`, you can
ensure that `foo` is type-complete with:

```
pyright-cov --verifytypes foo --ignoreexternal
```

This will fail (i.e. exit `1`) if your type coverage is less than 100%. To set a lower
threshold, such as 60%:

```
pyright-cov --verifytypes foo --ignoreexternal --fail-under 60
```

To exclude symbols whose names match a given (glob) pattern, use `--excludelike`, for example:

```
pyright-cov --verifytypes foo --ignoreexternal --excludelike "*.tests.*"
```

Additional command-line flags are passed to [Pyright](https://github.com/microsoft/pyright).

## Used by

- [Narwhals](https://github.com/narwhals-dev/narwhals)

## Testing

Make sure you have `uv` and `pytest` installed. Then, run:

```
pytest tests
```

