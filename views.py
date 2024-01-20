from django.shortcuts import redirect,render
from . forms import *
from django.contrib import messages
from django.views import generic
from .models import Homework
from youtubesearchpython import VideosSearch
import requests
import wikipedia

from .forms import DashboardForm 

from .models import Todo  # Import the Todo model
from .forms import TodoForm  

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method=="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added form{request.user.username} successfully!")
    else:
        form=NotesForm()
    notes = Notes.objects.filter(user=request.user)

    context ={'notes':notes,'form':form}
    return render(request, 'dashboard/notes.html',context)
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
class NotesDetailView(generic.DetailView):
    model=Notes


    
    
def homework(request):
    if request.method=="POST":
        form=HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            homework=Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished = finished
            )
            homework.save()
            messages.success(request,f"Homework Added form{request.user.username} successfully!!")
    else:
        form=HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done=True
    else:
        homework_done=False
    context ={
        'homeworks':homework, 
        'homeworks_done':homework_done,
        'form':form,
        }
    return render(request, 'dashboard/homework.html',context)


def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    return redirect("homeworks")

def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homework")


 # Assuming you have a forms.py file in your app

"""def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)  # Corrected 'post' to 'POST'
        text = request.POST['text']
        video = VideosSearch(text, limit=50)
        result_list = []

        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],  # Corrected 'viewcount' to 'viewCount'
                'published': i['publishedTime'],
            }

            desc = ''
            if 'description' in i:
                desc = ''
                for j in i['description']:
                    desc += j['text']
                result_dict['description'] = desc

            result_list.append(result_dict)
            context = {
                'form': form,
                'results': result_list,
            }

        return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/youtube.html', context)"""


# youtube section

"""def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=50)
        result_list = []

        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
            }

            if 'thumbnails' in i and i['thumbnails']:
                result_dict['thumbnail'] = i['thumbnails'][0]['url']

            if 'description' in i:
                desc = ''
                for j in i['description']:
                    desc += j['text']
                result_dict['description'] = desc

            result_list.append(result_dict)

        context = {
            'form': form,
            'results': result_list,
        }

        return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/youtube.html', context)"""
def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=50)
        result_list = []

        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
            }

            thumbnail_info = i.get('thumbnails', [])
            if thumbnail_info:
                result_dict['thumbnail'] = thumbnail_info[0]['url']
            else:
                result_dict['thumbnail'] = None  # or some default value if needed

            description_info = i.get('description', [])
            desc = ''.join(j['text'] for j in description_info) if description_info else ''
            result_dict['description'] = desc

            result_list.append(result_dict)

        context = {
            'form': form,
            'results': result_list,
        }

        return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/youtube.html', context)

    
#todo section

def todo(request):
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                finished=False
            todo=Todo(
                user=request.user,
                
                title=request.POST['title'],
                
                is_finished = finished
            )
            todo.save()
            messages.success(request,f"Homework Added form{request.user.username} successfully!!")
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo)==0:
        todos_done=True
    else:
        todos_done=False
    context = {
    'form': form,
    'todos': todo,
    'todos_done': todos_done
    }
    return render(request, 'dashboard/todo.html',context)


def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    return redirect("todo")


def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")



"""def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r=requests.get(url)
        answer=r.json()
        result_list = []

        for i in range(10):
            result_dict = {
                
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail': answer['items'][i]['volumeInfo'].get('imageLink').get('thumbnail'),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink')
                
            }

            result_list.append(result_dict)
            context = {
            'form': form,
            'results': result_list,
            }

        return render(request, 'dashboard/books.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/books.html', context) """
        
  # Import your DashboardForm from the correct location

