import string
import locale

from alphanum_exception import AlphanumValidationError
class AlphaNum():
    def __init__(self, locale_code = ''):
        self.locale_code = locale_code
        if self.locale_code == '':
            self.locale_code = 'en-us'
        print('I am some constructor behavior and the language I am supporting is: ' + self.locale_code)

    def get_french_chars(self):
        ## read up on unicode, https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin
        chrs = ['\u00E7','\u00E8','\u00E9','\u00EA','\u00EE','\u00EF','\u00F4','\u0153','\u00FA','\u00FB','\u00FC']
        return chrs

    def get_char(self, position):
        char = None
        try:
            char = list(self.get_alphabet(self.locale_code))[position]
            return char
        except Exception as ex:
            if(type(ex).__name__ == 'IndexError'):
                raise AlphanumValidationError({"message": "You passed a number which is outside of the range of the alphabet positions",
                                               "acceptable_range": "0-25",
                                               "value_passed": position})
            raise ex
    def get_position(self, character):
        return self.get_alphabet(self.locale_code).index(character.lower())

    def get_locale(self):
        return self.locale_code

    def get_french_alphabet(self):
        fr_alphabet = list(string.ascii_lowercase)
        fr_alphabet[1:1] = ['\u00E0','\u00E1','\u00E4']
        fr_alphabet[6:6]= ['\u00E7']
        fr_alphabet[9:9] = ['\u00E8','\u00E9','\u00EA']
        fr_alphabet[15:15] = ['\u00EE', '\u00EF']
        fr_alphabet[24:24] = ['\u00F4', '\u0153']
        fr_alphabet[32:32] = ['\u00F9', '\u00FC']
        fr_alphabet[38:38] = ['\u00FF']
        return fr_alphabet

    def get_german_alphabet(self):
        raise Exception('German alphabet not implemented')

    def get_alphabet(self, locale):
        if locale == 'en-us' : return string.ascii_lowercase
        if locale == 'fr-fr': return self.get_french_alphabet()
        raise Exception('Unknown locale, unsupported')


