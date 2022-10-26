from skrit_r0073rr0r import skrit

def test_satrovacki():
    a = skrit.skrit()
    assert a.Satrovacki("sranje"), "njesra"

if __name__ == "__main__":
    test_satrovacki()
    print("Everything passed")