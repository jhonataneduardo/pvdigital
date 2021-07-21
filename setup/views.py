from django.http import JsonResponse


def index(request):
    return JsonResponse({
        'project': 'PV Digital',
        'author': 'Jhonatan Eduardo <jhonatanepp@gmail.com>',
        'github': 'https://github.com/jhonataneduardo/pvdigital'
    })
