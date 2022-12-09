from random import randint


def main():
    topic = choose_topic()
    while True:
        input('Click ENTER to generate')
        print(generate(topic))


def choose_topic():
    """Let user decide on what topic the text is to be generated

    :return: a dictionary: containing sliced sentences
    """
    janusz_korwin_mikke = {'beginning': ['Ja chcę powiedzieć jedną rzecz: ', 'Trzeba powiedzieć jasno: ',
                                         'Jak powiedzial wybitny krakowianin, Stanisław Lem, ',
                                         'Proszę mnie dobrze zrozumieć, ', 'Ja chciałem państwu przypomnieć, że ',
                                         'Niech państwo nie maja złudzeń: ', 'Powiedzmy to wyraźnie: '],
                           'section_1': ['przedstawiciele czerwonej chołoty ', 'ci wszyscy (tfu!) geje ',
                                         'funkcjonariusze reżymowej telewizji ', 'tak zwani ekolodzy ',
                                         'ci wszyscy (tfu!) demokraci ', 'agenci bezpieki ', 'feminazistki '],
                           'section_2': ['zupełnie bezkarnie ', 'całkowicie bezczelnie ',
                                         'o poglądach na lewo od komunizmu ', 'celowo i świadomie ', 'z premedytacją ',
                                         'od czasów Okrągłego Stołu ', 'w ramach postępu '],
                           'section_3': ['nawołują do podniesienia podatków ', 'próbują wyrzucić kierowców z miast ',
                                         'próbują skłócic Polskę z Rosją ', 'głoszą brednie o globalnym ociepleniu ',
                                         'zakazują posiadania broni ', 'nie dopuszczaję prawicy do władzy ',
                                         'uczą dzieci homoseksualizmu '],
                           'section_4': ['bo dzięki temu mogą kraść ', 'bo dostają za to pieniądze ',
                                         'bo tak się uczy w państwowej szkole ',
                                         'bo bez tego (tfu!) demokracja nie może istnieć ',
                                         'bo głupich jest więcej niż mądrych ', 'bo chcą stworzyc raj na ziemi',
                                         'bo chcą niszczyć cywilizację białego człowieka '],
                           'ending': ['przez kolejne kadencje.', 'o czym sie nie mówi.',
                                      'i właśnie dlatego Europa umiera.', 'ale przyjdą muzułmanie i zrobią porządek.',
                                      '- tak samo zreszta jak za Hitlera.',
                                      '- prosze zobaczyć co się dzieje na Zachodzie, jeśli mi państwo nie wierzą.',
                                      'co lat temu sto, nikomu nie przyszło by nawet do głowy.']}

    return janusz_korwin_mikke

def generate(dictionary):
    """Generate a random sentence on the chosen topic

    :param dictionary: containing parts of text to be joined together. Can be of any size.
    :return: a joined sentence from randomly chosen parts
    """

    keys = dictionary.keys()
    parts_list = []
    for key in keys:
        part = dictionary[key][randint(0, len(dictionary[key]) - 1)]
        parts_list.append(part)
    return ''.join(parts_list)

if __name__ == '__main__':
    main()
