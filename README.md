# Purpose

I wanted to install Google's new Antigravity so I could try out the new Gemini 3.1 PRO, but it requires me to log into my google account on the same machine as the Antigravity install. This is a deal breaker for me becuase I keep a secutity gap between my machine that runs AI dev stuffs and my machine that logs into my important accounts (and so should you). So I wrote this utility to get around the issue. 

Follw the instructions below and then run the Antigravity install. Copy the URL and get it to your trusted machine and open that URL and log in. Then take the auth URL to localhost that log in returns and open that back on the Anitgravity machine and Antigravity will finish the install. 

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
