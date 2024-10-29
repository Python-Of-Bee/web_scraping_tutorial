from bs4 import BeautifulSoup

# Đọc tệp HTML
with open('SELENIUM DIR\google.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Phân tích HTML
soup = BeautifulSoup(html_content, 'lxml')

# Xóa tất cả các thẻ <style>
for style in soup.find_all('style'):
    style.decompose()

# Xóa tất cả các thẻ <link> có rel="stylesheet"
for link in soup.find_all('link', rel='stylesheet'):
    link.decompose()

# Xóa tất cả các thẻ <script>
for script in soup.find_all('script'):
    script.decompose()

# Xóa tất cả các thẻ <path>
for path in soup.find_all('path'):
    path.decompose()

# Xóa tất cả các thẻ <circle>
for path in soup.find_all('circle'):
    path.decompose()

# Xóa tất cả các thẻ <svg>
for path in soup.find_all('svg'):
    path.decompose()

# Xóa tất cả các thẻ <div> và <span> nếu không có nội dung bên trong
for tag in soup.find_all(['div', 'span', 'li']):
    if not tag.get_text(strip=True):  # Kiểm tra xem có nội dung hay không
        tag.decompose()  # Xóa thẻ nếu không có nội dung

# Xóa khoảng trống, dấu ngắt dòng và dấu enter thừa
for element in soup.find_all(True):  # Tìm tất cả các thẻ
    if element.string:
        # Loại bỏ khoảng trắng thừa và dấu ngắt dòng
        cleaned_string = ' '.join(element.string.split())  # Xóa khoảng trắng thừa
        cleaned_string = cleaned_string.replace('\n', ' ')  # Thay thế dấu




# Lưu lại tệp HTML đã xóa CSS
with open('cleaned_file.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Đã xóa tất cả mã CSS và lưu vào cleaned_file.html")
