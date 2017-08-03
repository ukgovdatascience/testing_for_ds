from words import extract_words

def test_extract_words():
    assert extract_words(
        'Mary had a little lamb, its fleece was white as snow') == \
        'Mary little lamb its fleece white snow'.split()
