from random import randint


def main():
    topic = choose_topic()
    while True:
        user_input = input('''Click ENTER to generate: 
Or type in anything to go back to topics menu.''')
        print('')
        if not user_input:
            print(generate(topic))
            print('')
        else:
            print('')
            topic = choose_topic()


def choose_topic():
    """Let user decide on what topic the text is to be generated.

    :return: a dictionary: containing sliced sentences.
    """
    janusz_korwin_mikke = {
        'beginning': ['Ja chcę powiedzieć jedną rzecz:', 'Trzeba powiedzieć jasno:',
                      'Jak powiedzial wybitny krakowianin, Stanisław Lem,',
                      'Proszę mnie dobrze zrozumieć,', 'Ja chciałem państwu przypomnieć, że',
                      'Niech państwo nie maja złudzeń:', 'Powiedzmy to wyraźnie:'],
        'section_1': ['przedstawiciele czerwonej chołoty', 'ci wszyscy (tfu!) geje',
                      'funkcjonariusze reżymowej telewizji', 'tak zwani ekolodzy',
                      'ci wszyscy (tfu!) demokraci', 'agenci bezpieki', 'feminazistki'],
        'section_2': ['zupełnie bezkarnie', 'całkowicie bezczelnie',
                      'o poglądach na lewo od komunizmu', 'celowo i świadomie', 'z premedytacją',
                      'od czasów Okrągłego Stołu', 'w ramach postępu'],
        'section_3': ['nawołują do podniesienia podatków', 'próbują wyrzucić kierowców z miast',
                      'próbują skłócic Polskę z Rosją', 'głoszą brednie o globalnym ociepleniu',
                      'zakazują posiadania broni', 'nie dopuszczaję prawicy do władzy',
                      'uczą dzieci homoseksualizmu'],
        'section_4': ['bo dzięki temu mogą kraść', 'bo dostają za to pieniądze',
                      'bo tak się uczy w państwowej szkole',
                      'bo bez tego (tfu!) demokracja nie może istnieć',
                      'bo głupich jest więcej niż mądrych', 'bo chcą stworzyc raj na ziemi',
                      'bo chcą niszczyć cywilizację białego człowieka'],
        'ending': ['przez kolejne kadencje', 'o czym sie nie mówi',
                   'i właśnie dlatego Europa umiera', 'ale przyjdą muzułmanie i zrobią porządek',
                   '- tak samo zreszta jak za Hitlera',
                   '- prosze zobaczyć co się dzieje na Zachodzie, jeśli mi państwo nie wierzą',
                   'co lat temu sto, nikomu nie przyszło by nawet do głowy']}

    power_metal_lyrics = {
        'begining': ['Galloping', 'Crying', 'Enlightening', 'Darkening', 'Fly', 'Rise', 'Reflect', 'Climb', 'Burn',
                     'Redeem', 'Power', 'Guide', 'Standing', 'Blazing', 'Reaching', 'Searching'],
        'section_2': ['triumphantly', 'quickly', 'eternally', 'brightly', 'vengefully', 'courageously', 'defiantly',
                      'gracefully', 'solemnly', 'viciously', 'sorrowfully', 'bravely', 'mysteriously', 'violently',
                      'frantically', 'wildly'],
        'section_3': ['through', 'into', 'above', 'beneath', 'beyond', 'amongst', 'below', 'under', 'in', 'against',
                      'within', 'inside', 'before', 'outside'],
        'section_4': ['snowy', 'shining', 'glowing', 'ancient', 'rising', 'crystal', 'fantastical', 'soulful',
                      'aggressive', 'courageous', 'defiant', 'bloody', 'cloudy', 'graceful', 'misty', 'icy'],
        'ending': ['moonlight', 'darkness', 'defenders', 'wings', 'light', 'fields', 'destiny', 'sun',
                   'heavens', 'souls', 'sunlight', 'battle cry', 'night', 'skies', 'dream', 'clouds', 'path',
                   'ice', 'mountains', 'plains', 'hearts', 'stars', 'fire', 'lands', 'abyss']}

    print('Choose a topic:')
    print('Type 1 for: Janusz Korwin Mikke [PL]')
    print('Type 2 for: Power Metal lyrics [EN]')
    choice = input()

    if choice == '1':
        return janusz_korwin_mikke
    elif choice == '2':
        return power_metal_lyrics
    else:
        print('You have failed to type a simple number...')
        main()


def generate(dictionary):
    """Generate a random sentence on the chosen topic.

    :param dictionary: containing parts of text to be joined together. Can be of any size.
    :return: a joined sentence from randomly chosen parts.
    """

    keys = dictionary.keys()
    parts_list = []
    for key in keys:
        part = dictionary[key][randint(0, len(dictionary[key]) - 1)]
        parts_list.append(part)
    sentence = ' '.join(parts_list) + '.'
    ready_sentence = f'"{sentence}"'
    return ready_sentence


if __name__ == '__main__':
    main()