def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url = f"https://www.googleapis.com/books/v1/volumes?q={text}"
            r = requests.get(url)
            answer = r.json()
            result_list = []

            for item in answer.get('items', [])[:10]:
                volume_info = item.get('volumeInfo', {})

                result_dict = {
                    'title': volume_info.get('title', 'N/A'),
                    'subtitle': volume_info.get('subtitle'),
                    'description': volume_info.get('description'),
                    'count': volume_info.get('pageCount'),
                    'categories': volume_info.get('categories', []),
                    'rating': volume_info.get('pageRating'),
                    'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail'),
                    'preview': volume_info.get('previewLink')
                }

                result_list.append(result_dict)

            context = {
                'form': form,
                'results': result_list,
            }

            return render(request, 'dashboard/books.html', context)
    else:
        form = DashboardForm()

    context = {'form': form}
    return render(request, 'dashboard/books.html', context)


# dictionary section

def dictionary(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = f"https://api.dictionaryapi.dev/api/v2/entries/es_us/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics=answer[0]['phonetics'][0]['text']
            audio=answer[0]['phonetics'][0]['audio']
            definition=answer[0]['meanings'][0]['definition'][0]['definition']
            example=answer[0]['meanings'][0]['definition'][0]['example']
            synonyms=answer[0]['meanings'][0]['definition'][0]['synonyms']
            context={
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context={
                'form':form,
                'input':''
            }
        return render(request, 'dashboard/dictionary.html',context)
    else:
        form = DashboardForm()
    context = {'form': form}
    return render(request, 'dashboard/dictionary.html',context)
    
    


# Assuming this is part of your views.py

"""from django.shortcuts import render
from .forms import DashboardForm

def dictionary(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = f"https://api.dictionaryapi.dev/api/v2/entries/es_US/{text}"
        r = requests.get(url)
        answer = r.json()

        try:
            word_data = answer[0]  # Assuming the first entry contains the desired information

            phonetics = word_data.get('phonetics', [{}])[0].get('text', '')
            audio = word_data.get('phonetics', [{}])[0].get('audio', '')
            
            meanings = word_data.get('meanings', [])
            if meanings:
                first_meaning = meanings[0]
                definition = first_meaning.get('definition', '')
                examples = [example['example'] for example in first_meaning.get('examples', [])]
                synonyms = first_meaning.get('synonyms', [])
            else:
                definition = examples = synonyms = []

            context = {
                'form': form,
                'input': text,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'examples': examples,
                'synonyms': synonyms
            }
        except (IndexError, KeyError):
            context = {
                'form': form,
                'input': text,
                'error_message': 'No data found for the given text.'
            }

        return render(request, 'dashboard/dictionary.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/dictionary.html', context)
"""

"""def wiki(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        search=wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary
        }
        return render(request, 'dashboard/wiki.html',context)
    else:
        form = DashboardForm()
        context = {
            'form': form
        }
    return render(request, 'dashboard/wiki.html',context)"""
    
import warnings
from wikipedia import wikipedia
from django.shortcuts import render
from wikipedia.exceptions import WikipediaException
from .forms import DashboardForm  # Make sure to import your DashboardForm

# Suppress GuessedAtParserWarning

def wiki(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST.get('text', '')  # Use get to avoid MultiValueDictKeyError
        try:
            search = wikipedia.page(text)
            context = {
                'form': form,
                'title': search.title,
                'link': search.url,
                'details': search.summary
            }
        except WikipediaException as e:
            # Handle specific Wikipedia API exceptions
            context = {
                'form': form,
                'error_message': f"Error: {str(e)}"
            }
        return render(request, 'dashboard/wiki.html', context)
    else:
        form = DashboardForm()
        context = {'form': form}
        return render(request, 'dashboard/wiki.html', context)

# user registration form
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Accounted Created for{username} successfully!!")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)


def profile(request):
    homework = Homework.objects.filter(is_finished=False , user=request.user)
    todo = Todo.objects.filter(is_finished=False , user=request.user)
   
    if len(homework)==0:
        homework_done=True
    else:
        homework_done=False
    if len(todo)==0:
        todos_done=True
    else:
        todos_done=False
    context ={
        'homeworks':homework, 
        'todos': todo,
        'homeworks_done':homework_done,
        'todos_done': todos_done
        
    }
    return render(request, 'dashboard/profile.html',context)