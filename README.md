# R’lyehian Lexical Reference

An open-source Python command-line tool for exploring English-to-R’lyehian vocabulary from the public [JLDevOps/Rlyehian](https://github.com/JLDevOps/Rlyehian) fan lexicon.

**Current scope:** A sourced vocabulary lookup and provisional lexical glossing tool—not a complete language, verified grammar, pronunciation guide, or fluent translator.

## Main features

- **English-to-R’lyehian word lookup:** Find recorded source forms for individual English terms.
- **Provisional text glossing:** Replace recognized words and expressions with their listed equivalents without inventing missing vocabulary.
- **Multiword phrase recognition:** Match entries such as `cross over` before processing individual words.
- **Ambiguity detection:** Display unresolved markers and alternatives when an English term has multiple source forms, rather than silently choosing one.
- **Unknown-word reporting:** Mark words missing from the reference dictionary as `⟦term?⟧`.
- **Formatting preservation:** Retain punctuation, whitespace, and line breaks in gloss output.
- **Documented source data:** Load 92 English entries extracted from one pinned upstream revision, with its license preserved.
- **Automated checks:** Run unit tests locally or through the included GitHub Actions workflow.

## Requirements

- Python 3.10 or later
- No third-party Python packages

## Getting started

Clone the repository and run these commands from its root directory:

```sh
python -m rlyehian_reference lookup "call"
python -m rlyehian_reference translate "cross over, soul!"
python -m rlyehian_reference sources
```

### Commands

| Command | What it does |
| --- | --- |
| `lookup "word"` | Returns every recorded R’lyehian form for an English entry, as JSON. |
| `translate "text"` | Produces a provisional gloss and reports ambiguous or unknown terms, as JSON. |
| `sources` | Displays the source repository, pinned revision, and license metadata. |

The `translate` command is named for discoverability; its output is **not** a complete semantic translation.

### Examples

```sh
python -m rlyehian_reference lookup "soul"
```

```json
{
  "term": "soul",
  "forms": ["orr'e"]
}
```

```sh
python -m rlyehian_reference translate "cross over, soul!"
```

The provisional gloss contains:

```text
ch', orr'e!
```

For an ambiguous lookup such as `call`, the reference data records both `'ai` and `uln`. The tool flags the term rather than selecting one without sufficient context.

## Vocabulary and research method

The bundled [lexicon](rlyehian_reference/data/lexicon.json) contains **92 English entries** extracted from the public upstream CSV at [revision `482bd14`](https://github.com/JLDevOps/Rlyehian/commit/482bd14e19d6a25094af800e6e2a65836484d319).

Only records labeled as standalone `word` entries are imported. One source entry was omitted from this derivative dataset. Distinct source spellings for the same English term are preserved as alternatives. The upstream material is a **fan-maintained glossary**, not an authoritative Lovecraftian dictionary.

The database and executable do not provide sentence grammar, morphology, tense, contextual disambiguation, or pronunciation. These would require separate, explicitly sourced design and validation before implementation.

## Testing

```sh
python -m unittest discover -s tests -v
```

The included GitHub Actions workflow runs the test suite on pushes and pull requests.

## Source and licensing

- **Upstream vocabulary:** [JLDevOps/Rlyehian](https://github.com/JLDevOps/Rlyehian)
- **Pinned data file:** [kadishtuor.csv at revision `482bd14`](https://github.com/JLDevOps/Rlyehian/blob/482bd14e19d6a25094af800e6e2a65836484d319/rlyehian/kadishtuor.csv)
- **Upstream license:** MIT; preserved in [`third_party/JLDevOps-LICENSE.txt`](third_party/JLDevOps-LICENSE.txt)

The code in this repository is licensed under the root [MIT license](LICENSE). The upstream vocabulary is separately provided under its original MIT license; retain the original notice when redistributing it.
