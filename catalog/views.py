from django.shortcuts import render


# Create your views here.
def home(request):

    if request.method == 'POST':
        search = request.POST.get('search')

        print(f'Search: {search}')

    return render(request, 'catalog/home.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        search = request.POST.get('search')

        if search is not None:
            print(f'Search: {search}')
        else:
            print(f'Имя: {name}\nЭл.Почта: {email}\nТелефон:{phone}')

    return render(request, 'catalog/contacts.html')
