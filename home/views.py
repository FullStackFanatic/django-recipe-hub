from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples = [
        {'name': 'abhijit gupta', 'age': 22},
        {'name': 'rohan sawant', 'age': 24},
        {'name': 'Priya more', 'age': 23},
    ]

    # for people in peoples:
    #    if people['age'] :
    #        print("Yes")

    # vegetables = ["Pumpkin","Tomato","Potato"]

    text = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum laudantium beatae nulla numquam at minima in, eum sed nemo molestiae dolores illo qui quam rem adipisci velit laborum, voluptate a provident ullam! Perspiciatis beatae ratione saepe quidem voluptate animi numquam vero, vitae nobis aut non soluta ipsa magni delectus eaque fugiat quisquam obcaecati pariatur, accusamus sint aspernatur amet. Praesentium nihil similique, nemo hic neque asperiores! Voluptatibus, obcaecati maxime nemo vitae non impedit reprehenderit dolore excepturi rerum repellendus quo praesentium aspernatur, 
    officia temporibus, corrupti deserunt. Voluptatibus rem molestiae modi ipsam, commodi odit aliquam eos animi illo ullam, error nostrum, reiciendis exercitationem!'''

    return render(request, "home/index.html" , context ={'page': 'Django project','peoples': peoples, 'text': text})

def about(request):
    context ={'page': 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context ={'page': 'Contact'}
    return render(request, "home/contact.html", context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> heyyyyyyy.....!")