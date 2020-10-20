from django import forms

from .models import ImageModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('title', 'category', 'image')

    def save(self, *args, **kwargs):
        try:
            this = ImageModel.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            pass
        super().save(*args, **kwargs)
