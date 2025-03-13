import datetime
from typing import Tuple
import customtkinter as ctk
import os
from PIL import Image
import json

# Устанавливаем начальный режим отображения и тему (без переключения)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Файл для хранения заметок в формате JSON
NOTES_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "notes.json")    

class NotesApp:
    # Устанавливаем начальный режим отображения и тему (без переключения)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    def __init__(self, master):
        self.root = master
        self.root.title("Заметки")
        self.root.geometry("1000x600")
        self.root.minsize(1000, 600)
        #self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "notes.ico"))
        self.notes = list()
        
        # Фиксированные цвета для dark-темы
        self.colors = {
            "bg": "#1e1e1e",
            "title_text": "white",
            "note_frame": "#111",
            "note_text": "white",
            "info_text": "#a5a5a5",
            "button": "#4D76DB"
        }

                # Создаем основной фрейм
        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=10, pady=20)
        self.title_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.title_frame.pack(side=ctk.TOP, fill=ctk.X, padx=45, pady=5)


        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text="Заметки",
            font=("Poppins", 30, "bold"),
            text_color=self.colors["title_text"],
            image=self.load_image("notes.png", (40, 40)),
            compound=ctk.LEFT,
            
        )

        self.add_button = ctk.CTkButton(
            self.title_frame,
            text="",
            image=self.load_image("plus.png", (35, 35)),
            width=0,
            fg_color="transparent",
            hover_color="#222",
            command=self.open_add_popup
        )

        self.add_button.pack(side=ctk.RIGHT, anchor="ne", padx=10)
        self.title_label.pack(side=ctk.LEFT, anchor="nw", padx=10)
        self.notes_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        self.notes_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=40, pady=10)
        

    def load_image(self, image_name: str, size: Tuple[int, int]) -> ctk.CTkImage:
        """Загружает изображение из папки images"""
        image_path = os.path.join(os.path.dirname(__file__), "images")
        full_path = os.path.join(image_path, image_name)
        return ctk.CTkImage(Image.open(full_path), size=size)

    def open_add_popup(self):
        """Открывает окно для добавления заметки"""
        self.open_note_popup(mode="add")

    
    def open_note_popup(self, mode: str = "add", note_index: int | None = None) -> None:
        """
        Универсальное окно для добавления или редактирования заметки.
            Если mode == "update", поля заполняются текущими данными заметки.    """
        popup = ctk.CTkToplevel(self.root, fg_color=self.colors["bg"])
        popup.overrideredirect(True)
        toplevel_width = 500
        toplevel_height = 620

        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        x = root_x + (root_width - toplevel_width) // 2
        y = root_y + (root_height - toplevel_height) // 2
        popup.geometry(f"{toplevel_width}x{toplevel_height}+{x}+{y - 40}")
        popup.resizable(False, False)
        #popup.attributes("-topmost", True)
        popup.wait_visibility()
        popup.grab_set()

        frame = ctk.CTkFrame(popup, fg_color=self.colors["note_frame"],
        border_color="#111", corner_radius=15)
        frame.pack(fill=ctk.BOTH, expand=True)

        # Заголовок окна
        header_frame = ctk.CTkFrame(frame, fg_color="transparent")
        header_inner = ctk.CTkFrame(header_frame, fg_color="transparent")
        header_text = "Добавить новую заметку" if mode == "add" else "Редактировать заметку"
        header_label = ctk.CTkLabel(
            header_inner,
            text=header_text,
            font=("IBM Plex Sans", 30, "bold"),
            text_color=self.colors["note_text"]
        )
        header_label.pack(side=ctk.LEFT, padx=10)
        close_btn = ctk.CTkButton(
            header_inner,
            text="",
            width=0,
            fg_color="transparent",
            hover_color="#333",
            image=self.load_image("x.png", (35, 35)),
            command=popup.destroy
        )
        close_btn.pack(side=ctk.RIGHT)
        header_inner.pack(side=ctk.TOP, fill=ctk.X, padx=20, pady=10)
        header_frame.pack(fill=ctk.X, pady=5)
        # Поле ввода заголовка
        title_frame = ctk.CTkFrame(frame, fg_color="transparent")
        title_lbl = ctk.CTkLabel(
            title_frame,
            text="Заголовок",
            font=("Poppins", 25, "bold"),
            text_color=self.colors["note_text"]
        )
        title_lbl.pack(side=ctk.TOP, anchor="nw", padx=30)
        title_entry = ctk.CTkEntry(
            title_frame,
            height=60,
            placeholder_text="",
            font=("Poppins", 25),
            fg_color="transparent",
            border_color="#cdcdcd",
            text_color=self.colors["note_text"]
        )
        title_entry.pack(side=ctk.TOP, fill=ctk.X, padx=30, pady=10)
        title_frame.pack(side=ctk.TOP, fill=ctk.X, pady=10)
        # Поле ввода описания заметки
        desc_frame = ctk.CTkFrame(frame, fg_color="transparent")
        desc_lbl = ctk.CTkLabel(
            desc_frame,
            text="Описание",
            font=("Poppins", 25, "bold"),
            text_color=self.colors["note_text"]
        )
        desc_lbl.pack(side=ctk.TOP, anchor="nw", padx=30, pady=5)
        desc_text = ctk.CTkTextbox(
            desc_frame,
            height=100,
            font=("Poppins", 25),
            fg_color="transparent",
            border_color="#cdcdcd",
            text_color=self.colors["note_text"],
            border_width=1
        )
        desc_text.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, padx=30, pady=10)
        desc_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True, pady=5)
        
        def save_action():
            '''
            Получаем данные из title и descr 
            Вызываем метод save_notes()
            Обновтить экран display_all_notes()
            Закрыть окно destroy()
            '''
            pass

        save_btn = ctk.CTkButton(
            frame,
            text="Сохранить заметку",
            fg_color=self.colors["button"],
            hover_color="#567DDC",
            font=("Poppins", 20),
            command=save_action
        )
        save_btn.pack(side=ctk.TOP, fill=ctk.X, ipady=15, pady=20, padx=30)

        # Если редактирование, заполняем поля данными заметки
        if mode == "update" and note_index is not None:
            note = self.notes[note_index]
            title_entry.insert(0, note["title"])
            desc_text.insert("1.0", note["description"])

        title_val = title_entry.get().strip()
        desc_val = desc_text.get("1.0", ctk.END).strip()

        if not title_val or not desc_val:
            print ("dsf")
            return # можно добавить сообщение об ошибке
        
        # Если редактирование, заполняем поля данными заметки
        if mode == "update" and note_index is not None:
            note = self.notes[note_index]
            title_entry.insert(0, note["title"])
            desc_text.insert("1.0", note["description"])

        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%d.%m.%Y")

        self.notes.append(new_note)

        new_note = {
            "title": title_val,
            "description": desc_val,
            "date": formatted_time,
            "timestamp": current_datetime.timestamp(),
        }

        self.notes.append(new_note)
        self.save_notes()


    def save_notes(self):
        """Сохраняет заметки в файл JSON"""
        try:
            with open(NOTES_FILE, "w", encoding="utf-8") as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Ошибка при сохранении заметок:", e)


if __name__ == "__main__":
    root = ctk.CTk()
    app = NotesApp(root)
    root.mainloop()