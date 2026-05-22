# Ninja Gold

A Django mini-game where the player earns or loses gold by visiting different locations.

---

# Features

- Starts user with 0 gold
- Uses Django session to save gold amount
- Uses Django session to save activity history
- Four locations:
  - Farm
  - Cave
  - House
  - Quest
- Uses hidden inputs in forms
- Uses POST requests
- Displays activity log
- Includes reset button

---

# Technologies Used

- Python
- Django
- HTML
- CSS
- Django Session

---

# Project Structure

```bash
ninja_gold/
│
├── manage.py
├── README.md
│
├── ninja_gold/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── gold_app/
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── index.html
    │
    └── static/
        └── style.css
```
