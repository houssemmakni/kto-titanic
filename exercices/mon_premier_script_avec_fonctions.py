#"""
#Count names with more than seven letters
#"""
#def names(prenoms):
#    more_than_seven = 0
#    for prenom in prenoms:
#        if len(prenom) > 7:
#            more_than_seven += 1
#            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
#        else:
#            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
#    return more_than_seven
#
#prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
#print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))






import unittest

MAX_SHORT_NAME_LENGTH = 7


def names(prenoms: list[str]) -> int:
    """
    Count names with more than seven letters
    """
    long_names_count = 0

    for prenom in prenoms:
        if has_more_letters_than_limit(prenom):
            long_names_count += 1
            print(f"{prenom} est un prénom avec plus de {MAX_SHORT_NAME_LENGTH} lettres")
        else:
            print(f"{prenom} est un prénom avec {MAX_SHORT_NAME_LENGTH} lettres ou moins")

    return long_names_count


def has_more_letters_than_limit(prenom: str) -> bool:
    return len(prenom) > MAX_SHORT_NAME_LENGTH



class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()