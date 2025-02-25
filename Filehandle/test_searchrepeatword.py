from searchrepeatword import Dataextractor

def test_searchrepeatedword():
    data = Dataextractor("testfile.txt")
    res = data.search()
    #assert res == "the"
    assert res == "work"