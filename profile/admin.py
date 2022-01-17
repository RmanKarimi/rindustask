from django.contrib import admin
from .models import Profile

class BaseAdmin(admin.ModelAdmin):
    fields = []
    list_filter = []
    list_display = []
    search_fields = []
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = []
    allowed_actions = []
    inlines = []

class DataModelAdmin(BaseAdmin):
    fields = ['id', 'create_date', 'update_date', ]
    list_display = ['id', 'create_date', ]
    list_filter = []
    search_fields = []
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = ['id', 'create_date', 'update_date', ]
    allowed_actions = []
    inlines = []
    save_as = True

    def __init__(self, *args, **kwargs):
        Klass = DataModelAdmin
        Klass_parent = BaseAdmin

        super(Klass, self).__init__(*args, **kwargs)

        self.fields = Klass_parent.fields + self.fields
        self.list_display = Klass_parent.list_display + self.list_display
        self.list_filter = Klass_parent.list_filter + self.list_filter
        self.search_fields = Klass_parent.search_fields + self.search_fields
        self.exclude = Klass_parent.exclude + self.exclude
        self.dynamic_raw_id_fields = Klass_parent.dynamic_raw_id_fields + self.dynamic_raw_id_fields
        self.raw_id_fields = Klass_parent.raw_id_fields + self.raw_id_fields
        self.readonly_fields = Klass_parent.readonly_fields + self.readonly_fields
        self.allowed_actions = Klass_parent.allowed_actions + self.allowed_actions
        self.inlines = Klass_parent.inlines + self.inlines



class UserDataModelAdmin(DataModelAdmin):
    fields = ['user', ]
    list_display = ['user', ]
    list_filter = []
    search_fields = []
    exclude = []
    raw_id_fields = ['user', ]
    dynamic_raw_id_fields = []
    readonly_fields = ['user', ]
    allowed_actions = []
    inlines = []
    save_as = True

    def __init__(self, *args, **kwargs):
        Klass = UserDataModelAdmin
        Klass_parent = DataModelAdmin

        super(Klass, self).__init__(*args, **kwargs)

        self.fields = Klass_parent.fields + self.fields
        self.list_display = Klass_parent.list_display + self.list_display
        self.list_filter = Klass_parent.list_filter + self.list_filter
        self.search_fields = Klass_parent.search_fields + self.search_fields
        self.exclude = Klass_parent.exclude + self.exclude
        self.dynamic_raw_id_fields = Klass_parent.dynamic_raw_id_fields + self.dynamic_raw_id_fields
        self.raw_id_fields = Klass_parent.raw_id_fields + self.raw_id_fields
        self.readonly_fields = Klass_parent.readonly_fields + self.readonly_fields
        self.allowed_actions = Klass_parent.allowed_actions + self.allowed_actions
        self.inlines = Klass_parent.inlines + self.inlines

    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Profile)
class UserAdmin(UserDataModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'IBAN']
    list_filter = []
    search_fields = []
    exclude = []
    raw_id_fields = []
    dynamic_raw_id_fields = []
    readonly_fields = []
    allowed_actions = []
    inlines = []

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()