# A simple project using Django to implement flashcards

# Data Model (PostgreSQL back end)

- Category
  - category (CharField(100))
- Card

  - question (MDTextField)
  - answer (MDTextField)
  - category (ForeignKey)

- (Future) Deck

# Django Plugins Used

- djangorestframework
- django-cors-headers
- [django-mdeditor](https://developpaper.com/implementation-of-beautiful-django-markdown-rich-text-app-plug-in/)
