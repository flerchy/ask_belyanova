from django.shortcuts import render

# Create your views here.

def index(request):
	print request.GET
	print request.POST
	values = []
	for key in request.GET.keys():
		values.append({'key': key, 'value': request.GET[key]})
	return render(request, 'index.html', {'get_query': values})
	for key in request.POST.keys():
		values.append({'key': key, 'value': request.POST[key]})
	return render(request, 'index.html', {'post_query': values})
