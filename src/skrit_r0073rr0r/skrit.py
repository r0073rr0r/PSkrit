"""Python Skrit module"""
class Skrit:
    """Python Skrit module INIT"""
    def __init__(self):
        self._samoglasnici = [
            'a', 'e', 'i', 'o',
            'u', 'r', 'A', 'E',
            'I', 'O', 'U', 'R',
            'а', 'е', 'и', 'о', 'у',
            'р', 'А', 'Е', 'И', 'О',
            'У', 'Р'
        ]
        self._serbian_letters_dvoslov = [
            ['l', 'j'], ['n', 'j'], ['s', 'h'],
            ['d', 'j'], ['d', 'z'], ['d', 'ž'],
        ]
        self._serbian_letters_dvoslov_fix = [
            'lj', 'nj', 'sh',
            'dj', 'dz', 'dž',
        ]

    def __call__(self, input_string):
        return self.satrovacki(input_string)

    def is_odd(self, input_string):
        """Python Skrit check if letter is odd"""
        return True if input_string % 2 else False

    def is_samoglasnik(self, input_string):
        """Python Skrit samoglasnik check"""
        for letter in self._samoglasnici:
            return input_string.find(letter) > 0
        return False

    def is_serbian_letter(self, lista, hlf_list, cnt_list):
        """Python Skrit check word for dvoslov"""
        poslednja_dva = lista[hlf_list-2:hlf_list]
        zadnja_dva = lista[cnt_list-2:cnt_list]
        # print({
        #     "ZD": zadnja_dva,
        #     "PZ": poslednja_dva
        # })
        for letter in self._serbian_letters_dvoslov:
            if letter == poslednja_dva:
                return True
            if letter == zadnja_dva:
                return True
        return False

    # satrovacki method
    def satrovacki(self, input_string):
        """Python Skrit satrovacki"""
        lista = list(input_string)
        cnt_list = len(lista)
        hlf_list = round(cnt_list/2)
        # pair = self.is_odd(cnt_list)
        # ima_dvoslov = self.is_serbian_letter(lista, hlf_list, cnt_list)
        # output = None
        # print({
        #     "L:": lista, "Length": str(cnt_list),
        #     "Half": str(hlf_list), "Pair": str(pair),
        #     "LastInHalf": str(lista[hlf_list]),
        #     "Dvoslov": ima_dvoslov
        # })
        #
        # @TODO samoglasnici and serbian letters to parse:
        #  pishtolj or pištolj as štoljpi or shtoljpi
        #
        output = input_string[hlf_list:cnt_list]
        output += input_string[0:hlf_list]
        return output

# hide = Skrit()
# print(hide.satrovacki("pishtolj"))
