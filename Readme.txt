### ReadMe for Python Code

This Python script is a user management system that simulates a registration and login system with additional features like course selection, placement tests, and password recovery. Here's a breakdown of how the code works and what it offers:

---

### Key Features:
1. **Signup**:
    - Users are asked to provide a unique username, password, email, and birth year.
    - Password validation is performed with checks for:
        - Minimum length of 8 characters
        - At least one lowercase letter
        - At least one uppercase letter
        - At least one digit
    - Users can recover their password by answering security questions (favorite color and car).
    - A random ID code is generated for each user, along with a registration timestamp.
    - The user data is saved to a `db.json` file for persistence.

2. **Login**:
    - Users can log in using their username and password.
    - Upon successful login, they are presented with three options:
        - **Course Registration**: Users can choose to register for one of the available courses (ML, Programming, Math).
        - **Placement Test**: Users can take a test with multiple-choice questions. Their performance is graded and saved.
        - **Password Recovery**: Users can reset their password by answering the same security questions (favorite color and car).

3. **Course Registration**:
    - Users can select from three available courses:
        - Learning Machine Learning (ML)
        - Learning Programming
        - Learning Math
    - Each course has its own unique registration list.
    - If a user has already signed up for a course, they are prompted to choose a different one.

4. **Placement Test**:
    - A quiz with 5 multiple-choice questions is provided to users who select the placement test option.
    - Correct answers increase the user's score, and their grade is saved to the database.
    - The test checks for general knowledge, such as geography and history.

5. **Password Recovery**:
    - If the user forgets their password, they can recover it by answering the security questions ("What is your favorite color?" and "What is your favorite car?").
    - After answering the questions correctly, users are allowed to set a new password.

---

### File Handling:
- The code interacts with several JSON files to load and save data:
    - **db.json**: Stores the user information such as username, password, email, birth year, and ID code.
    - **quiz.json**: Stores the questions and answers for the placement test.
    - **math.json, programming.json, ml.json**: These store the registration lists for the courses.

---

### How It Works:
1. **Signup Process**:
   - The user is prompted to enter their username, password, email, and birth year.
   - After validating the input, the user's data is saved to `db.json`.

2. **Login Process**:
   - The user enters their username and password.
   - If correct, they can choose to register for a course, take the placement test, or reset their password.

3. **Course Registration**:
   - The user selects a course, and if they haven't already registered for it, they are successfully added to the course's list.

4. **Placement Test**:
   - The user answers a series of questions. Their score is calculated and saved to the database.

5. **Password Recovery**:
   - If the user forgets their password, they answer security questions to recover it.

---

### Requirements:
- Python 3.x
- `json` module (Standard Python library)

### Example Usage:

```bash
🔷hello and welcome to our final project🔷
🔷enter your choice 🔷:
🔷 1) signup
🔷 2) login
```

- **Option 1**: Sign up as a new user.
- **Option 2**: Log in with an existing account.

---

### Important Notes:
- The program loads and saves data to `json` files. Make sure you have write permissions to the directory where these files are stored.
- Passwords are stored in plaintext in this example, which is not secure for production use. Consider implementing password hashing (e.g., using `bcrypt` or `hashlib`) for better security in a real-world scenario.

---

### Conclusion:
This script provides a simple system for managing user registrations, course selections, and password recovery. It uses JSON files for storing and loading data, allowing persistence across program executions.





---------------------------------------------------------------- فارسی ------------------------------------------------------------------------

### راهنمای استفاده از کد پایتون

این اسکریپت پایتون یک سیستم مدیریت کاربران است که فرآیند ثبت‌نام و ورود به سیستم را شبیه‌سازی می‌کند و ویژگی‌های اضافی مانند انتخاب دوره، آزمون جایگاه و بازیابی رمز عبور را ارائه می‌دهد. در اینجا توضیحی از نحوه کارکرد کد و ویژگی‌های آن آورده شده است:

---

### ویژگی‌های اصلی:
1. **ثبت‌نام (Signup)**:
    - از کاربران خواسته می‌شود تا نام کاربری، رمز عبور، ایمیل و سال تولد خود را وارد کنند.
    - اعتبارسنجی رمز عبور شامل بررسی موارد زیر است:
        - حداقل طول 8 کاراکتر
        - حداقل یک حرف کوچک
        - حداقل یک حرف بزرگ
        - حداقل یک عدد
    - کاربران می‌توانند در صورت فراموشی رمز عبور، با پاسخ به سوالات امنیتی (رنگ مورد علاقه و ماشین مورد علاقه) رمز عبور خود را بازیابی کنند.
    - یک کد شناسایی تصادفی برای هر کاربر ایجاد می‌شود و زمان ثبت‌نام ذخیره می‌شود.
    - داده‌های کاربران در فایل `db.json` ذخیره می‌شود.

