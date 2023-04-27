########################################################
#---------------- github.com/duruburak ----------------#
########################################################

import time
from random import choice
from threading import Thread

import customtkinter
# import numpy as np



customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.minsize(700, 450)
        self.maxsize(700, 450)
        self.title("Typing Speed Test")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.is_ongoing : bool = False

        self.quit : bool = False

        self.is_reset : bool = False

        self.is_time_up : bool = False
        self.timer : int = 60
        self.timer_formatted : str = '01:00'

        self.words : list = ["ring", "stamp", "claim", "perfect", "funny", "snails", "probable", 
                             "best", "vengeful", "crime", "yielding", "flowery", "grubby", 
                             "peaceful", "pie", "film", "elated", "punch", "sweet", "lewd", 
                             "unequal", "rabbit", "open", "internal", "property", "hurry", 
                             "useless", "divide", "nutritious", "fish", "hop", "understood", 
                             "wise", "toothpaste", "romantic", "decorate", "uneven", "possible", 
                             "plant", "famous", "island", "boast", "wonderful", "bikes", "shaggy", 
                             "lucky", "program", "thought", "mixed", "efficacious", "far-flung", 
                             "skinny", "hydrant", "spicy", "itch", "changeable", "hunt", "rely", 
                             "juicy", "lumpy", "late", "diligent", "develop", "escape", "coast", 
                             "rate", "wary", "green", "deer", "energetic", "placid", "zoo", "condition", 
                             "stormy", "grease", "naive", "old", "jagged", "voice", "giraffe", "invasion",
                             "rung", "census", "hurl", "far", "question", "hard", "moon", "defend", "dentist",
                             "haunt", "toll", "aunt", "light", "translate", "satisfied", "hut" ,"rank", "conflict",
                             "reporter", "diamond", "treasurer", "soup", "breed", "privilege", "unique", "bring",
                             "climb", "wisecrack", "notebook", "trench", "verdict", "an", "senior", "battlefield",
                             "computer", "root", "accompany", "registration", "elapse", "respect", "absorb", "reach", 
                             "gown", "projection", "unfair", "just", "laboratory", "supply"]
        
        self.kelimeler : list = ['öğrenci', 'sınav', 'kalem', 'masa', 'kitap', 'yazılım', 'programlama', 'bilgisayar', 
                                 'ders', 'not', 'okul', 'üniversite', 'öğretmen', 'müzik', 'dizi', 'film', 'sinema', 
                                 'tiyatro', 'saat', 'tarih', 'takvim', 'kahve', 'çay', 'su', 'meyve', 'sebze', 'et', 
                                 'tavuk', 'balık', 'eşya', 'mobilya', 'ev', 'yatak', 'yorgan', 'perde', 'ayna', 'tuvalet', 
                                 'banyo', 'havlu', 'şampuan', 'sabun', 'parfüm', 'koku', 'renk', 'sarı', 'kırmızı', 
                                 'mavi', 'yeşil', 'mor', 'turuncu', 'pembe', 'siyah', 'beyaz', 'kahverengi', 'grisi', 
                                 'altın', 'gümüş', 'para', 'banka', 'kredi', 'faiz', 'borç', 'gider', 'gelir', 'maaş', 
                                 'iş', 'fabrika', 'üretim', 'hizmet', 'satış', 'müşteri', 'pazarlama', 'reklam', 'medya', 
                                 'haber', 'gazete', 'dergi', 'internet', 'sosyal', 'telefon', 'bilgi', 'veri', 'dosya', 
                                 'belge', 'rapor', 'metin', 'imza', 'sözleşme', 'hukuk', 'avukat', 'dava', 'yargı', 
                                 'hükümet', 'devlet', 'bakan', 'cumhurbaşkanı', 'parlamento', 'yasa', 'kanun', 'toplum', 
                                 'insan', 'sağlık', 'hastane', 'doktor', 'hemşire', 'ilaç', 'eczane', 'spor', 'futbol', 
                                 'basketbol', 'voleybol', 'yüzme', 'koşu', 'araba', 'tatil', 'seyahat', 'otel', 
                                 'restoran', 'yemek', 'tatlı', 'dondurma', 'çikolata', 'kek', 'pasta', 'çerez', 'fındık', 
                                 'fıstık', 'çekirdek', 'yumurta', 'süt', 'peynir', 'abajur', 'abartı', 'acele', 'anarşi', 
                                 'bağlama', 'hasır', 'konuksever', 'meydan', 'ödeme', 'öğle', 'palamut', 'tartı', 'trafik']


        self.random_words : list = []
        self.current_word : str = ""

        self.current_word_index_minus_1_in_textbox : float = 0.0
        self.current_word_index_in_textbox : int = 0
        self.current_words_letter_index : int = 0
        self.current_letter_index_in_textbox : float = 0.0
        self.current_letter_index_in_textbox_int : int = int(self.current_letter_index_in_textbox)
        self.previous_letter_index_in_textbox_textbox_formatted : float = 1.0
        self.current_letter_index_in_textbox_textbox_formatted : float = 1.0
        self.next_letter_index_in_textbox_textbox_formatted : float = 1.1
        self.colors_by_index : dict = {}

        self.correct_characters_count : int = 0
        self.correct_words_count : int = 0
        self.mistyped_words_count : int = 0
        self.total_characters_count : int = 0

        self.current_language = "English"
        self.var_language_choice : customtkinter.StringVar = customtkinter.StringVar(value="English")
        self.var_is_reset : customtkinter.BooleanVar = customtkinter.BooleanVar(value=False)
        self.var_is_quit : customtkinter.BooleanVar = customtkinter.BooleanVar(value=False)
        self.entry_variable : customtkinter.StringVar = customtkinter.StringVar(value="")

        self.container_frame = customtkinter.CTkFrame(self)
        self.container_frame.grid(padx=15, pady=(15,2), sticky="nsew")
        self.container_frame.grid_rowconfigure((0,1,2,3), weight=1)
        self.container_frame.grid_columnconfigure(0, weight=1)

        self.words_textbox = customtkinter.CTkTextbox(master=self.container_frame, text_color="white", font=("Bahnschrift", 21, "normal"), wrap="word", activate_scrollbars=False)
        self.words_textbox.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.place_words()

        self.entry_timer_and_buttons_container = customtkinter.CTkFrame(self.container_frame)
        self.entry_timer_and_buttons_container.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.entry_timer_and_buttons_container.grid_rowconfigure(0, weight=1)
        self.entry_timer_and_buttons_container.grid_columnconfigure(0, weight=1)

        self.entry = customtkinter.CTkEntry(master=self.entry_timer_and_buttons_container, textvariable=self.entry_variable, text_color="white", font=("Arial Rounded MT", 18, "bold"), placeholder_text="Type to start/keep on")
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.kick_off = self.entry_variable.trace_add('write', self.is_kick_off)
        self.reset_entry = self.entry_variable.trace_add('write', self.spacebar_pressed)
        self.entry.bind('<Key>', self.check_typed_letter)

        self.label_timer = customtkinter.CTkLabel(master=self.entry_timer_and_buttons_container, height=30, width=50, corner_radius=15, text="01:00", text_color="#ECF2FF", font=("Roboto Mono Regular", 17, "normal"), fg_color="#2B2B2B")
        self.label_timer.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.chosen_language = customtkinter.CTkSwitch(master=self.entry_timer_and_buttons_container, fg_color="#3A4750", progress_color="#303841", text="English", text_color="#DDFFBB", font=("Harrington", 17, "bold"), button_color="#94B3FD", button_hover_color="#9795CF", border_color="#B2A4FF", variable=self.var_language_choice, onvalue="English", offvalue="Türkçe", command=self.switch_language)
        self.chosen_language.grid(row=0, column=2, padx=(5,6), pady=5, sticky="ew")

        self.reset_button = customtkinter.CTkButton(master=self.entry_timer_and_buttons_container, height=15, width=15, corner_radius=15, text="RESET", hover_color="#E21818", fg_color="#DC4C64", command=self.reset)
        self.reset_button.grid(row=0, column=3, padx=(6,5), pady=5, sticky="nsew")

        self.results_container = customtkinter.CTkFrame(self.container_frame, corner_radius=15)
        self.results_container.grid(row=3, column=0, padx=12, pady=(10,0), ipady=5, sticky="new")
        self.results_container.grid_rowconfigure((0,1), weight=1)
        self.results_container.grid_columnconfigure((0,1,2,3), weight=1)

        self.label_results_cps = customtkinter.CTkLabel(self.results_container, text="CPS", text_color="#B2A4FF", font=("Century Gothic", 16, "bold"))
        self.label_results_cps.grid(row=0, column=0, sticky="nsew")

        self.label_results_correct_words = customtkinter.CTkLabel(self.results_container, text="Correct Words", text_color="#B2A4FF", font=("Century Gothic", 16, "bold"))
        self.label_results_correct_words.grid(row=0, column=1, sticky="nsew")

        self.label_results_correct_letters = customtkinter.CTkLabel(self.results_container, text="Correct Letters", text_color="#B2A4FF", font=("Century Gothic", 16, "bold"))
        self.label_results_correct_letters.grid(row=0, column=2, sticky="nsew")

        self.label_results_false_words = customtkinter.CTkLabel(self.results_container, text="Mistyped Words", text_color="#B2A4FF", font=("Century Gothic", 16, "bold"))
        self.label_results_false_words.grid(row=0, column=3, sticky="nsew")

        self.value_results_cps = customtkinter.CTkLabel(self.results_container, text="-", text_color="#5BC0DE", font=("Rajdhani Medium", 17, "bold"))
        self.value_results_cps.grid(row=1, column=0, sticky="nsew")

        self.value_results_correct_words = customtkinter.CTkLabel(self.results_container, text="-", text_color="#14A44D", font=("Rajdhani Medium", 17, "bold"))
        self.value_results_correct_words.grid(row=1, column=1, sticky="nsew")

        self.frame_results_correct_letters = customtkinter.CTkFrame(self.results_container, fg_color="gray20", bg_color="gray20")
        self.frame_results_correct_letters.grid(row=1, column=2, sticky="ns")
        self.frame_results_correct_letters.grid_columnconfigure((0,1,2), weight=1)

        self.value_results_correct_letters = customtkinter.CTkLabel(self.frame_results_correct_letters, text="-", text_color="#14A44D", font=("Rajdhani Medium", 17, "bold"))
        self.value_results_correct_letters.grid(row=0, column=0, padx=2, sticky="nse")

        self.value_results_hyphen = customtkinter.CTkLabel(self.frame_results_correct_letters, text="/", text_color="#B2A4FF", font=("Rajdhani Medium", 21, "bold"))
        self.value_results_hyphen.grid(row=0, column=1, padx=2, sticky="ns")

        self.value_results_total_letters = customtkinter.CTkLabel(self.frame_results_correct_letters, text="-", text_color="#E5BEEC", font=("Rajdhani Medium", 17, "bold"))
        self.value_results_total_letters.grid(row=0, column=2, padx=2, sticky="nsw")

        self.value_results_false_words = customtkinter.CTkLabel(self.results_container, text="-", text_color="#E21818", font=("Rajdhani Medium", 17, "bold"))
        self.value_results_false_words.grid(row=1, column=3, sticky="nsew")

        self.signature = customtkinter.CTkButton(self, width=1, height=1, text="by duruburak", text_color="#B2B2B2", font=("Blackadder ITC", 18, "normal"), hover=False, fg_color="transparent", bg_color="transparent", command=self.go_to_my_github)
        self.signature.grid(row=1, column=0, padx=10, pady=(1,3), ipady=1, sticky="nse")

    def switch_language(self):

        self.current_language = self.var_language_choice.get()

        if self.current_language == "Türkçe":
            self.chosen_language.configure(text="Türkçe")
            self.reset_button.configure(text="SIFIRLA")
            self.label_results_correct_words.configure(text="Doğru Kelime")
            self.label_results_correct_letters.configure(text="Doğru Harf")
            self.label_results_false_words.configure(text="Yanlış Kelime")
            self.place_words()
            self.title("Yazma Hızı Testi")

        else:
            self.chosen_language.configure(text="English")
            self.reset_button.configure(text="RESET")
            self.label_results_correct_words.configure(text="Correct Words")
            self.label_results_correct_letters.configure(text="Correct Letters")
            self.label_results_false_words.configure(text="Mistyped Words")
            self.place_words()
            self.title("Typing Speed Test")

        self.update_idletasks()

    def place_words(self):

        self.random_words.clear()
        self.words_textbox.configure(state="normal")
        self.words_textbox.delete(1.0, "end")

        index : float = 1.0

        if self.current_language == "English":
            for _ in range(100):
                word = choice(self.words)
                self.words_textbox.insert(index, word + " ")
                self.random_words.append(word)
                index += len(word) + 1

        else:
            for _ in range(100):
                word = choice(self.kelimeler)
                self.words_textbox.insert(index, word + " ")
                self.random_words.append(word)
                index += len(word) + 1

        self.words_textbox.configure(state="disabled")

    def start_game(self):

        self.chosen_language.configure(state="disabled")
        self.is_ongoing = True

        while self.timer:

            if self.quit:
                self.var_is_quit.set(True)
                return

            if self.is_reset:
                break

            if self.timer == 10:
                self.label_timer.configure(text_color="#FF0000")

            mins, secs = divmod(self.timer, 60)
            self.timer_formatted = '{:02d}:{:02d}'.format(mins, secs)
            self.label_timer.configure(text=self.timer_formatted)

            time.sleep(1)

            self.timer -= 1
        # If entry is disabled without focusing another widget, the user will still be typing words
        self.words_textbox.focus()
        self.entry.configure(state="disabled")
        self.bell()

        self.is_ongoing = False
        self.is_time_up = True

        if self.is_reset != True:
            self.label_timer.configure(text="00:00")
            self.get_results()

        self.var_is_reset.set(True)
        self.chosen_language.configure(state="normal")

    # Cue for the test to begin
    def is_kick_off(self, *args):

        Thread(target=self.start_game).start()
        self.entry_variable.trace_vdelete('w', self.kick_off)

    def spacebar_pressed(self, *args):

        try:
            if self.entry_variable.get()[-1] == " ":

                self.current_word = self.random_words[self.current_word_index_in_textbox]
                word = self.entry_variable.get().lower()

                self.check_typed_word(word)

                self.total_characters_count += len(self.current_word)
                self.current_word_index_minus_1_in_textbox += len(self.random_words[self.current_word_index_in_textbox]) + 1
                self.current_words_letter_index = 0
                self.current_word_index_in_textbox += 1

                # Get the current vertical position of the scrollbar
                _, y = self.words_textbox.yview()

                # Get the height of the Text widget in pixels
                height = self.words_textbox.winfo_height()

                # Get the index of the word at the bottom of the visible area
                index = self.words_textbox.index(f"@0,{int(y * height)} wordend")

                # If the words yet to be typed are not visible, go scroll down
                if self.current_letter_index_in_textbox_int >= int(index.split('.')[1]):
                    self.words_textbox.see('100.0+0c')

                self.entry.delete(0, "end")
                # Prevent spamming spacebar (causes miscalculation)
                time.sleep(0.1)

        except:
            pass

    # Whether the typed word is correct
    def check_typed_word(self, word):

        if word[:len(self.current_word)] == self.current_word:
            self.correct_characters_count += len(self.current_word)
            self.correct_words_count += 1

        else:
            self.check_correct_letters_and_mark_false_letters_red_on_space(word)
            self.mistyped_words_count += 1

    def check_typed_letter(self, key):

        keysym = key.keysym
        key_char = key.char

        # If key stroke is not White Space, Tab, Enter, CTRL + Backspace and is something alphabetical or is Turkish letter and is not CTRL + Backspace
        if (keysym != "space" and keysym != "Tab" and keysym != "Return" and keysym.isalpha() and key_char != "\x7f") or (keysym == "??" and key_char != "\x7f"):

            letter = key_char.lower()

            self.current_letter_index_in_textbox = self.current_word_index_minus_1_in_textbox + self.current_words_letter_index
            self.current_letter_index_in_textbox_int = int(self.current_letter_index_in_textbox)

            if self.current_letter_index_in_textbox_int > 0:
                self.previous_letter_index_in_textbox_textbox_formatted = float(f"1.{self.current_letter_index_in_textbox_int - 1}")
            else:
                self.previous_letter_index_in_textbox_textbox_formatted = 1.0
            self.current_letter_index_in_textbox_textbox_formatted = float(f"1.{self.current_letter_index_in_textbox_int}")
            self.next_letter_index_in_textbox_textbox_formatted =  float(f"1.{self.current_letter_index_in_textbox_int + 1}")

            previous_index_digit = len(str(self.current_letter_index_in_textbox_int - 1))
            current_index_digit = len(str(self.current_letter_index_in_textbox_int))
            next_index_digit = len(str(self.current_letter_index_in_textbox_int + 1))

            if current_index_digit < next_index_digit:

                if next_index_digit == 3:
                    self.previous_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int - 1}"), ".2f")
                    self.current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int}"), ".2f")
                    self.next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int + 1}"), ".3f")
                else:
                    self.next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int + 1}"), ".2f")

            elif current_index_digit > 1:

                if current_index_digit == 3:
                    self.previous_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int - 1}"), ".3f")
                    self.current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int}"), ".3f")
                    self.next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int + 1}"), ".3f")
                    if previous_index_digit == 2:
                        self.previous_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int - 1}"), ".2f")
                else:
                    if previous_index_digit != 1:
                        self.previous_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int - 1}"), ".2f")
                    self.current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int}"), ".2f")
                    self.next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{self.current_letter_index_in_textbox_int + 1}"), ".2f")

            current_typed_word_length = len(self.entry_variable.get())
            current_correct_word_length = len(self.random_words[self.current_word_index_in_textbox])

            if letter != "\b" and current_typed_word_length < current_correct_word_length:

                if letter == self.words_textbox.get(self.current_letter_index_in_textbox_textbox_formatted, self.next_letter_index_in_textbox_textbox_formatted):
                    self.words_textbox.tag_add("correct", self.current_letter_index_in_textbox_textbox_formatted, self.next_letter_index_in_textbox_textbox_formatted)
                    self.words_textbox.tag_config("correct", foreground="green")
                    self.colors_by_index[self.current_letter_index_in_textbox_int] = 1

                else:
                    self.words_textbox.tag_add("false", self.current_letter_index_in_textbox_textbox_formatted, self.next_letter_index_in_textbox_textbox_formatted)
                    self.words_textbox.tag_config("false", foreground="red")
                    self.colors_by_index[self.current_letter_index_in_textbox_int] = 0

                self.current_words_letter_index += 1

            elif letter == "\b" and current_typed_word_length <= current_correct_word_length:

                    if self.current_words_letter_index > 0:

                        if self.colors_by_index[self.current_letter_index_in_textbox_int - 1]:
                            self.words_textbox.tag_remove("correct", self.previous_letter_index_in_textbox_textbox_formatted, self.current_letter_index_in_textbox_textbox_formatted)
                        else:
                            self.words_textbox.tag_remove("false", self.previous_letter_index_in_textbox_textbox_formatted, self.current_letter_index_in_textbox_textbox_formatted)

                        self.current_words_letter_index -= 1

            self.words_textbox.update_idletasks()

    def check_correct_letters_and_mark_false_letters_red_on_space(self, word):

        current_letter_index_in_textbox_textbox_formatted_int = int(self.current_word_index_minus_1_in_textbox)
        next_letter_index_in_textbox_textbox_formatted_int = int(self.current_word_index_minus_1_in_textbox) + 1

        counter = 0
        for i, l in enumerate(self.random_words[self.current_word_index_in_textbox]):

            current_letter_index_in_textbox_textbox_formatted = float(f"1.{current_letter_index_in_textbox_textbox_formatted_int + i}")
            next_letter_index_in_textbox_textbox_formatted = float(f"1.{next_letter_index_in_textbox_textbox_formatted_int + i}")

            if len(str(next_letter_index_in_textbox_textbox_formatted_int + i)) == 2:
                if current_letter_index_in_textbox_textbox_formatted_int + i == 9:
                    next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{next_letter_index_in_textbox_textbox_formatted_int + i}"), ".2f")
                else:
                    current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{current_letter_index_in_textbox_textbox_formatted_int + i}"), ".2f")
                    next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{next_letter_index_in_textbox_textbox_formatted_int + i}"), ".2f")

            elif len(str(next_letter_index_in_textbox_textbox_formatted_int + i)) == 3:
                if current_letter_index_in_textbox_textbox_formatted_int + i == 99:
                    current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{current_letter_index_in_textbox_textbox_formatted_int + i}"), ".2f")
                    next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{next_letter_index_in_textbox_textbox_formatted_int + i}"), ".3f")
                else:
                    current_letter_index_in_textbox_textbox_formatted = format(float(f"1.{current_letter_index_in_textbox_textbox_formatted_int + i}"), ".3f")
                    next_letter_index_in_textbox_textbox_formatted = format(float(f"1.{next_letter_index_in_textbox_textbox_formatted_int + i}"), ".3f")

            try:
                if l == word[i]:
                    counter += 1
                    continue
                else:
                    self.words_textbox.tag_add("false", current_letter_index_in_textbox_textbox_formatted, next_letter_index_in_textbox_textbox_formatted)
                    self.words_textbox.tag_config("false", foreground="red")
                    self.colors_by_index[self.current_word_index_minus_1_in_textbox + i + 1] = 0
            except:
                self.words_textbox.tag_add("false", current_letter_index_in_textbox_textbox_formatted, next_letter_index_in_textbox_textbox_formatted)
                self.words_textbox.tag_config("false", foreground="red")
                self.colors_by_index[self.current_word_index_minus_1_in_textbox + i + 1] = 0
                pass

        self.correct_characters_count += counter
        self.words_textbox.update_idletasks()


    def get_results(self):

        self.current_word = self.random_words[self.current_word_index_in_textbox]
        word = self.entry_variable.get().lower()
        current_word_length = len(self.current_word)
        current_typed_word_length = len(word)

        if current_typed_word_length >= current_word_length:

            if word[:current_word_length] == self.current_word:
                self.correct_words_count += 1
                self.correct_characters_count += current_word_length
                self.total_characters_count += current_word_length

            else:
                self.mistyped_words_count += 1
                self.total_characters_count += current_typed_word_length

        else:

            if word != "" or word != "\r" and current_typed_word_length > 0:
                if word == self.current_word[:current_typed_word_length]:
                    self.correct_characters_count += current_typed_word_length
                    self.total_characters_count += current_typed_word_length

                else:
                    for i, l in enumerate(word):
                        if l == self.current_word[i]:
                            self.correct_characters_count += 1
                            self.total_characters_count += 1
                        else:
                            self.total_characters_count += 1

        # correct_and_false_values = list(self.colors_by_index.values())
        # unique_values, counts = np.unique(correct_and_false_values, return_counts=True)
        # correct_and_false_value_counts = dict(zip(unique_values, counts))

        correct_letters_count = self.correct_characters_count
        total_letters_count = self.total_characters_count
        mistyped_words_count = self.mistyped_words_count
        correct_words_count = self.correct_words_count
        character_per_second = round(correct_letters_count / 60, 2)

        self.value_results_cps.configure(text = str(character_per_second))
        self.value_results_correct_words.configure(text = str(correct_words_count))
        self.value_results_correct_letters.configure(text = str(correct_letters_count))
        self.value_results_total_letters.configure(text = str(total_letters_count))
        self.value_results_false_words.configure(text = str(mistyped_words_count))

    def reset(self):

        if self.timer:
            self.is_reset = True
            self.wait_variable(self.var_is_reset)

        self.var_is_reset.set(False)

        self.label_timer.configure(text="01:00", text_color="#ECF2FF")

        self.is_reset = False

        self.is_time_up = False
        self.timer = 60
        self.timer_formatted = "01:00"

        self.current_word = ""

        self.current_word_index_minus_1_in_textbox = 0.0
        self.current_word_index_in_textbox = 0
        self.current_words_letter_index = 0
        self.current_letter_index_in_textbox = 0.0
        self.current_letter_index_in_textbox_int = int(self.current_letter_index_in_textbox)
        self.previous_letter_index_in_textbox_textbox_formatted = 1.0
        self.current_letter_index_in_textbox_textbox_formatted = 1.0
        self.next_letter_index_in_textbox_textbox_formatted = 1.1
        self.colors_by_index.clear()

        self.correct_characters_count = 0
        self.correct_words_count = 0
        self.mistyped_words_count = 0
        self.total_characters_count = 0

        self.place_words()

        self.entry.configure(state="normal")
        self.entry_variable.set("")
        self.entry.delete(0, "end")
        self.kick_off = self.entry_variable.trace_add('write', self.is_kick_off)

    def go_to_my_github(self):
        import webbrowser
        webbrowser.open_new(r"https://github.com/duruburak")

    def on_closing(self):
        # Terminate gracefully
        if self.is_ongoing:
            self.quit = True
            self.wait_variable(self.var_is_quit)

        self.destroy()



if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()