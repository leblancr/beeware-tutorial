"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import faker
import httpx


def greeting(name):
    if name:
        return f"Hello, {name}"
    else:
        return "Hello, stranger"

class Beewaretutorial(toga.App):
    def startup(self):
        main_box = toga.Box(direction=COLUMN)

        name_label = toga.Label(
            "Your name: ",
            margin=(0, 5),
        )

        self.name_input = toga.TextInput(flex=1)

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            margin=5,
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self, widget):
        fake = faker.Faker()
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        await self.main_window.dialog(
            toga.InfoDialog(
                greeting(self.name_input.value),
                f"A message from {fake.name()}: {payload['body']}",
            )
        )


def main():
    return Beewaretutorial()  # instance of our class
