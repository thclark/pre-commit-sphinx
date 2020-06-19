# pre-commit-sphinx
A pre-commit hook that will fail if documentation (eg for [readthedocs.io](https://www.readthedocs.io)) can't be built using sphinx

Using [pre-commit](https://pre-commit.com/#new-hooks)


## build_docs

Builds documentation using sphinx, returns PASSED to pre-config if the documentation compiles (even with warnings)

Use in your `.pre-commit-config.yaml` file like:
```yaml
  - repo: https://github.com/thclark/pre-commit-sphinx
    rev: 0.0.1
    hooks:
      - id: build-docs
        args: ['--cache-dir', 'docs/doctrees', '--html-dir', 'docs/html', '--source-dir', 'docs/source']
        language_version: python3
```

