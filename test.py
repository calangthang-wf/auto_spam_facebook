import random
import string

# Mẫu tên đăng nhập của Gmail: "tênđăngnhậpgmail123"
pattern = "@gmail.com"

# Độ dài của tên đăng nhập
length = random.choice(range(20))

# Nhập số lượng tài khoản cần tạo
num_accounts = int(input("Nhập số lượng tài khoản cần tạo: "))

# Hàm tạo tên đăng nhập mới
def generate_username():
    # Tạo một chuỗi ngẫu nhiên từ các ký tự ABC123 với độ dài cho trước
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

    # Tạo tên đăng nhập mới dựa trên mẫu và chuỗi ngẫu nhiên
    username = random_string + pattern
    
    return username

generate_username()
# Tạo danh sách các tên đăng nhập mới
usernames = []
for i in range(num_accounts):
    usernames.append(generate_username())

# In danh sách các tên đăng nhập mới
print(usernames)