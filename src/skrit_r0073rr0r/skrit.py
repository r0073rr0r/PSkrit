"""Module providing cyrillic to latin and vice versa convertint."""
import cyrtranslit

class Skrit:
    """Python Skrit INIT"""
    def __init__(self, cyrillic = True, lng = "sr"):
        self.cyrillic = cyrillic
        self.lng = lng
        self._samoglasnici = [
            'a', 'e', 'i', 'o', 'u', 'r',
            'A', 'E', 'I', 'O', 'U', 'R',
            'а', 'е', 'и', 'о', 'у', 'р',
            'А', 'Е', 'И', 'О', 'У', 'Р'
        ]
        self._srb_ltrs_dvoslov = [
            ['l', 'j'], ['n', 'j'], ['s', 'h'],
            ['d', 'j'], ['d', 'z'], ['c', 'h']
        ]
        self._srb_cyr_ltrs_dvoslov = [
            ['љ'], ['њ'], ['ш'],
            ['ђ'], ['џ'], ['č']
        ]
        self._serbian_letters_dvoslov_fix = [
            'lj', 'nj', 'sh',
            'dj', 'dz', 'dž',
        ]
        self._dvoslov_dict = {}
        for ltn, cyr in zip(self._srb_ltrs_dvoslov, self._srb_cyr_ltrs_dvoslov):
            self._dvoslov_dict[''.join(ltn)] = ''.join(cyr)
        self._dvoslov_dict['dz'] = 'џ'
        self._dvoslov_dict['dž'] = 'џ'

    def __call__(self, input_string, cyrillic, lng):
        return self.satrovacki(input_string, cyrillic, lng)

    def is_odd(self, input_string):
        """Python Skrit check if letter is odd"""
        return input_string % 2

    def convert_dvoslov(self, input_text):
        """Python Skrit convert dvoslov"""
        output_text = input_text
        for dvoslov, cyrillic in self._dvoslov_dict.items():
            output_text = output_text.replace(dvoslov, cyrillic)
        return output_text

    def is_smglsnk_lst(self, input_string):
        """Python Skrit samoglasnik check"""
        if input_string[-1] in self._samoglasnici:
            return True
        return False

    # satrovacki method
    def satrovacki(self, input_string, cyrillic=True, lng="sr"):
        """Python Skrit satrovacki"""
        input_string = self.convert_dvoslov(input_string)
        input_string = cyrtranslit.to_cyrillic(input_string, lng)
        lista = list(input_string)
        cnt_list = len(lista)
        hlf_list = round(cnt_list/2)
        if self.is_smglsnk_lst(input_string[0:hlf_list]) is not True:
            hlf_list = round(cnt_list/2)-1
        output = input_string[hlf_list:cnt_list]
        output += input_string[0:hlf_list]
        if cyrillic is True:
            return output
        return cyrtranslit.to_latin(output, lng)

# hide = Skrit()
# print(hide.satrovacki("kurchina", True))
