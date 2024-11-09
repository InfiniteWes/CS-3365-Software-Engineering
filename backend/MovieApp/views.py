from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Movie
from ReviewApp.models import Review
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
import json


def is_admin(user):
    return user.is_authenticated and user.is_staff

def get_movie_details(movie):
    return {
        'movie_id': movie.movie_id,
        'title': movie.title,
        'genre': movie.genre,
        'description': movie.description,
        'release_date': movie.release_date,
        'duration': movie.duration,
        'rating': movie.rating,
        'image': movie.image.url if movie.image else None,
        'location': movie.location
    }

def get_movie_list():
    movies = Movie.objects.all()
    return [get_movie_details(movie) for movie in movies]

def get_movie(movie_id):
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        return get_movie_details(movie)
    except ObjectDoesNotExist:
        return None
    
def get_movie_reviews_api(request, movie_id):
    movie = get_movie(movie_id)
    if movie is None:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    return JsonResponse({'movie': movie, 'reviews': get_movie_reviews(movie)})

def get_movie_list_api(request):
    return JsonResponse({'movies': get_movie_list()})

def update_rating(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    try:
        data = json.loads(request.body)
        movie_id = data.get('movie_id')
        new_rating = data.get('rating')
        if movie_id is None or new_rating is None:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        movie = Movie.objects.get(movie_id=movie_id)
        movie.rating = new_rating
        movie.save()
        return JsonResponse({'success': True})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def add_movie(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    try:
        data = json.loads(request.body)
        title = data.get('title')
        genre = data.get('genre')
        duration = data.get('duration')
        release_date = data.get('release_date')
        description = data.get('description')
        rating = data.get('rating')
        location = data.get('location')
        image = request.FILES.get('image')
        if title is None or genre is None or duration is None or release_date is None or description is None:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        movie = Movie.objects.create(
            title=title,
            genre=genre,
            duration=duration,
            release_date=release_date,
            description=description,
            rating=rating,
            image=image,
            location=location
        )
        return JsonResponse({'movie_id': movie.movie_id})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def update_movie(request, movie_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    try:
        data = json.loads(request.body)
        movie = Movie.objects.get(movie_id=movie_id)
        for key, value in data.items():
            setattr(movie, key, value)
        movie.save()
        return JsonResponse({'success': True})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def delete_movie(request, movie_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        movie.delete()
        return JsonResponse({'success': True})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

