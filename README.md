# NiceGUI Example: Encapsulating Pages in Classes

This repository is a minimal **NiceGUI** example that demonstrates a clean pattern for **encapsulating UI pages into Python classes**.

Instead of putting all UI code inside the `@ui.page(...)` functions, each page is implemented as a class with a `render()` method, while the route functions only instantiate the class and call `render()`.

## What it shows

- How to define pages as **classes** (`PageOne`, `PageTwo`)
- How each class can:
  - render its own UI via `render()`
  - handle its own navigation/actions via methods (e.g. `go_to_page_2`)
- How to register routes using NiceGUI’s `@ui.page(...)` decorator

## Project structure

- `main.py` – the full example (two pages and navigation between them)

## Pages / Routes

- `/` renders **Page 1**
- `/page2` renders **Page 2**

Each page has a button to navigate to the other page using:

- `ui.navigate.to("/page2")`
- `ui.navigate.to("/")`

## Requirements

- Python 3
- `nicegui`

Install dependencies:

```bash
pip install nicegui
```

## Run

From the repository root:

```bash
python main.py
```

NiceGUI will start a local web server (it will print the address in the terminal). Open it in your browser to test the navigation.

## Why this pattern?

Encapsulating pages in classes helps when your app grows:

- better organization (page-specific UI and logic stays together)
- easier reuse (components/pages can be instantiated/configured)
- simpler testing and maintenance
