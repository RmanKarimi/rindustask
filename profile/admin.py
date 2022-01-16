from django.contrib import admin
from .models import Profile


class DataModelAdmin(admin.ModelAdmin):
    fields = ['id', 'created_date', 'updated_date']
    list_display = ['id', 'created_date']
    readonly_fields = ['id', 'created_date', 'updated_date']
    save_as = True


class UserDataModelAdmin(DataModelAdmin):
    fields = ['user']
    list_display = ['user']
    raw_id_fields = ['user']
    readonly_fields = ['user']
    save_as = True

    def __init__(self, *args, **kwargs):
        Klass = UserDataModelAdmin
        Klass_parent = DataModelAdmin

        super(Klass, self).__init__(*args, **kwargs)


    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Profile)
class UserAdmin(UserDataModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'IBAN')
    exclude = []