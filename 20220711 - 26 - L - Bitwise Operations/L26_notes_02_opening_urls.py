# 20220713 - Python - from: https://github.com/CodingPawn/python/blob/main/web-automation/web_automation.py


import webbrowser


def web_automation():
    urls = ("stackoverflow.com", "github.com", "neuralnine.com")        # URLs we're opening

    for url in urls:
        webbrowser.open("https://" + url)       # Not using a specific Chrome directory. Add 'https://' to the URL to open in default browser.


web_automation()
