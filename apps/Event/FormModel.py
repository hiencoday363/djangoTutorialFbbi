from django import forms

from apps.Event.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        # fields = ['is_deleted']
        exclude = ['private_key']

    # def clean(self):
    #     cleaned_data = super().clean()

    def save(self, commit=True):
        # Save the provided password in hashed format
        event = super(EventForm, self).save(commit=False)

        if commit:
            event.save()
            # image_path = ImagePathModel()
            # image_path.event = event
            # image_path.image_url = 'path_1'
            # image_path.save()
        return event
