from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar


btn_swich_theme = "theme-light-dark"
name_apps = "Finansion"

KV = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDTopAppBar:
        title: "''' +  name_apps  + '''"
        right_action_items: [["''' +  btn_swich_theme  + '''", lambda x: app.theme_style()]]

    MDLabel:
        text: "This theme style - {}".format(app.theme_cls.theme_style)
        halign: "center"
        font_style: "H5"
        bold: True
        allow_selection: True

        
    MDBottomAppBar:

        MDTopAppBar:
            icon: "plus"
            type: "bottom"
            on_action_button: app.see_message_tests(self.icon)
'''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        return Builder.load_string(KV)

    def see_message_tests(self, button):
        Snackbar(text="Add transaction...").open()

    def theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )




if __name__ == '__main__':
    app = MainApp()
    app.run()
