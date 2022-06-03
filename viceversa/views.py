from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	splited_list = list(user_text.split(' '))
	reverse_text =''.join(reversed(user_text))
	count_text = len(splited_list)
	return render(request, 'reverse.html', {'reversed_text':reverse_text, 'usertext':user_text, 'word_count':count_text})