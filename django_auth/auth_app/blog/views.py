from django.shortcuts import render


posts = [
    {
        'author':'Grace',
        'title':'Django Python',
        'content':'First post',
        'date_posted':'December 09, 2020'
    },
    {
        'author':'Jane Doe',
        'title':'Django Python 2',
        'content':'Second post',
        'date_posted':'December 10, 2020'
    }
]

def home(request):
    context = {
        'posts':posts   #create a dictionary and set the value of the key to the posts array above
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})