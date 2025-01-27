FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌ها
COPY . /app

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# باز کردن پورت
EXPOSE 5000

# اجرای پروژه
CMD ["python", "app.py"]
