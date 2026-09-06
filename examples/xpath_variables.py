"""Run with Python and lxml installed: python examples/xpath_variables.py."""
from lxml import etree


def main():
    names = [
        "Heading",
        "Owner's copy",
        'Review "Draft"',
        'Review "Owner\'s copy"',
        "Heading [draft]",
    ]
    styles = etree.Element("styles")
    expected = {name: etree.SubElement(styles, "style", name=name) for name in names}

    for name, saved in expected.items():
        matches = styles.xpath("style[@name=$name]", name=name)
        assert matches == [saved], (name, matches)
    assert styles.xpath("style[@name=$name]", name="Not present") == []

    name = names[3]
    try:
        styles.xpath(f'style[@name="{name}"]')
    except etree.XPathEvalError:
        print("Interpolated expression: reproduced XPathEvalError")
    else:
        raise AssertionError("Expected the interpolated expression to fail")

    print("Bound values: 5 exact matches; 1 missing name returns no match")
    print(f"Runtime: lxml {etree.LXML_VERSION}; libxml2 {etree.LIBXML_VERSION}")


if __name__ == "__main__":
    main()
