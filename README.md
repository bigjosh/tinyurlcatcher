# TinyURLCatcher

A lightweight Windows utility that registers as an HTTP/HTTPS URL handler. When a URL is opened from a non-browser app (Slack, email, terminal, etc.), TinyURLCatcher displays it in a simple window so you can inspect and copy it.

## Requirements

- Windows 10/11
- Python 3 with tkinter (included by default)

## Setup

1. Register the URL handler:

   ```
   python register.py
   ```

2. Open **Windows Settings > Default Apps** and set **TinyURLCatcher** as your web browser.

## Usage

Click any link from a non-browser application. TinyURLCatcher will pop up showing the URL. From there you can:

- **Copy to Clipboard** — click the button to copy the full URL
- **Select the text** — click into the URL field to manually select/copy
- **Close** — dismiss the window

You can also run it directly:

```
python tinyurlcatcher.py "https://example.com/test?q=hello"
```

## Uninstall

Remove all registry entries:

```
python unregister.py
```

Then reset your default browser in **Windows Settings > Default Apps**.
