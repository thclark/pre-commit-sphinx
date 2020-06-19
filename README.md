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


## convert_bibliography

NOT IMPLEMENTED YET

If you have a bibliography (or citations, references, whatever you want to call them) in BibTeX format, and wish to use them in `.rst` documentation
you'll need to translate them in order to use those references in `rst` docs.

It's more convenient to maintain a bibtex file than a .rst citations file, because most reference managers can use and/or export bibtex.

This updates a `rst` based citations file any time a bibliography file changes.

You may wish to invoke this prior to the `build-docs` hook if you're also using that! 
Use in your `.pre-commit-config.yaml` file like:
```yaml
  - repo: https://github.com/thclark/pre-commit-sphinx
    rev: 0.0.1
    hooks:
      - id: convert-bibliography
        args: ['--input-file', 'docs/source/bibliography.bib', '--output-file', 'docs/source/bibliography.rst']
        language_version: python3
```
