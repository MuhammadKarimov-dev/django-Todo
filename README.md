# Optimal ToDo List

Bu loyiha Django framework yordamida yaratilgan vazifalar boshqarish tizimi. Foydalanuvchilar o'z vazifalarini yaratish, bajarilgan deb belgilash va o'chirish imkoniyatiga ega.

## Asosiy funksiyalar

- Vazifa yaratish (sarlavha, tavsif va bajarilish sanasi bilan)
- Vazifani bajarilgan deb belgilash
- Vazifani o'chirish
- Responsive dizayn
- Vazifalarni bajarilgan/bajarilmagan holatda ko'rsatish

## Texnologiyalar

- Python 3.x
- Django
- HTML5
- CSS3
- JavaScript

## O'rnatish

1. Loyihani klonlang:
```bash
https://github.com/MuhammadKarimov-dev/django-Todo
cd django-Todo
```

2. Virtual muhit yarating va faollashtiring:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac uchun
# yoki
venv\Scripts\activate  # Windows uchun
```

3. Kerakli paketlarni o'rnating:
```bash
pip install -r requirements.txt
```

4. Migratsiyalarni yarating va qo'llang:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Serverni ishga tushiring:
```bash
python manage.py runserver
```

## Loyiha strukturasi

```
optimal-todo/
├── manage.py
├── requirements.txt
├── templates/
│   └── index.html
└── todo/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── models.py
```

## Foydalanish

1. Brauzerda `http://localhost:8000` manzilini oching
2. Yangi vazifa qo'shish uchun formani to'ldiring
3. Vazifani bajarilgan deb belgilash uchun checkboxni belgilang
4. Vazifani o'chirish uchun "O'chirish" tugmasini bosing

## Xususiyatlar

- Zamonaviy va chiroyli interfeys
- Responsive dizayn (mobil qurilmalarga moslashgan)
- Vazifalarni bajarilgan/bajarilmagan holatda ko'rsatish
- Vazifalar uchun bajarilish sanasini belgilash
- Vazifalar uchun tavsif qo'shish imkoniyati

## Yaratuvchi

- Ism: [Sizning ismingiz]
- Email: [Sizning email manzilingiz]

## Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatilgan. Batafsil ma'lumot uchun `LICENSE` faylini ko'ring. 
