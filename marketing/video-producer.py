from html2image import Html2Image
hti = Html2Image()
hti.screenshot(
    html_file='word.html', css_file='word.css',
    save_as='blue_page.png',size=(1080, 1920)
)