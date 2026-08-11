"""
Belote Score Counter
A simple Kivy app to track scores for two teams (Us / Them) in Belote.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.core.window import Window

# Optional: comfortable default window size for desktop testing
#Window.size = (400, 650)


class RoundEntry:
    """Stores one round's added points and the totals right after it."""

    def __init__(self, us_added, them_added, us_total, them_total):
        self.us_added = us_added
        self.them_added = them_added
        self.us_total = us_total
        self.them_total = them_total


class BeloteRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(15), spacing=dp(10), **kwargs)

        self.us_total = 0
        self.them_total = 0
        self.history = []  # list of RoundEntry, most recent last

        # ---------- Title ----------
        title = Label(
            text="Belote Score Counter",
            font_size="24sp",
            bold=True,
            size_hint=(1, None),
            height=dp(50),
        )
        self.add_widget(title)

        # ---------- Totals display ----------
        totals_layout = GridLayout(cols=2, size_hint=(1, None), height=dp(90), spacing=dp(10))

        us_box = BoxLayout(orientation="vertical")
        us_box.add_widget(Label(text="US", font_size="20sp", bold=True))
        self.us_total_label = Label(text="0", font_size="32sp")
        us_box.add_widget(self.us_total_label)
        totals_layout.add_widget(us_box)

        them_box = BoxLayout(orientation="vertical")
        them_box.add_widget(Label(text="THEM", font_size="20sp", bold=True))
        self.them_total_label = Label(text="0", font_size="32sp")
        them_box.add_widget(self.them_total_label)
        totals_layout.add_widget(them_box)

        self.add_widget(totals_layout)

        # ---------- Input fields ----------
        inputs_layout = GridLayout(cols=2, size_hint=(1, None), height=dp(60), spacing=dp(10))

        self.us_input = TextInput(
            hint_text="Us points",
            input_filter="int",
            multiline=False,
            font_size="20sp",
            halign="center",
        )
        self.them_input = TextInput(
            hint_text="Them points",
            input_filter="int",
            multiline=False,
            font_size="20sp",
            halign="center",
        )
        inputs_layout.add_widget(self.us_input)
        inputs_layout.add_widget(self.them_input)

        self.add_widget(inputs_layout)

        # ---------- Action buttons ----------
        buttons_layout = BoxLayout(size_hint=(1, None), height=dp(55), spacing=dp(10))

        add_btn = Button(text="Add", background_color=(0.2, 0.7, 0.3, 1))
        add_btn.bind(on_press=self.add_round)

        undo_btn = Button(text="Undo", background_color=(0.9, 0.6, 0.1, 1))
        undo_btn.bind(on_press=self.undo_round)

        reset_btn = Button(text="Reset", background_color=(0.8, 0.2, 0.2, 1))
        reset_btn.bind(on_press=self.confirm_reset)

        buttons_layout.add_widget(add_btn)
        buttons_layout.add_widget(undo_btn)
        buttons_layout.add_widget(reset_btn)

        self.add_widget(buttons_layout)

        # ---------- History label ----------
        history_title = Label(
            text="Round history",
            font_size="18sp",
            bold=True,
            size_hint=(1, None),
            height=dp(30),
        )
        self.add_widget(history_title)

        # ---------- Scrollable history list ----------
        scroll = ScrollView(size_hint=(1, 1))
        self.history_layout = GridLayout(cols=1, size_hint_y=None, spacing=dp(4))
        self.history_layout.bind(minimum_height=self.history_layout.setter("height"))
        scroll.add_widget(self.history_layout)
        self.add_widget(scroll)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def add_round(self, instance):
        us_text = self.us_input.text.strip()
        them_text = self.them_input.text.strip()

        # Treat empty field as 0
        us_added = int(us_text) if us_text else 0
        them_added = int(them_text) if them_text else 0

        if us_text == "" and them_text == "":
            return  # nothing entered, do nothing

        self.us_total += us_added
        self.them_total += them_added

        entry = RoundEntry(us_added, them_added, self.us_total, self.them_total)
        self.history.append(entry)

        self.update_totals_display()
        self.add_history_row(entry, len(self.history))

        self.us_input.text = ""
        self.them_input.text = ""

    def undo_round(self, instance):
        if not self.history:
            return

        self.history.pop()

        if self.history:
            last = self.history[-1]
            self.us_total = last.us_total
            self.them_total = last.them_total
        else:
            self.us_total = 0
            self.them_total = 0

        self.update_totals_display()
        self.rebuild_history_display()

    def confirm_reset(self, instance):
        content = BoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        content.add_widget(Label(text="Reset all scores?\nThis cannot be undone."))

        buttons_row = BoxLayout(size_hint=(1, None), height=dp(45), spacing=dp(10))
        yes_btn = Button(text="Yes, reset")
        no_btn = Button(text="Cancel")
        buttons_row.add_widget(yes_btn)
        buttons_row.add_widget(no_btn)
        content.add_widget(buttons_row)

        popup = Popup(
            title="Confirm Reset",
            content=content,
            size_hint=(0.8, 0.35),
            auto_dismiss=False,
        )

        def do_reset(_instance):
            self.reset_all()
            popup.dismiss()

        yes_btn.bind(on_press=do_reset)
        no_btn.bind(on_press=popup.dismiss)
        popup.open()

    def reset_all(self):
        self.us_total = 0
        self.them_total = 0
        self.history = []
        self.update_totals_display()
        self.rebuild_history_display()

    # ------------------------------------------------------------------
    # Display helpers
    # ------------------------------------------------------------------
    def update_totals_display(self):
        self.us_total_label.text = str(self.us_total)
        self.them_total_label.text = str(self.them_total)

    def add_history_row(self, entry, round_number):
        row_text = (
            f"Round {round_number}:  "
            f"Us +{entry.us_added} (={entry.us_total})   |   "
            f"Them +{entry.them_added} (={entry.them_total})"
        )
        row_label = Label(
            text=row_text,
            size_hint_y=None,
            height=dp(28),
            font_size="14sp",
        )
        # Insert newest entries at the top of the list
        self.history_layout.add_widget(row_label, index=0)

    def rebuild_history_display(self):
        self.history_layout.clear_widgets()
        for i, entry in enumerate(self.history, start=1):
            self.add_history_row(entry, i)


class BeloteApp(App):
    def build(self):
        self.title = "Belote Score Counter"
        return BeloteRoot()



if __name__ == "__main__":
    BeloteApp().run()