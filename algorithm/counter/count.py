

# metoda do przetwarzania stringa na liste
def make_an_int_list(text):
    j = 0
    result_list = ["" for i in range(7)]
    for i in range(len(text)):
        if text[i] != " ":
            result_list[j] += text[i]
        else:
            j += 1
    for i in range(len(result_list)):
        result_list[i] = int(result_list[i])
    return result_list


# metoda do obliczania wyniku
def count_result(response):
    points_file = open("./algorithm/counter/points.txt", "r")
    tmp_plus_points = points_file.readline().rstrip()  # string z punktami zaczynajacymi sie od plusa
    tmp_minus_points = points_file.readline().rstrip()  # string z punktami zaczynajacymi sie od minusa

    plus_points = make_an_int_list(tmp_plus_points)  # lista z punktami zaczynajacymi sie od plusa
    minus_points = make_an_int_list(tmp_minus_points)  # lista z punktami zaczynajacymi sie od minusa
    points_file.close()

    queue_file = open("./algorithm/counter/queue.txt", "r")
    tmp_queue = queue_file.readline().rstrip()  # string z kolejnoscia punktow
    queue = list(tmp_queue)  # lista z kolejnoscia punktow
    queue_file.close()

    queue_of_section_file = open("./algorithm/counter/queue_of_section.txt", "r")
    tmp_queue_of_section = queue_of_section_file.readline().rstrip()  # string z kolejnoscia wystepowania pytan
    section = list(tmp_queue_of_section)  # lista z kolejnoscia wystepowania pytan
    queue_of_section_file.close()

    mind = 49
    energy = 49
    nature = 49
    tactics = 49
    identification = 49

    for i in range(60):
        if queue[i] == 'm':
            points = minus_points.copy()
        elif queue[i]=='p':
            points = plus_points.copy()
        else:
            print("Zly plik z kolejka")
        # dla opcji absolutnie sie zgadzam
        if response[i] == -3 and section[i] == "m":
            mind += points[0]
        if response[i] == -3 and section[i] == "e":
            energy += points[0]
        if response[i] == -3 and section[i] == "n":
            nature += points[0]
        if response[i] == -3 and section[i] == "t":
            tactics += points[0]
        if response[i] == -3 and section[i]=="i":
            identification += points[0]
        # dla opcji srednio sie zgadzam
        if response[i] == -2 and section[i] == "m":
            mind += points[1]
        if response[i] == -2 and section[i] == "e":
            energy += points[1]
        if response[i] == -2 and section[i] == "n":
            nature += points[1]
        if response[i] == -2 and section[i] == "t":
            tactics += points[1]
        if response[i] == -2 and section[i] == "i":
            identification += points[1]
        # dla opcji troche sie zgadzam
        if response[i] == -1 and section[i] == "m":
            mind += points[2]
        if response[i] == -1 and section[i] == "e":
            energy += points[2]
        if response[i] == -1 and section[i] == "n":
            nature += points[2]
        if response[i] == -1 and section[i] == "t":
            tactics += points[2]
        if response[i] == -1 and section[i] == "i":
            identification += points[2]
        # dla opcji nie mam zdania
        if response[i] == 0 and section[i] == "m":
            mind += points[3]
        if response[i] == -0 and section[i] == "e":
            energy += points[3]
        if response[i] == 0 and section[i] == "n":
            nature += points[3]
        if response[i] == 0 and section[i] == "t":
            tactics += points[3]
        if response[i] == 0 and section[i] == "i":
            identification += points[3]
        # dla opcji troche sie nie zgadzam
        if response[i] == 1 and section[i] == "m":
            mind += points[4]
        if response[i] == 1 and section[i] == "e":
            energy += points[4]
        if response[i] == 1 and section[i] == "n":
            nature += points[4]
        if response[i] == 1 and section[i] == "t":
            tactics += points[4]
        if response[i] == 1 and section[i] == "i":
            identification += points[4]
        # dla opcji srednio sie nie zgadzam
        if response[i] == 2 and section[i] == "m":
            mind += points[5]
        if response[i] == 2 and section[i] == "e":
            energy += points[5]
        if response[i] == 2 and section[i] == "n":
            nature += points[5]
        if response[i] == 2 and section[i] == "t":
            tactics += points[5]
        if response[i] == 2 and section[i] == "i":
            identification += points[5]
        # dla opcji absolutnie sie zgadzam
        if response[i] == 3 and section[i] == "m":
            mind += points[6]
        if response[i] == 3 and section[i] == "e":
            energy += points[6]
        if response[i] == 3 and section[i] == "n":
            nature += points[6]
        if response[i] == 3 and section[i] == "t":
            tactics += points[6]
        if response[i] == 3 and section[i] == "i":
            identification += points[6]

    return mind, energy, nature, tactics, identification


