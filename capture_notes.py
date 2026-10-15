from playwright.sync_api import sync_playwright
import os

html = os.path.abspath(r'C:\Users\Lenovo\高级网页设计\马蜂窝\index.html')
out = os.path.abspath(r'C:\Users\Lenovo\高级网页设计\notes_current.png')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 1200})
    page.goto('file:///' + html.replace('\\', '/'))
    page.wait_for_load_state('networkidle')
    # Find the notes section bounding box
    box = page.locator('.qyy-notes-header').bounding_box()
    if box:
        # capture a bit above and enough height for 4 items
        x = int(box['x'])
        y = max(0, int(box['y']) - 10)
        w = 760  # a bit wider than list
        h = 720
        page.screenshot(path=out, clip={'x': x, 'y': y, 'width': w, 'height': h})
    else:
        page.screenshot(path=out, full_page=True)
    browser.close()
print('saved', out)
