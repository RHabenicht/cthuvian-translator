"""Provisional word lookup from a public R'lyehian fan lexicon."""
import argparse
import json
import re
import unicodedata
from functools import lru_cache
from importlib.resources import files

TOKENS = re.compile(r"[^\W\d_]+(?:[\u0300-\u036f]+)?(?:[\u2019'-][^\W\d_]+(?:[\u0300-\u036f]+)?)*|\s+|.", re.UNICODE)

@lru_cache(maxsize=1)
def data():
    with files("rlyehian_reference").joinpath("data/lexicon.json").open(encoding="utf-8") as f:
        return json.load(f)

def normalize(term):
    return unicodedata.normalize("NFC", term).replace("’", "'").casefold()

def lookup(term):
    return data()["entries"].get(normalize(term), [])

def analyze(text):
    """Preserve punctuation; flag ambiguous/unmapped tokens without inventing words."""
    tokens = TOKENS.findall(text)
    terms = data()["entries"]
    out, issues = [], []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.isspace() or not any(c.isalpha() for c in t):
            out.append(t)
            i += 1
            continue
        key, count = normalize(t), 1
        for n in range(min(7, len(tokens)-i), 1, -1):
            candidate = ''.join(tokens[i:i+n])
            if '\n' not in candidate and normalize(candidate) in terms:
                key, count = normalize(candidate), n
                break
        original = ''.join(tokens[i:i+count])
        forms = terms.get(key, [])
        if len(forms) == 1:
            out.append(forms[0])
        else:
            out.append(f'⟦{original}?⟧')
            issues.append({'term':original,'type':'ambiguous' if forms else 'unknown','forms':forms})
        i += count
    return {'gloss': ''.join(out), 'issues': issues}

def main(argv=None):
    p=argparse.ArgumentParser(description="R'lyehian public-source lexical lookup")
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('lookup').add_argument('term')
    sub.add_parser('translate').add_argument('text')
    sub.add_parser('sources')
    args=p.parse_args(argv)
    if args.command=='lookup': print(json.dumps({'term':args.term,'forms':lookup(args.term)},ensure_ascii=False,indent=2))
    elif args.command=='translate':
        print('PROVISIONAL LEXICAL GLOSS (not a completed translation)')
        print(json.dumps(analyze(args.text),ensure_ascii=False,indent=2))
    else: print(json.dumps(data()['source'],indent=2,ensure_ascii=False))

if __name__ == '__main__':
    main()
