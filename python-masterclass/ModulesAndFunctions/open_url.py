import webbrowser

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
url1 = 'https://docs.python.org/3.10/library/webbrowser'
# webbrowser.open('https://docs.python.org/3.10/library/webbrowser')
# webbrowser.open('https://docs.python.org/3.10/library/webbrowser', new=1)
# webbrowser.open_new('https://docs.python.org/3.10/library/webbrowser')

# webbrowser.Chrome.open(url=url1)
# chrome = webbrowser.get(using='google-chrome')
chrome = webbrowser.get(chrome_path)
chrome.open_new(url1)
