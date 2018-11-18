from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


class ExampleView(View):
    def get(self, request):
        return render(request, 'laba4.html', {'my_variable': 'Орхидея'})


def tags(request):
    return render(request, 'tags.html')


def link(request):
    return render(request, 'link.html')


class OrdersView(View):
    def get(self, request):
        data = {
            'plants': [
                {'title': 'Орхидея', 'id': 1},
                {'title': 'Кактус', 'id': 2},
                {'title': 'Фикус', 'id': 3},
            ]
        }
        return render(request, 'Orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'plant': {
                'id': id
            }
        }
        return render(request, 'order.html', data)