2. **ورود (Login)**:
    - کاربران می‌توانند با استفاده از نام کاربری و رمز عبور خود وارد سیستم شوند.
    - پس از ورود موفقیت‌آمیز، سه گزینه به آنها نمایش داده می‌شود:
        - **ثبت‌نام در دوره**: کاربران می‌توانند یکی از دوره‌های موجود (یادگیری ML، برنامه‌نویسی، ریاضی) را انتخاب کنند.
        - **آزمون جایگاه**: کاربران می‌توانند در یک آزمون تست شرکت کنند.
        - **بازیابی رمز عبور**: کاربران می‌توانند رمز عبور خود را با پاسخ به سوالات امنیتی بازیابی کنند.

3. **ثبت‌نام در دوره‌ها**:
    - کاربران می‌توانند یکی از سه دوره موجود را انتخاب کنند:
        - یادگیری ماشین (ML)
        - یادگیری برنامه‌نویسی
        - یادگیری ریاضی
    - هر دوره یک لیست ثبت‌نام مجزا دارد.
    - اگر کاربری قبلاً در یک دوره ثبت‌نام کرده باشد، از او خواسته می‌شود تا دوره دیگری انتخاب کند.

4. **آزمون جایگاه**:
    - آزمون شامل 5 سوال چند گزینه‌ای است که به کاربران ارائه می‌شود.
    - پاسخ‌های صحیح به نمره کاربر افزوده می‌شود و نمره او ذخیره می‌شود.
    - این آزمون سوالاتی در مورد اطلاعات عمومی مانند جغرافیا و تاریخ دارد.

5. **بازیابی رمز عبور**:
    - اگر کاربر رمز عبور خود را فراموش کند، می‌تواند آن را با پاسخ به سوالات امنیتی (رنگ مورد علاقه و ماشین مورد علاقه) بازیابی کند.
    - پس از پاسخ درست به سوالات، کاربر می‌تواند رمز عبور جدیدی تنظیم کند.

---

### نحوه ذخیره‌سازی فایل‌ها:
- این کد با چند فایل JSON برای بارگذاری و ذخیره‌سازی داده‌ها تعامل دارد:
    - **db.json**: اطلاعات کاربران مانند نام کاربری، رمز عبور، ایمیل، سال تولد و کد شناسایی را ذخیره می‌کند.
    - **quiz.json**: سوالات و پاسخ‌های آزمون جایگاه را ذخیره می‌کند.
    - **math.json, programming.json, ml.json**: این فایل‌ها لیست ثبت‌نام‌های دوره‌ها را ذخیره می‌کنند.

---

### نحوه عملکرد:
1. **فرآیند ثبت‌نام**:
   - از کاربر خواسته می‌شود نام کاربری، رمز عبور، ایمیل و سال تولد خود را وارد کند.
   - پس از اعتبارسنجی ورودی‌ها، اطلاعات کاربر در فایل `db.json` ذخیره می‌شود.

2. **فرآیند ورود**:
   - کاربر نام کاربری و رمز عبور خود را وارد می‌کند.
   - اگر وارد شدن موفقیت‌آمیز باشد، کاربر می‌تواند برای یکی از گزینه‌های ثبت‌نام در دوره، آزمون جایگاه یا بازیابی رمز عبور انتخاب کند.

3. **ثبت‌نام در دوره‌ها**:
   - کاربر یکی از دوره‌ها را انتخاب می‌کند، و اگر قبلاً در آن دوره ثبت‌نام نکرده باشد، به لیست دوره اضافه می‌شود.

4. **آزمون جایگاه**:
   - کاربر در یک سری سوالات چند گزینه‌ای شرکت می‌کند. نمره او محاسبه شده و در پایگاه داده ذخیره می‌شود.

5. **بازیابی رمز عبور**:
   - اگر کاربر رمز عبور خود را فراموش کند، می‌تواند آن را با پاسخ به سوالات امنیتی بازیابی کرده و رمز عبور جدیدی تنظیم کند.

---

### الزامات:
- پایتون نسخه 3.x
- ماژول `json` (کتابخانه استاندارد پایتون)

### نمونه استفاده:

```bash
🔷hello and welcome to our final project🔷
🔷enter your choice 🔷:
🔷 1) signup
🔷 2) login
```

- **گزینه 1**: ثبت‌نام به عنوان یک کاربر جدید.
- **گزینه 2**: ورود به سیستم با یک حساب کاربری موجود.

---

### نکات مهم:
- این برنامه با فایل‌های `json` تعامل دارد. لطفاً مطمئن شوید که دسترسی نوشتن به دایرکتوری که این فایل‌ها در آن ذخیره می‌شوند را دارید.
- در این نمونه، رمز عبور به صورت متنی ذخیره می‌شود که در یک سیستم واقعی توصیه نمی‌شود. برای امنیت بیشتر در دنیای واقعی، باید از تکنیک‌های هش کردن رمز عبور (مانند `bcrypt` یا `hashlib`) استفاده کنید.

---

### نتیجه‌گیری:
این اسکریپت یک سیستم ساده برای مدیریت ثبت‌نام‌های کاربران، انتخاب دوره‌ها، آزمون جایگاه و بازیابی رمز عبور فراهم می‌کند. از فایل‌های JSON برای ذخیره و بارگذاری داده‌ها استفاده می‌کند تا اطلاعات کاربران در طول اجرای برنامه حفظ شوند.