"""Python Skrit test satrovacki case"""
from skrit_r0073rr0r import skrit

def test_satrovacki():
    """Python Skrit test method"""
    hide = skrit.Skrit()
    assert hide.satrovacki("sranje"), "njesra"

if __name__ == "__main__":
    test_satrovacki()
    print("Everything passed")
