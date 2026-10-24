"""
FB Lite Login SDK - Test Script
Dùng để test module đăng nhập Facebook không cần giải captcha
"""
import subprocess
import json
import sys
import os

SDK_EXE = os.path.join(os.path.dirname(__file__), "fb_lite_login.exe")


def login(email: str, password: str) -> dict:
    result = subprocess.run(
        [SDK_EXE, email, password],
        capture_output=True,
        text=True,
        timeout=30,
    )
    try:
        return json.loads(result.stdout)
    except Exception:
        return {"status": "error", "message": result.stdout or result.stderr}


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        email = sys.argv[1]
        password = sys.argv[2]
    else:
        email = input("Email / UID / SĐT: ").strip()
        password = input("Mật khẩu: ").strip()

    print(f"\n[*] Đang đăng nhập: {email}")
    data = login(email, password)

    status = data.get("status")
    if status == "success":
        print(f"[✓] LOGIN THÀNH CÔNG")
        print(f"  UID          : {data.get('uid')}")
        print(f"  Access Token : {data.get('access_token')}")
        print(f"  Machine ID   : {data.get('machine_id')}")
        cookies = data.get("session_cookies", [])
        if cookies:
            cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies)
            print(f"  Cookies      : {cookie_str}")
    elif status == "checkpoint":
        print(f"[!] TÀI KHOẢN BỊ CHECKPOINT")
        print(f"  Link giải: {data.get('checkpoint_url')}")
    elif status == "wrong_password":
        print(f"[✗] SAI MẬT KHẨU")
    elif status == "not_found":
        print(f"[✗] EMAIL/UID KHÔNG TỒN TẠI")
    else:
        print(f"[?] Kết quả: {json.dumps(data, indent=2, ensure_ascii=False)}")
