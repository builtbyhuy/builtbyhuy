# When a saved document style cannot be read back

Hồ Khắc Huy · September 6, 2026

A style name containing quotation marks could be created in `python-docx-ng`,
then fail when the application looked it up again. The name was valid document
data. The lookup was building an XPath expression by inserting that data into
the query text.

I fixed this in [PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131),
which the maintainer reviewed and merged on August 4. The useful lesson is in
the path between the public API and the XML library: changing one expression
was only part of the repair.

## A small reproduction

Here is a standalone illustration using `lxml`. It creates the XML through
the element API, so the example does not depend on hand-escaping XML text.

```python
from lxml import etree

styles = etree.Element("styles")
name = 'Review "Owner\'s copy"'
saved = etree.SubElement(styles, "style", name=name)

# The data becomes part of the XPath source.
styles.xpath(f'style[@name="{name}"]')
```

That last line raises `XPathEvalError`. The quotation marks in the name end
the string literal that the expression was trying to construct.

The XML can be perfectly valid while this second operation fails. XML
serialization and XPath expression construction are separate steps, with
separate syntax rules. Escaping a value correctly for the first step does not
make it safe to splice into the second.

Changing the expression to use single quotes would only change which input
breaks it. This particular name contains both kinds of quotation mark.

## Keep the expression fixed

`lxml` supports binding values to XPath variables:

```python
matches = styles.xpath("style[@name=$name]", name=name)
assert matches == [saved]
```

Now the expression describes the lookup, and the keyword argument supplies
its value. The quotation marks remain characters in the name. They do not
become query syntax. This is the variable mechanism documented in
[lxml's XPath guide](https://lxml.de/xpathxslt.html#the-xpath-method).

This change is scoped to values. If an application lets a caller supply an
entire XPath expression, passing a separate variable does not validate that
expression or define which parts of the document the caller may inspect.

## Follow the value through the wrapper

The package did not call `lxml` directly at every lookup. Its XML element base
class wrapped `xpath()` to supply the document's namespace mapping.

The wrapper also had to accept `**variables` and forward them to the underlying
XPath evaluator. Otherwise the corrected lookup could ask for a variable that
never reached the library responsible for evaluating it.

The patch preserved the existing namespace behavior: the standard document
prefixes remained available, and a caller could still supply additional
prefixes or override a mapping. A regression check combined a bound value with
a custom namespace so that those two features were exercised together.

Three lookups used the same problematic pattern: ordinary style names, style
IDs, and latent-style names. Updating just the first visible failure would
have left the other paths inconsistent. The patch changed all three to pass
values separately from their expressions.

## Test the promise made by the public API

The central regression was a round trip: create a style through the public
style collection, then retrieve it by the same name. A test confined to the
low-level XPath helper would not establish that the collection API actually
used the repaired path.

The submitted tests also covered low-level name and ID lookup, latent styles,
and variables used alongside a custom namespace. The upstream diff shows
those cases directly; the merged contribution is the evidence for that change.

For the simplified example in this note, I added a separate
[runnable reproduction](../examples/xpath_variables.py). It checks ordinary
text, single quotes, double quotes, both quote types, a bracketed name, and a
missing name. The missing-name case matters: the lookup should return no
match, rather than an unrelated element.

Those local checks verify this illustration. They are not a claim about every
XML parser, every release of the package, or a deployed customer system.

## A review question to reuse

When a stored value cannot be retrieved, trace how that value crosses each
representation: object, serialized data, query argument, and result. Check the
public round trip as well as the helper that appears to be failing. Small
correctness fixes often depend on preserving the contract between those layers.

---

I take on remote Python/TypeScript, API, and automation projects. If an existing
workflow is stuck, [email me](mailto:hohuyblon@gmail.com) with the current
behavior and the result you need. I can assess the fit and propose a concrete
first deliverable. [More public work](https://github.com/builtbyhuy).

This article describes my open-source contribution, not a client case study.
Written with AI assistance; source claims and the runnable example were checked.
