from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar


btn_swich_theme = "theme-light-dark"
name_apps = "Finansion"

color_1 = "#FFDB40"
color_2 = "#50026E"
color_3 = "#4EA429"

KV = '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'
            # badge_icon: "numeric-10"

            MDLabel:
                text: ''
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Wallet'
            icon: 'wallet'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Report'
            icon: 'chart-arc'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'  

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Setting'
            icon: 'cog'

            MDLabel:
                text: 'Setting page'
                halign: 'center'
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
