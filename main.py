#!/usr/bin/python3
#
# Example of encapsulating NiceGUI pages in classes
#

from nicegui import ui


class PageOne:
    def render(self):
        ui.label("Page 1")
        ui.button("Go to page 2", on_click=self.go_to_page_2)

    def go_to_page_2(self):
        # Navigate to another page
        ui.navigate.to("/page2")


class PageTwo:
    def render(self):
        ui.label("Page 2")
        ui.button("Go to page 1", on_click=self.go_to_page_1)

    def go_to_page_1(self):
        # Navigate to another page
        ui.navigate.to("/")


# The ui.page() decorator will register the pages
@ui.page("/")
def page_one():
    page = PageOne()
    page.render()


@ui.page("/page2")
def page_two():
    page = PageTwo()
    page.render()


def start():
    # Start the application
    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    start()
