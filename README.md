# FB Lite Login SDK

Đăng nhập Facebook qua native mobile protocol — không cần giải captcha.

## Yêu cầu
- Windows 10/11 (64-bit)
- Không cần cài Python

## Cách dùng

### Chạy CLI
```bash
fb_lite_login.exe email@gmail.com matkhau123
```

### Tích hợp vào code Python
```python
import subprocess, json

def fb_login(email, password):
    result = subprocess.run(
        ["fb_lite_login.exe", email, password],
        capture_output=True, text=True, timeout=30
    )
    return json.loads(result.stdout)

data = fb_login("email@gmail.com", "password123")
if data["status"] == "success":
    print(data["access_token"])
```

## Output JSON

| status | Ý nghĩa |
|--------|---------|
| `success` | Đăng nhập thành công — có `access_token`, `uid`, `session_cookies` |
| `checkpoint` | Tài khoản bị khoá tạm — có `checkpoint_url` để mở khoá |
| `wrong_password` | Sai mật khẩu |
| `not_found` | Email/UID không tồn tại |
| `error` | Lỗi kết nối mạng |

## Update
Khi có bản mới: tải `fb_lite_login.exe` mới về thay thế file cũ.
