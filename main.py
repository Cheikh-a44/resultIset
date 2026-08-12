"""
Belote Score Counter
Modern dark UI - Kivy
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


# =========================================================
# Window
# =========================================================

Window.clearcolor = (0.05, 0.05, 0.05, 1)


# =========================================================
# Round Entry
# =========================================================

class RoundEntry:

    def __init__(self, us_added, them_added, us_total, them_total):
        self.us_added = us_added
        self.them_added = them_added
        self.us_total = us_total
        self.them_total = them_total


# =========================================================
# Clickable Team Name
# =========================================================

class ClickableLabel(Label):

    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):
            self.show_edit_popup()
            return True

        return super().on_touch_down(touch)

    def show_edit_popup(self):

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(15)
        )

        text_input = TextInput(
            text=self.text,
            multiline=False,
            font_size="18sp",
            size_hint=(1, None),
            height=dp(50),
            halign="center",
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        content.add_widget(text_input)

        buttons = BoxLayout(
            size_hint=(1, None),
            height=dp(45),
            spacing=dp(10)
        )

        save_btn = Button(
            text="SAVE",
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1)
        )

        cancel_btn = Button(
            text="CANCEL",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )

        buttons.add_widget(save_btn)
        buttons.add_widget(cancel_btn)

        content.add_widget(buttons)

        popup = Popup(
            title="Edit Team Name",
            content=content,
            size_hint=(0.82, 0.4),
            auto_dismiss=False,
            separator_color=(1, 1, 1, 1)
        )

        def save_name(instance):

            new_name = text_input.text.strip()

            if new_name:
                self.text = new_name

            popup.dismiss()

        save_btn.bind(on_press=save_name)
        cancel_btn.bind(on_press=popup.dismiss)

        popup.open()


# =========================================================
# Main UI
# =========================================================

class BeloteRoot(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(10),
            **kwargs
        )

        # -------------------------------------------------
        # Game values
        # -------------------------------------------------

        self.us_total = 0
        self.them_total = 0

        self.us_sets = 0
        self.them_sets = 0

        self.history = []

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        title = Label(
            text="BELOTE",
            font_size="20sp",
            bold=True,
            size_hint=(1, None),
            height=dp(30),
            color=(1, 1, 1, 1)
        )

        self.add_widget(title)

        # -------------------------------------------------
        # Sets
        # -------------------------------------------------

        sets_layout = GridLayout(
            cols=2,
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(10)
        )

        self.us_sets_label = Label(
            text="0",
            font_size="25sp",
            bold=True,
            color=(1, 1, 1, 0)
        )

        self.them_sets_label = Label(
            text="0",
            font_size="25sp",
            bold=True,
            color=(1, 1, 1, 0)
        )

        sets_layout.add_widget(self.us_sets_label)
        sets_layout.add_widget(self.them_sets_label)

        self.add_widget(sets_layout)

        # -------------------------------------------------
        # Main Scores
        # -------------------------------------------------

        score_layout = GridLayout(
            cols=2,
            size_hint=(1, None),
            height=dp(165),
            spacing=dp(12)
        )

        # =================================================
        # US SIDE
        # =================================================

        us_box = BoxLayout(
            orientation="vertical",
            spacing=dp(3),
            padding=dp(5)
        )

        us_header = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=dp(38),
            spacing=dp(6)
        )

        self.us_label = ClickableLabel(
            text="US",
            font_size="19sp",
            bold=True,
            color=(1, 1, 1, 1)
        )

        us_t_button = Button(
            text="T",
            size_hint=(None, 1),
            width=dp(38),
            background_color=(0.18, 0.18, 0.18, 1),
            color=(1, 1, 1, 1),
            font_size="15sp",
            bold=True
        )

        us_t_button.bind(
            on_press=self.us_t_action
        )

        us_header.add_widget(self.us_label)
        us_header.add_widget(us_t_button)

        us_box.add_widget(us_header)

        self.us_total_label = Label(
            text="0",
            font_size="52sp",
            bold=True,
            color=(1, 1, 1, 1)
        )

        us_box.add_widget(self.us_total_label)

        score_layout.add_widget(us_box)

        # =================================================
        # THEM SIDE
        # =================================================

        them_box = BoxLayout(
            orientation="vertical",
            spacing=dp(3),
            padding=dp(5)
        )

        them_header = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=dp(38),
            spacing=dp(6)
        )

        self.them_label = ClickableLabel(
            text="THEM",
            font_size="19sp",
            bold=True,
            color=(1, 1, 1, 1)
        )

        them_t_button = Button(
            text="T",
            size_hint=(None, 1),
            width=dp(38),
            background_color=(0.18, 0.18, 0.18, 1),
            color=(1, 1, 1, 1),
            font_size="15sp",
            bold=True
        )

        them_t_button.bind(
            on_press=self.them_t_action
        )

        them_header.add_widget(self.them_label)
        them_header.add_widget(them_t_button)

        them_box.add_widget(them_header)

        self.them_total_label = Label(
            text="0",
            font_size="52sp",
            bold=True,
            color=(1, 1, 1, 1)
        )

        them_box.add_widget(self.them_total_label)

        score_layout.add_widget(them_box)

        self.add_widget(score_layout)

        # -------------------------------------------------
        # Inputs
        # -------------------------------------------------

        inputs = GridLayout(
            cols=2,
            size_hint=(1, None),
            height=dp(55),
            spacing=dp(12)
        )

        self.us_input = self.create_input()
        self.them_input = self.create_input()

        inputs.add_widget(self.us_input)
        inputs.add_widget(self.them_input)

        self.add_widget(inputs)

        # -------------------------------------------------
        # Action Buttons
        # -------------------------------------------------

        buttons = GridLayout(
            cols=3,
            size_hint=(1, None),
            height=dp(52),
            spacing=dp(8)
        )

        add_btn = Button(
            text="ADD",
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1),
            bold=True
        )

        undo_btn = Button(
            text="UNDO",
            background_color=(0.22, 0.22, 0.22, 1),
            color=(1, 1, 1, 1),
            bold=True
        )

        reset_btn = Button(
            text="RESET ALL",
            background_color=(0.22, 0.22, 0.22, 1),
            color=(1, 1, 1, 1),
            bold=True
        )

        add_btn.bind(on_press=self.add_round)
        undo_btn.bind(on_press=self.undo_round)
        reset_btn.bind(on_press=self.confirm_reset)

        buttons.add_widget(add_btn)
        buttons.add_widget(undo_btn)
        buttons.add_widget(reset_btn)

        self.add_widget(buttons)

        # -------------------------------------------------
        # History title
        # -------------------------------------------------

        history_title = Label(
            text="ROUND HISTORY",
            font_size="13sp",
            bold=True,
            size_hint=(1, None),
            height=dp(30),
            color=(0.75, 0.75, 0.75, 1)
        )

        self.add_widget(history_title)

        # -------------------------------------------------
        # History
        # -------------------------------------------------

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        self.history_layout = GridLayout(
            cols=2,
            size_hint_y=None,
            spacing=dp(2)
        )

        self.history_layout.bind(
            minimum_height=self.history_layout.setter("height")
        )

        scroll.add_widget(self.history_layout)

        self.add_widget(scroll)
        # App Info #####
        app_info = Label(
        text="By Cheikh_A\nVersion 1.0",
        font_size="11sp",
        color=(1, 1, 1, 0.45),
        halign="center",
        valign="middle",
        size_hint=(1, None),
        height=dp(38)
)

        app_info.bind(
    size=app_info.setter("text_size")
)

        self.add_widget(app_info)

    # =====================================================
    # Create Input
    # =====================================================

    def create_input(self):

        return TextInput(
            input_filter="int",
            multiline=False,
            font_size="20sp",
            halign="center",
            background_color=(0.13, 0.13, 0.13, 1),
            background_normal="",
            background_active="",
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            padding=[
                dp(10),
                dp(10),
                dp(10),
                dp(10)
            ]
        )

    # =====================================================
    # Update Sets Display
    # =====================================================

    def update_sets_display(self):

        # Hide Sets only when BOTH are 0
        if self.us_sets == 0 and self.them_sets == 0:

            self.us_sets_label.color = (1, 1, 1, 0)
            self.them_sets_label.color = (1, 1, 1, 0)

        else:

            self.us_sets_label.color = (1, 1, 1, 1)
            self.them_sets_label.color = (1, 1, 1, 1)

        self.us_sets_label.text = str(self.us_sets)
        self.them_sets_label.text = str(self.them_sets)

    # =====================================================
    # T Button - US
    # =====================================================

    def us_t_action(self, instance):

        self.us_sets += 2
        self.them_sets -= 2

        self.update_sets_display()

    # =====================================================
    # T Button - THEM
    # =====================================================

    def them_t_action(self, instance):

        self.them_sets += 2
        self.us_sets -= 2

        self.update_sets_display()

    # =====================================================
    # Add Round
    # =====================================================

    def add_round(self, instance):

        us_text = self.us_input.text.strip()
        them_text = self.them_input.text.strip()

        if us_text == "" and them_text == "":
            return

        us_added = int(us_text) if us_text else 0
        them_added = int(them_text) if them_text else 0

        self.us_total += us_added
        self.them_total += them_added

        entry = RoundEntry(
            us_added,
            them_added,
            self.us_total,
            self.them_total
        )

        self.history.append(entry)

        self.us_input.text = ""
        self.them_input.text = ""

        self.update_totals_display()
        self.rebuild_history_display()

        self.check_set_completion()

    # =====================================================
    # Check Set Completion
    # =====================================================

    def check_set_completion(self):

        if self.us_total < 100 and self.them_total < 100:
            return

        if self.us_total == self.them_total:
            return

        if self.us_total > self.them_total:

            if self.us_total >= 100:

                self.us_sets += 1
                self.update_sets_display()

                self.start_new_set()

        elif self.them_total > self.us_total:

            if self.them_total >= 100:

                self.them_sets += 1
                self.update_sets_display()

                self.start_new_set()

    # =====================================================
    # Start New Set
    # =====================================================

    def start_new_set(self):

        self.us_total = 0
        self.them_total = 0

        self.history.clear()

        self.update_totals_display()
        self.rebuild_history_display()

    # =====================================================
    # Undo
    # =====================================================

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

    # =====================================================
    # Reset Confirmation
    # =====================================================

    def confirm_reset(self, instance):

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(15)
        )

        message = Label(
            text=(
                "Reset EVERYTHING?\n\n"
                "Scores, sets and history\n"
                "will all return to 0."
            ),
            color=(1, 1, 1, 1)
        )

        content.add_widget(message)

        buttons = BoxLayout(
            size_hint=(1, None),
            height=dp(48),
            spacing=dp(10)
        )

        yes_btn = Button(
            text="RESET",
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1),
            bold=True
        )

        cancel_btn = Button(
            text="CANCEL",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )

        buttons.add_widget(yes_btn)
        buttons.add_widget(cancel_btn)

        content.add_widget(buttons)

        popup = Popup(
            title="Reset Everything",
            content=content,
            size_hint=(0.85, 0.42),
            auto_dismiss=False,
            separator_color=(1, 1, 1, 1)
        )

        yes_btn.bind(
            on_press=lambda x: self.reset_all(popup)
        )

        cancel_btn.bind(
            on_press=popup.dismiss
        )

        popup.open()

    # =====================================================
    # Reset Everything
    # =====================================================

    def reset_all(self, popup=None):

        self.us_total = 0
        self.them_total = 0

        self.us_sets = 0
        self.them_sets = 0

        self.history.clear()

        self.us_input.text = ""
        self.them_input.text = ""

        self.us_total_label.text = "0"
        self.them_total_label.text = "0"

        self.update_sets_display()

        self.history_layout.clear_widgets()

        if popup:
            popup.dismiss()

    # =====================================================
    # Update Display
    # =====================================================

    def update_totals_display(self):

        self.us_total_label.text = str(
            self.us_total
        )

        self.them_total_label.text = str(
            self.them_total
        )

    # =====================================================
    # Rebuild History
    # =====================================================

    def rebuild_history_display(self):

        self.history_layout.clear_widgets()

        for entry in reversed(self.history):

            us_label = Label(
                text=str(entry.us_added),
                size_hint_y=None,
                height=dp(25),
                font_size="18sp",
                halign="left",
                color=(1, 1, 1, 1)
            )

            us_label.bind(
                size=us_label.setter("text_size")
            )

            them_label = Label(
                text=str(entry.them_added),
                size_hint_y=None,
                height=dp(25),
                font_size="16sp",
                halign="right",
                color=(1, 1, 1, 1)
            )

            them_label.bind(
                size=them_label.setter("text_size")
            )

            self.history_layout.add_widget(
                us_label
            )

            self.history_layout.add_widget(
                them_label
            )


# =========================================================
# App
# =========================================================

class BeloteApp(App):

    def build(self):

        self.title = "Belote Score Counter"

        return BeloteRoot()


# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    BeloteApp().run()