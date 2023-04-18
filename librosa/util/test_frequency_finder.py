import sys
sys.path.insert(0, '~/Desktop/EECS/481/hw6/librosa/')
import utils


def test_frequency_range():
    print(utils.frequency_range('violin', True), "== [196.0, 1661.2]")
    assert utils.frequency_range('violin', True) == [196.0, 1661.2]
    print(utils.frequency_range('trumpet', False), "== [130.8, 1174.7]")
    assert utils.frequency_range('trumpet', False) == [130.8, 1174.7]
    print(utils.frequency_range('guitar', True), "== [82.4, 1318.5]")
    assert utils.frequency_range('guitar', True) == [82.4, 1318.5]
    print(utils.frequency_range('flute', False), "== [261.6, 2093.0]")
    assert utils.frequency_range('flute', False) == [261.6, 2093.0]
    print(utils.frequency_range('human voice', True), "== [85.0, 1100.0]")
    assert utils.frequency_range('human voice', True) == [85.0, 1100.0]
    print(utils.frequency_range('invalid instrument', True), "== None")
    assert utils.frequency_range('invalid instrument', True) == None
    print(utils.frequency_range('telephone', False), "== [300.0, 3400.0]")
    assert utils.frequency_range('telephone', False) == [300.0, 3400.0]
    print(utils.frequency_range('double bass', True)," == [41.2, 277.2]")
    assert utils.frequency_range('double bass', True) == [41.2, 277.2]
    print(utils.frequency_range('drums', True), "== [20.0, 16000.0]")
    assert utils.frequency_range('drums', True) == [20.0, 16000.0]
    print(utils.frequency_range('saxophone', True), "== [123.5, 1567.9]")
    assert utils.frequency_range('saxophone', True) == [123.5, 1567.9]
    print(utils.frequency_range('harp', False), "== [27.5, 1864.7]")
    assert utils.frequency_range('harp', False) == [27.5, 1864.7]
    # Empty input:
    print("Empty input")
    assert utils.frequency_range('', True) == None
    assert utils.frequency_range('', False) == None
    # Non-string input:
    print("Non-string input")
    assert utils.frequency_range(123, True) == None
    assert utils.frequency_range(True, False) == None
    # Invalid category:
    print("Invalid category")
    assert utils.frequency_range('glockenspiel', True) == None
    assert utils.frequency_range('glockenspiel', False) == None
    # Invalid subcategory:
    print("Invalid subcategory")
    assert utils.frequency_range('strings', True) == None
    assert utils.frequency_range('strings', False) == None
    # Voice category with invalid input:
    print("Voice category with invalid input")
    assert utils.frequency_range('voice', True) == None
    assert utils.frequency_range('voice', False) == None
    assert utils.frequency_range('alto voice', True) == None
    assert utils.frequency_range('soprano voice', False) == None
    # Partials category with invalid input:
    print("Partials category with invalid input")
    assert utils.frequency_range('partials', True) == None
    assert utils.frequency_range('partials', False) == None



test_frequency_range()