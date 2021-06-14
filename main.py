from tkinter import *
import csv
import pandas as pd

KEPCO_DATA = "kepco_conv.csv"   # 한국전력공사 용어사전
KHNP_DATA = "khnp_conv.csv"     # 한국수력원자력 용어사전

# Load csv datasets using pandas
kepco = pd.read_csv(KEPCO_DATA)
khnp = pd.read_csv(KHNP_DATA)

# An action for search button
def search(event=None):
    data_selected = current_dropdown.get()
    if data_selected == "한국전력공사":
        data = kepco
    elif data_selected == "한국수력원자력":
        data = khnp
    else:
        # didn't select any of dropdown menus
        return

    # retrieving search input and clearing fields
    word = entry_input.get()
    entry_input.delete(0, END)
    output_text.delete("0.0", "end")

    # formatting the search result
    try:
        word_def = word + ": " + data.loc[data["용어"] == word, "용어설명"].values[0]
    except:
        word_def = "단어를 찾을 수 없습니다."

    # putting result to the output field
    output_text.insert(END, word_def)

# loading tkinter window
window = Tk()
window.title("공공데이터 사전 검색")
window.bind("<Return>", search)     # bind keyboard event to search function

Label(window, text="검색하려는 단어를 입력해주세요.")\
    .grid(row=0, column=0, columnspan=2, sticky="w")

# dropdown menu
current_dropdown = StringVar(window)
current_dropdown.set("데이터 선택")
dropdown_options = {"한국전력공사", "한국수력원자력"}
dropdown_menu = OptionMenu(window, current_dropdown, *dropdown_options)
dropdown_menu.grid(row=1, column=0, sticky="we")
dropdown_menu.config(width=10)

# input field
entry_input = Entry(window, bg="light blue")
entry_input.grid(row=1, column=1, sticky="we")

# search button
Button(window, width=5, text="검색", command=search)\
    .grid(row=1, column=2, sticky="w")

# output field
Label(window, text="용어설명")\
    .grid(row=2, column=0, sticky="w")
output_text = Text(window, width=50, height=6, wrap=WORD, background="light blue")
output_text.grid(row=4, column=0, columnspan=3, sticky="we")

# initializing the program
if __name__ == "__main__":
    window.mainloop()