from django.shortcuts import render

posts = [
	{
		'author': 'nayeem',
		'title': 'Blog post one',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'

	},
	{
		'author': 'doe',
		'title': 'Blog post two',
		'content': 'Second post content',
		'date_posted': 'August 2f, 2018'

	}

]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'GOGO Company'})

 