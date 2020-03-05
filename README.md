# A simple project using Django to implement flashcards

## Data Model (PostgreSQL back end)

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

## Django Plugins Used

- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/)

## Flash Card Content

- Toptal: https://www.toptal.com/javascript/interview-questions
- Front End: https://git.generalassemb.ly/michelene/interview-workshop/blob/master/lib/front-end.md
- Back End: https://git.generalassemb.ly/michelene/interview-workshop/blob/master/lib/back-end.md
