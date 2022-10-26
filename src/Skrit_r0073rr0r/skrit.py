"""Python Skrit module."""
class Skrit:
    """Python Skrit module INIT."""
    def __init__(self):
        self._samoglasnici = [
            'a', 'e', 'i', 'o',
            'u', 'r', 'A', 'E',
            'I', 'O', 'U', 'R'
        ]
        self._serbian_letters = [
            ['l', 'j'], ['n', 'j'], ['s', 'h'],
            ['d', 'j'], ['d', 'z'], ['d', 'ž'],
            'ž'
        ]

    def __call__(self, input_string):
        return self.satrovacki(input_string)

    def is_odd(self, input_string):
        """Python Skrit check if letter is odd."""
        return input_string % 2

    # Check if letter is Samoglasnik
    def is_samoglasnik(self, input_string):
        """Python Skrit samoglasnik check"""
        for letter in self._samoglasnici:
            return input_string.find(letter) > 0
        return False

    # Check if letter is Serbian Letter
    def is_serbian_letter(self, input_string):
        """Python Skrit serbian letter check"""
        for letter in self._serbian_letters:
            return input_string.find(letter) > 0
        return False

    # satrovacki method
    def satrovacki(self, input_string):
        """Python Skrit satrovacki."""
        lista = list(input_string)
        cnt_list = len(lista)
        hlf_list = round(cnt_list/2)
        pair = self.is_odd(cnt_list)
        output = None
        print({
            "L:": lista, "Length": str(cnt_list),
            "Half": str(hlf_list), "Pair": str(pair),
            "LastInHalf": str(lista[hlf_list])
        })
        #
        # @TODO samoglasnici and serbian letters to parse:
        #  pishtolj or pištolj as štoljpi or shtoljpi
        #
        output = input_string[hlf_list:cnt_list]
        output += input_string[0:hlf_list]
        return output
