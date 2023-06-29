import algorithm.counter.count


class Personality:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters

    def introduce(self):
        return self.name

    def if_this(self, result_code):
        if result_code == self.parameters:
            return True
        else:
            return False

personalities = [[] for i in range(16)]
personalities[0].append(Personality("Architekt - INTJ-A", "", [1, 0, 0, 0, 0]))
personalities[0].append(Personality("Architekt - INTJ-T", "", [1, 0, 0, 0, 1]))
personalities[1].append(Personality("Logik - INTP-A", "", [1, 0, 0, 1, 0]))
personalities[1].append(Personality("Logik - INTP-T", "", [1, 0, 0, 1, 1]))
personalities[2].append(Personality("Dowódca - ENTJ-A", "", [0, 0, 0, 0, 0]))
personalities[2].append(Personality("Dowódca - ENTJ-T", "", [0, 0, 0, 0, 1]))
personalities[3].append(Personality("Dyskutant - ENTP-A", "", [0, 0, 0, 1, 0]))
personalities[3].append(Personality("Dyskutant - ENTP-T", "", [0, 0, 0, 1, 1]))
personalities[4].append(Personality("Rzecznik - INFJ-A", "", [1, 0, 1, 0, 0]))
personalities[4].append(Personality("Rzecznik - INFJ-T", "", [1, 0, 1, 0, 1]))
personalities[5].append(Personality("Pośrednik - INFP-A", "", [1, 0, 1, 1, 0]))
personalities[5].append(Personality("Pośrednik - INFP-T", "", [1, 0, 1, 1, 1]))
personalities[6].append(Personality("Protagonista - ENFJ-A", "", [0, 0, 1, 0, 0]))
personalities[6].append(Personality("Protagonista - ENFJ-T", "", [0, 0, 1, 0, 1]))
personalities[7].append(Personality("Działacz - ENFP-A", "", [0, 0, 1, 1, 0]))
personalities[7].append(Personality("Działacz - ENFP-T", "", [0, 0, 1, 1, 1]))
personalities[8].append(Personality("Logistyk - ISTJ-A", "", [1, 1, 0, 0, 0]))
personalities[8].append(Personality("Logistyk - ISTJ-T", "", [1, 1, 0, 0, 1]))
personalities[9].append(Personality("Obrońca - ISFJ-A", "", [1, 1, 1, 0, 0]))
personalities[9].append(Personality("Obrońca - ISFJ-T", "", [1, 1, 1, 0, 1]))
personalities[10].append(Personality("Wykonawca - ESTJ-A", "", [0, 1, 0, 0, 0]))
personalities[10].append(Personality("Wykonawca - ESTJ-T", "", [0, 1, 0, 0, 1]))
personalities[11].append(Personality("Doradca - ESFJ-A", "", [0, 1, 1, 0, 0]))
personalities[11].append(Personality("Doradca - ESFJ-T", "", [0, 1, 1, 0, 1]))
personalities[12].append(Personality("Wirtuoz - ISTP-A", "", [1, 1, 0, 1, 0]))
personalities[12].append(Personality("Wirtuoz - ISTP-T", "", [1, 1, 0, 1, 1]))
personalities[13].append(Personality("Poszukiwacz Przygód - ISFP-A", "", [1, 1, 1, 1, 0]))
personalities[13].append(Personality("Poszukiwacz Przygód - ISFP-T", "", [1, 1, 1, 1, 1]))
personalities[14].append(Personality("Przedsiębiorca - ESTP-A", "", [0, 1, 0, 1, 0]))
personalities[14].append(Personality("Przedsiębiorca - ESTP-T", "", [0, 1, 0, 1, 1]))
personalities[15].append(Personality("Animator - ESFP-A", "", [0, 1, 1, 1, 0]))
personalities[15].append(Personality("Animator - ESFP-T", "", [0, 1, 1, 1, 1]))

for i in range(16):
    path = "./algorithm/" + str(i)
    file = open(path, "r")
    opis = file.read()
    personalities[i][0].description = opis
    personalities[i][1].description = opis

def know_your_personality(response, personalities = personalities):
    results = algorithm.counter.count.count_result(response)
    result_code = [-1 for i in range(len(results))]
    for i in range(len(results)):
        if results[i] <= 50:
            result_code[i] = 1
        else:
            result_code[i] = 0
    for i in range(len(personalities)):
        if(personalities[i][0].if_this(result_code)):
            return personalities[i][0].name, personalities[i][0].description
        if(personalities[i][1].if_this(result_code)):
            return personalities[i][1].name, personalities[i][1].description
    return "Błąd wyświetlania osobowości"

