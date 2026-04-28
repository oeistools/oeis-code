# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-04-28

### Added
- Initial release of `oeis-code`.
- Core `get(seq_id, n, backend)` API for retrieving OEIS sequence terms.
- Sequence registry with `@register` decorator.
- Python and PARI/GP dual-backend architecture (`backend="auto"` / `"python"` / `"pari"`).
- Implemented sequences:
  - **A000040** — Prime numbers.
  - **A000045** — Fibonacci numbers.
  - **A000120** — 1's-counting sequence (Hamming weight).
  - **A016993** — `a(n) = 7n + 1`.
  - **A017053** — `a(n) = 7n + 6`.
  - **A066096** — Lower Wythoff sequence (`floor(n·φ)`).
- `utils.math` module with `is_prime` and `fibonacci_term` helpers.
- Full CI with GitHub Actions (multi-Python matrix, ruff lint, codecov).
- MkDocs Material documentation deployed to GitHub Pages.
- SPDX license headers across all source files.

[Unreleased]: https://github.com/oeistools/oeis-code/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/oeistools/oeis-code/releases/tag/v0.1.0
