from django.contrib import admin
from .models import Rating, Comment, AvgRating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("author", "tank", "gun_rating", "mobility_rating", "detection_rating", "armor_rating", "cammo_rating", "overall_rating")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(AvgRating)
class AvgRatingAdmin(admin.ModelAdmin):
    list_display = ("tank", "avg_gun_rating", "avg_mobility_rating", "avg_detection_rating", "avg_armor_rating", "avg_cammo_rating", "avg_overall_rating")
