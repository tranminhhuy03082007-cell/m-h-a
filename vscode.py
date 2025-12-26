import sys

BASE_CHAR_CODE = ord('a')
ALPHABET_SIZE = 26

def encrypt(text, key):
    """
    Mã hóa văn bản (Dịch chuyển về phía sau k vị trí).
    
    Tham số:
    - text (str): Chuỗi văn bản gốc (chỉ chữ thường, không khoảng trắng, không dấu).
    - key (int): Khóa dịch chuyển.
    
    Trả về:
    - str: Chuỗi văn bản đã được mã hóa.
    """
    result = ""
    shift = key % ALPHABET_SIZE
    
    for char in text:
        original_index = ord(char) - BASE_CHAR_CODE
        
        new_index = (original_index + shift) % ALPHABET_SIZE
        
        new_char_code = new_index + BASE_CHAR_CODE
        
        result += chr(new_char_code)
        
    return result

def decrypt(text, key):
    """
    Giải mã văn bản (Dịch chuyển về phía trước k vị trí).
    
    Giải mã là quá trình ngược lại của mã hóa. 
    
    Tham số:
    - text (str): Chuỗi văn bản đã mã hóa.
    - key (int): Khóa dịch chuyển (giống khóa dùng để mã hóa).
    
    Trả về:
    - str: Chuỗi văn bản gốc.
    """
    result = ""
    shift = key % ALPHABET_SIZE
    
    for char in text:
        original_index = ord(char) - BASE_CHAR_CODE
        
        new_index = (original_index - shift + ALPHABET_SIZE) % ALPHABET_SIZE

        new_char_code = new_index + BASE_CHAR_CODE
        
        result += chr(new_char_code)
        
    return result

def get_user_input():
    """Yêu cầu người dùng nhập văn bản và khóa, có kiểm tra đầu vào cơ bản."""
    while True:
        text = input("Nhập chuỗi văn bản (chỉ a-z, chữ thường, không khoảng trắng): ").strip()
        if text and text.isalpha() and text.islower():
            break
        print("Lỗi: Văn bản không hợp lệ. Vui lòng chỉ nhập các chữ cái tiếng Anh (a-z, chữ thường, không khoảng trắng).")
    
    while True:
        try:
            key_str = input("Nhập khóa dịch chuyển (một số nguyên dương): ").strip()
            key = int(key_str)
            if key >= 0:
                return text, key
            else:
                print("Lỗi: Khóa phải là số nguyên không âm.")
        except ValueError:
            print("Lỗi: Khóa phải là một số nguyên.")

def display_menu():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    while True:
        print("\n--- CHƯƠNG TRÌNH MÃ HÓA CAESAR ---")
        print("1. Mã hóa văn bản")
        print("2. Giải mã văn bản")
        print("3. Thoát")
        
        choice = input("Vui lòng chọn chức năng (1, 2 hoặc 3): ").strip()
        
        if choice == '1':
            print("\n[CHỨC NĂNG MÃ HÓA]")
            text, key = get_user_input()
            cipher_text = encrypt(text, key)
            print(f"\n--- KẾT QUẢ ---")
            print(f"Văn bản gốc: {text}")
            print(f"Khóa dịch chuyển: {key}")
            print(f"Văn bản đã mã hóa: {cipher_text}")
            print("---------------")
            
        elif choice == '2':
            print("\n[CHỨC NĂNG GIẢI MÃ]")
            text, key = get_user_input() 
            plain_text = decrypt(text, key)
            print(f"\n--- KẾT QUẢ ---")
            print(f"Văn bản đã mã hóa: {text}")
            print(f"Khóa dịch chuyển: {key}")
            print(f"Văn bản đã giải mã: {plain_text}")
            print("---------------")
            
        elif choice == '3':
            print("Đã thoát chương trình. Tạm biệt!")
            sys.exit(0)
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if _name_ == "_main_":
    display_menu()
    