from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        return "Отрисована кнопка Windows"


class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Отрисован чекбокс Windows"


class MacButton(Button):
    def paint(self):
        return "Отрисована кнопка MacOS"


class MacCheckbox(Checkbox):
    def paint(self):
        return "Отрисован чекбокс MacOS"


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())


if __name__ == "__main__":
    windows_factory = WindowsFactory()
    mac_factory = MacFactory()

    render_ui(windows_factory)
    print("---")
    render_ui(mac_factory)
