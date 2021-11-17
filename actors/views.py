import json

from django.http         import JsonResponse
from django.views        import View

from actors.models       import Actor, Movie


class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(

            first_name      = data["first_name"],
            last_name       = data["last_name"],
            date_of_birth   = data["date_of_birth"]

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status = 201)
    
    def get(self, request):
        actors = Actor.objects.all()
        movies = Movie.objects.all()

        results = []
        for actor in actors:
            results.append(
                {
                    "last_name"   : actor.last_name,
                    "first_name"  : actor.first_name,
                    #"movie"      : list(movies.values("title").filter(actor = actor.id))
                    "movie"       :[{'title' : movie.title} for movie in movies.filter(actor = actor.id)]
                }
            )
        return JsonResponse({'results':results}, status=200)


class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        movie = Movie.objects.create(
            title          = data["title"],
            release_date   = data["release_date"],
            running_time   = data["running_time"],
            # actor        = Actor.objects.get(name = data["actor"])    

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        actors = Actor.objects.all()
        
        results = []
        
        for movie in movies:
            results.append(
                {
                    "title"          : movie.title,
                    "running time"   : movie.running_time,
                    "movie"        : [{'actor' : actor.first_name} for actor in movie.actor_set.all()]
                    }
                )
        
        
        return JsonResponse({'results' : results}, status = 200)


# Create your views here.
