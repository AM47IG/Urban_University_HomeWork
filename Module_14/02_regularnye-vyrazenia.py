import re


def extract_image_links(html):
    pattern = (r'((?:https?://)(?P<site_name>[\w-]+.\w{2,3})(?:/[\w-]+)*/'
               r'(?P<file_name>[\w-]+(?:\.jpg|\.jpeg|\.png|\.gif)\'))')
    return re.finditer(pattern, html)


sample_html = ("<img src='https://example.com/awdfgeswgr/image1.jpg'> <img src='http://example.com/image2.png'> <img "
               "src='https://example.com/image3.gif'> <img "
               "src='https://urban-university.ru/members/courses/course999421818026/20240124-0000domasnee-zadanie-po"
               "-teme-regularnye-vyrazenia-737906319602/132154-awd_w.jpeg'>")
image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(f'{'':_^{len(image_link[0])+23}}')
        print('Ссылка на изображение:'.ljust(22), image_link[0])
        print('Сайт:'.ljust(22), image_link.group('site_name'))
        print('Имя файла:'.ljust(22), image_link.group('file_name'))
else:
    print("Нет ссылок с картинками в HTML тексте.")
