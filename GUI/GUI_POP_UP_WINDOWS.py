# Te biblioteki trzeba zostawić, bez nich nie działa, usunąłem zbędne, które można potem dodać
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import customtkinter
import algorithm.algorithm
import Google_Sheet.Google_Forms
import warnings
warnings.filterwarnings("ignore")

# Ustawienie koloru customowego
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Utworzenie list z wynikami końcowymi tworzącymi naszą osobowość, listę z pytaniami z naszego testu oraz z imieniem
results = []
que_test = []
names = []

# Otworzenie pliku z pytaniami i wrzucenie ich do listy za pomocą pętli
questions = open("./GUI/queue_num60.txt", "r", encoding="UTF-8")
for i in range(60):
    que_test.append(questions.readline())

# Utworzenie okna pierwszego o wielkości 170x145 wycentrowanego w środku ekranu z tytułem Test
root = customtkinter.CTk()
root.title("Test")

# root.eval('tk::PlaceWindow . center')

WIDTH = 1300
HEIGHT = 600

x = int((root.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((root.winfo_screenheight() / 2) - (HEIGHT / 2))

root.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')


# Stworzenie dwóch tabeli z nazwą oraz poleceniem,oraz okno do wpisania imienia.
name_test = customtkinter.CTkLabel(root, text="Test szesnastu osobowości",text_font=('Times New Roman', 30, 'bold'))
name_label = customtkinter.CTkLabel(root, text="Tutaj wpisz swoje imię:",text_font=('Times New Roman', 24, 'bold'))
name_entry = customtkinter.CTkEntry(root)
# Przypisane do dynamiki oraz ułożenie w ramce elementów
name_test.place(rely=0.3,relx=0.5,anchor= CENTER)
name_label.place(rely=0.4,relx=0.5,anchor= CENTER)
name_entry.place(rely=0.5,relx=0.5,anchor= CENTER)


# funkcja dodająca do pliku textowego imię po wpisaniu w pole
def add_name():
    name = name_entry.get()
    names.append(name)
    with open("./GUI/results.txt", "a") as f:
        f.write("\n")
        f.write(f"{name}")


# Funkcja wyświelająca wiadomość tekstową
def popup():
    messagebox.showinfo("Cześć!",
                        "Zapraszamy Cię do wykonania testu osobowości.\nOdpowiadaj szczerze, tylko takie odpowiedzi pozwolą określić Twój prawdziwy typ osobowości.\nTest składa się z 60 pytań.\nŻyczymy dobrej zabawy!")


# Przycisk w pierwszym oknie odpalający funkcję również przypisany do dynamiki. Odpala on też dalszy test.
button = customtkinter.CTkButton(root, text="Zapisz swoje imię",text_font=('Times New Roman', 13, 'bold'),
                                 command=lambda: [add_name(), popup(), test_window()])
button.place(rely=0.6,relx=0.5,anchor= CENTER)

# Zmienna z początkową wartości listy w celu wyświetlenia z dobrą kolejnością pytania z que_test
que_num = 0


# funkcja tworząca ostatnie okno z wynikiem
def graph():
    result = algorithm.algorithm.know_your_personality(results)
    values = Google_Sheet.Google_Forms.data_from_and_to_Google(result)
    personality = []
    resu_num_person = []
    personality_dual = str(values)
    personality_dual = personality_dual.split(",")
    for i in range(len(personality_dual)):
        personality_dual[i] = personality_dual[i].replace("'", " ")
        personality_dual[i] = personality_dual[i].replace("]", " ")
        personality_dual[i] = personality_dual[i].replace("[", " ")
        personality_dual[i] = personality_dual[i].rstrip()
        personality_dual[i] = personality_dual[i].lstrip()
        if i % 2 == 0:
            personality.append(personality_dual[i])
        else:
            personality_dual[i] = float(personality_dual[i])
            resu_num_person.append(personality_dual[i])


    fig, ax = plt.subplots(figsize=(20.,7.))
    plt.subplots_adjust(left=0.2, bottom=0.11, right=0.9, top=0.9, wspace=0.2, hspace=0.2)
    fig.canvas.set_window_title('Wykres')

    # Horizontal Bar Plot
    ax.barh(personality, resu_num_person, color = ['darkorchid','blueviolet','purple','mediumorchid',
                                                   'darkolivegreen','olivedrab','springgreen','palegreen',
                                                   'deepskyblue','skyblue','cyan','dodgerblue',
                                                   'yellow','darkgoldenrod','gold','khaki'],  align='edge')
    for bars in ax.containers:
        ax.bar_label(bars)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.6,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    # Add Plot Title
    ax.set_title('Wyniki wykonujących test w aplikacji',
                 loc='Center', )
    ax.set_xlabel("Liczba osób wykonujących test")
    ax.set_ylabel("Osobowość")
    ax.set_xticklabels(np.arange(0,101,10))

    plt.show()
  
    exit()

def result_window():
    result = customtkinter.CTk()
    result.title("Wynik")

    result.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    result_greetings = customtkinter.CTkLabel(result, text=f"\nWitaj {names[0]}\n Twoja osobowość to:",text_font=('Times New Roman', 20, 'bold')).pack()
    opisy = []
    opis = algorithm.algorithm.know_your_personality(results)
    opisy.append(opis)
    opisy = str(opisy)
    opisy = opisy.replace("|", " \n ")
    opisy = opisy.replace("]"," ")
    opisy = opisy.replace("["," ")
    opisy = opisy.replace(")", " ")
    opisy = opisy.replace("(", " ")
    opisy = opisy.replace("'", "")
    opisy = opisy.lstrip()
    opisy = opisy.rstrip()

    google_result = customtkinter.CTkLabel(result, text=f"\n{opisy}\n",text_font=('Times New Roman', 14)).pack()
    button = customtkinter.CTkButton(result, text="Pokaż wyniki \n innych osób",
                                     command=lambda: [graph()])
    button.pack()



    result.mainloop()

# Funkcja odpowiadająca za wyświetlanie okien z pytaniami
def test_window():
    # Utworzenie okna wraz z tytułem,centrowaniem,geometrią(wymiarem), oraz dynamiką
    root.wm_geometry('1x1+100000000+1000000000')
    gul = customtkinter.CTk()
    gul.title("Test")

    gul.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    Grid.rowconfigure(gul, 6, weight=1)
    Grid.rowconfigure(gul, 8, weight=1)
    Grid.columnconfigure(gul, 0, weight=1)
    Grid.columnconfigure(gul, 1, weight=1)
    Grid.columnconfigure(gul, 2, weight=1)
    Grid.columnconfigure(gul, 3, weight=1)
    Grid.columnconfigure(gul, 4, weight=1)
    Grid.columnconfigure(gul, 5, weight=1)
    Grid.columnconfigure(gul, 6, weight=1)

    # Funkcje odpowiadające za zamykanie, otwieranie kolejnego pytania z okna, oraz tworzenie listy z wynikami.

    def count():
        global que_num
        if que_num < 59:
            que_num += 1      
            test_window()
            gul.wm_geometry('1x1+100000000+1000000000')
        if que_num == 59:
            result_window()
            gul.wm_geometry('1x1+100000000+1000000000')

    def click1():
        results.append(-3)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click2():
        results.append(-2)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click3():
        results.append(-1)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click4():
        results.append(0)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click5():
        results.append(1)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click6():
        results.append(2)
        gul.wm_geometry('1x1+100000000+1000000000')

    def click7():
        results.append(3)
        gul.wm_geometry('1x1+100000000+1000000000')


    # Zmieniający się przycisk z zawartością(zmienia pytania przy pomocy zmiennej)
    question_label = customtkinter.CTkLabel(gul, text=(f"{que_test[que_num]}"),
                                            text_font=('Times New Roman', 26, 'bold'))
    question_label.place(relx=.5, rely=.4,anchor= CENTER)

    # Niezmienne pytania pojawiające się w tym samym miejscu powodują przy kliknięciu odpalenie funkcji odpowiedzialnych za wyniki
    answerno = customtkinter.CTkLabel(gul,text="Zdecydowanie \n nie zgadzam się",text_font=('Times New Roman', 12, 'bold'))
    answerno.place(x=20,y=300)
    answer1 = customtkinter.CTkButton(gul, text="1",height=50, width=50, command=lambda:[click7(),count()])
    answer1.place(x=200 ,y=300)
    answer2 = customtkinter.CTkButton(gul, text="2",height=50, width=50, command=lambda:[click6(),count()])
    answer2.place(x=350,y=300)
    answer3 = customtkinter.CTkButton(gul, text="3",height=50, width=50, command=lambda:[click5(),count()])
    answer3.place(x=500,y=300)
    answer4 = customtkinter.CTkButton(gul, text="4",height=50, width=50,command=lambda:[click4(),count()])
    answer4.place(x=650,y=300)
    answer5 = customtkinter.CTkButton(gul, text="5",height=50, width=50, command=lambda:[click3(),count()])
    answer5.place(x=800,y=300)
    answer6 = customtkinter.CTkButton(gul, text="6",height=50, width=50,  command=lambda:[click2(),count()])
    answer6.place(x=950,y=300)
    answer7 = customtkinter.CTkButton(gul, text="7",height=50, width=50, command=lambda:[click1(),count()])
    answer7.place(x=1100,y=300)
    answeryes = customtkinter.CTkLabel(gul, text="Zdecydowanie \n zgadzam się",text_font=('Times New Roman', 12, 'bold'))
    answeryes.place(x=1150, y=300)
    # utrzymywanie okna z pytaniami przy życiu
    gul.mainloop()


# Utrzymywanie okna początkowego przy życiu
root.mainloop()

# Żeby odpalić na customowym wygląda trzeba dodać nową bibliotekę o nazwie customtkinter
# Trzeba go pobrać z strony pod tym linkiem https://github.com/TomSchimansky/CustomTkinter
# odpalić cmd wiersza poleceń i dać tekst " python -m pip install customtinker"
# po zainstalowaniu zainstalować na platformie na jakiej robicie ( u mnie na pycharmie)
