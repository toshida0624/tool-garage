import pyperclip
import pyotp
import os
import time
# OTPを生成
totp = pyotp.TOTP("{YOUR_SECRET_KEY}")
result = totp.now()
# 結果をクリップボードにコピー
pyperclip.copy(result)
time.sleep(1)  # クリップボードにコピーする時間を確保
# ターミナルを閉じる
os.system("osascript -e 'tell application \"Terminal\" to quit'")