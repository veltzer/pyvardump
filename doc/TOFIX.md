# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `tera.snippets/main.md.tera:10` - the README says the module "just exports one function \"dump\"", but there is no `dump` function; `src/pyvardump/__init__.py:5` exports `dump_print`, `dump_pprint` and `dump_json`. Update the snippet to describe the real API.
- `src/pyvardump/dump.py:17` - `dump_obj` and `dump_obj_2` (line 37) recurse without tracking visited objects, so any self-referencing object raises `RecursionError` (verified with `a.me = a`); keep a `seen` set of `id()`s and stop on revisits.
- `src/pyvardump/dump.py:58` - `dump_json` calls `json.dump` without `default=`, so it raises `TypeError` for any non-JSON object, defeating the README's promise to dump objects that other tools choke on; pass `default=default_func` (line 46) or `object_to_members_or_string` (line 61), which are currently only used by tests.
- `pyproject.toml:84` - the mypy override sets `ignore_missing_imports` for `pyvardump.*`, the package itself, not a third-party library as the comment claims; a config-level suppression with no reason - remove it.

## Low

- `src/pyvardump/dump.py:23` - hard-coded skip of `adjustments` / `auto_shape_type` is a leftover from debugging python-pptx shapes; remove it or make the skip list a parameter.
- `src/pyvardump/dump.py:28` - `dump_obj` prints values without their attribute names, so the output cannot be mapped back to fields; print `f"{a} -> {val}"` like `flat_dump` does.
- `tera.templates/test.txt.tera:1` - an experiment template ("has cargo"/"no cargo") that renders the committed `test.txt`; delete both.
- `src/pyvardump/__init__.py:5` - `# noqa F401` lacks the colon, so ruff treats it as a blanket `noqa`; use `__all__` instead of the suppression.
- `doc/TODO.txt:1` - the file is empty; delete it.
