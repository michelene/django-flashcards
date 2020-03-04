# A simple project using Django to implement flashcards

# Data Model (PostgreSQL back end)

- Category

  - category (CharField(100))

- Card

  - title (CharField(100))
  - question (RichTextField)
  - answer (RichTextField)
  - categories (ManyToManyField(Category))

- Deck
  - title (CharField(100))
  - cards (ManyToManyField(Card))

# Django Plugins Used

- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/)
