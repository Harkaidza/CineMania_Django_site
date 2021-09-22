from django.shortcuts import render, redirect
from .models import Film, Actors, Contacts, Workers
from .forms import FilmForm, ActorsForm, ContactsForm, WorkersForm
from django.views.generic import DetailView, UpdateView, DeleteView


# ----------------------------Отношение: Кинопроекты------------------------
# сортируем вывод фильмов по дате их выхода в прокат
def cinema_home(request):
    films = Film.objects.order_by('-date')
    return render(request, 'cineMania/cinema_home.html', {'films': films})


# класс для просмотра подробной информации о фильме
class FilmsDetailView(DetailView):
    model = Film
    template_name = 'cineMania/details_view.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super(FilmsDetailView, self).get_context_data()
        current_film = self.get_object()
        context['film_actors'] = current_film.related_actors
        return context


# класс для обновления информации о фильме
class FilmsUpdateView(UpdateView):
    model = Film
    template_name = 'cineMania/film-update.html'
    form_class = FilmForm


# класс для удаления фильма
class FilmsDeleteView(DeleteView):
    model = Film
    context_object_name = 'film'
    success_url = '/cineMania/'
    template_name = 'cineMania/film-delete.html'


# функция для создания фильма
def create(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_home')
        else:
            error = 'Форма была заполнена неверно!'

    form = FilmForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cineMania/create_films.html', data)


# ---------------------------- Отношение: Контактные данные ------------------------
def create_contacts(request):
    error = ''
    if request.method == 'POST' and id == "workers":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_workers')
        else:
            error = 'Форма была заполнена неверно!'
    else:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_actors')
        else:
            error = 'Форма была заполнена неверно!'

    form = ContactsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cineMania/create_contacts.html', data)


# ---------------------------- Отношение: Актеры ------------------------
def actors(request):
    actor = Actors.objects.order_by('-count_films')
    return render(request, 'cineMania/actors.html', {'actors': actor})


# функция для добавления актера
def create_actors(request):
    error = ''
    if request.method == 'POST':
        form = ActorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actors')
        else:
            error = 'Форма была заполнена неверно!'

    form = ActorsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cineMania/create_actors.html', data)


# ---------------------------- Отношение: Работники ------------------------
def workers(request):
    worker = Workers.objects.order_by('contacts')
    return render(request, 'cineMania/workers.html', {'workers': worker})


# функция для добавления работника
def create_workers(request):
    error = ''
    if request.method == 'POST':
        form = WorkersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers')
        else:
            error = 'Форма была заполнена неверно!'

    form = WorkersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cineMania/create_workers.html', data)
