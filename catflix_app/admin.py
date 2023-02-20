from django.contrib import admin
from catflix_app.models import Movie
from catflix_app.models import Category
from catflix_app.models import Tag
from django.utils.html import format_html

# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    def preview(self, movie):
        """Render preview image as html image."""

        return format_html(
            f'<img style="height: 200px" src="/media/{movie.preview_image}" />'
        )

    def video(self, movie):
        """Render movie video as html image."""

        return format_html(
            f"""
            <video width="320" height="240" controls>
                <source src="/media/{movie.file}" type="video/mp4">
                Your browser does not support the video tag.
            </video>"""
        )

    preview.short_description = 'Movie image'
    video.short_description = 'Movie video'
    list_display = ['name', 'preview', 'video', 'description']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
admin.site.register(Tag)
