# Описание таблиц БД "Киностудия"
from django.db import models


# ---------------------------- отношение: Киностудия -------------------------------
class CinemaStudio(models.Model):
    title = models.CharField('Название студии', max_length=25)
    director = models.CharField('Директор студии', max_length=50)
    date_sign = models.DateField('Дата основания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Киностудия'
        verbose_name_plural = 'Киностудия'


# ---------------------------- отношение: Фильмы -------------------------------
class Film(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    actors = models.TextField('Актеры')
    plot = models.TextField('Сюжет')
    date = models.DateField('Дата выхода в прокат')

    # метод для просмотра фильмов по заголовкам
    def __str__(self):
        return self.title

    # метод для переадресации на новую страницу
    # после обновления данных
    def get_absolute_url(self):
        return f'/cineMania/{self.id}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


# ------------------------- отношение: Контактные данные ---------------------------------
class Contacts(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    phone = models.CharField('Номер телефона', max_length=11)
    email = models.EmailField('Почта')

    # метод для просмотра людей по фамилиям
    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


# ------------------------------ отношение: Актеры ---------------------------------------
class Actors(models.Model):
    # Контактные данные и актеры имеют связь один к одному
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE,
                                    primary_key=True, related_name='related_contact')
    # Актеры и фильмы имеют связь многие ко многим
    film = models.ManyToManyField(Film, related_name='related_actors')
    age = models.IntegerField('Возраст')
    sex = models.CharField('Пол', max_length=1)
    count_films = models.IntegerField('Фильмография')

    # метод для просмотра людей по фамилиям
    def __str__(self):
        return self.contacts.surname

    class Meta:
        verbose_name = 'Актера'
        verbose_name_plural = 'Актеры'


# ------------------------------ отношение: Работники ------------------------------------
class Workers(models.Model):
    # Контактные данные и работники имеют связь один к одному
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, primary_key=True,
                                    related_name='worker_contact')
    job_position = models.CharField('Должность', max_length=30)
    experience = models.IntegerField('Опыт работы')
    yearEnd_study = models.DateField('Дата окончания университета')
    degree = models.CharField('Степень', max_length=30)
    description = models.TextField('Комментарий о себе')

    # метод для просмотра людей по фамилиям
    def __str__(self):
        return self.job_position

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


# ---------------------------- отношение: Анкета --------------------------------
class Questionnaire(models.Model):
    age = models.IntegerField('Возраст анкетируемого')
    country = models.CharField('Страна проживания', max_length=50)
    city = models.CharField('Город проживания', max_length=50)
    level_education = models.CharField('Уровень образования', max_length=50)
    hobby = models.TextField('Хобби анкетируемого')
    favorite_movies = models.TextField('Любимые фильмы')
    desired_of_activity = models.TextField('Желаемый вид деятельности в студии')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


# ---------------------- отношение: Участники кастинга --------------------------
class CastingParticipants(models.Model):
    # Киностудия и участники кастинга имеют связь один ко многим
    cinemaStudio = models.ForeignKey(CinemaStudio, on_delete=models.CASCADE)
    # Контактные данные и участники кастинга имеют связь один к одному
    contact = models.OneToOneField(Contacts, on_delete=models.CASCADE,
                                   primary_key=False, related_name='casting_contact')
    questionnaire = models.OneToOneField(Questionnaire, on_delete=models.CASCADE,
                                         primary_key=True, related_name='casting_quest')

    def __str__(self):
        return self.сontact.surname

    class Meta:
        verbose_name = 'Участник кастинга'
        verbose_name_plural = 'Участники кастинга'


# ------------------------- отношение: Обратная связь -----------------------------
class Feedback(models.Model):
    # Киностудия и обратная_связь имеют связь один ко многим
    cinemaStudio = models.ForeignKey(CinemaStudio, on_delete=models.CASCADE)

    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта, для обратной связи с пользователем')
    country = models.CharField('Страна проживания', max_length=50)
    question = models.TextField('Вопрос к руководству киностудии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
