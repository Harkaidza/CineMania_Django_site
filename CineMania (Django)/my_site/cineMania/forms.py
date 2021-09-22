from .models import Film, Actors, Contacts, Workers
from django.forms import ModelForm, TextInput, DateInput, \
    Textarea, EmailInput, NumberInput, \
    Select, CheckboxSelectMultiple, FileInput


class FilmForm(ModelForm):
    class Meta:
        model = Film
        # поля таблицы которые будут отображаться при заполнении формы
        fields = ['title', 'actors', 'plot', 'date']

        # сама форма для заполнения информации о фильме
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "actors": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Актеры'
            }),
            "plot": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сюжет фильма'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выхода в прокат'
            }),
        }


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        # поля таблицы которые будут отображаться при заполнении формы
        fields = ['name', 'surname', 'phone', 'email']

        # сама форма для заполнения информации о фильме
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
        }


class ActorsForm(ModelForm):
    class Meta:
        model = Actors
        # поля таблицы которые будут отображаться при заполнении формы
        fields = ['contacts', 'age', 'sex', 'count_films', 'film']

        # сама форма для заполнения информации о фильме
        widgets = {
            "contacts": Select(attrs={
                'class': 'form-control'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "sex": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол актера'
            }),
            "count_films": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фильмография (количество фильмов)'
            }),
            "film": CheckboxSelectMultiple(attrs={
                'class': 'checkbox'})
        }


class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        # поля таблицы которые будут отображаться при заполнении формы
        fields = ['contacts', 'job_position', 'description', 'degree', 'yearEnd_study', 'experience']

        # сама форма для заполнения информации о фильме
        widgets = {
            "contacts": Select(attrs={
                'class': 'form-control'
            }),
            "job_position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Коментарий о себе'
            }),
            "degree": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Степень образования'
            }),
            "yearEnd_study": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания университета'
            }),
            "experience": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опыт работы'
            }),
        }
