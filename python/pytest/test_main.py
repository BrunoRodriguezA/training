from ex3 import unicos_en_orden, unicos_en_orden_nohash

def test_unicos_en_orden():
    assert unicos_en_orden([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert unicos_en_orden(["a", "a", "b", "A"]) == ["a", "b", "A"]
    assert unicos_en_orden(["á", "á", "b", "A"]) == ["á", "b", "A"]
    assert unicos_en_orden(["á", "á",1, "b", "A", 0, 0, 1]) == ["á", 1, "b", "A", 0]
    assert unicos_en_orden([""]) == [""]
    assert unicos_en_orden_nohash(["a", "a", "b", "A", [1]]) == ["a", "b", "A", [1]]









