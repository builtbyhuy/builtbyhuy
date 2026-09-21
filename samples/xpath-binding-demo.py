"""Small regression reproducer inspired by python-docx-ng PR #131.

Run: python xpath-binding-demo.py (requires lxml).
Synthetic XML only; not the upstream repository's test suite.
"""
from lxml import etree
import sys

cases = ["Plain Style", "O'Brien", 'He said "hello"', 'He said "it\'s fine" [today]']
print('XPATH VARIABLE-BINDING REPRODUCER — SYNTHETIC XML')
print('Python: '+sys.version.split()[0])
failures = 0
for value in cases:
    root=etree.Element('styles')
    target=etree.SubElement(root,'style',name=value)
    try:
        old=root.xpath(f'style[@name="{value}"]')
        old_result='MATCH' if old==[target] else 'NO MATCH'
    except etree.XPathError:
        old_result='XPathError'
    bound=root.xpath('style[@name=$name]', name=value)
    passed=bound==[target]
    failures+=not passed
    print(f'{"PASS" if passed else "FAIL"}: {value!r}; interpolated={old_result}; bound={"MATCH" if passed else "NO MATCH"}')
print(f'Result: {len(cases)-failures}/{len(cases)} bound-variable cases passed.')
print('Scope: demonstrates the binding mechanism; does not rerun the upstream suite or prove all style APIs.')
raise SystemExit(1 if failures else 0)
