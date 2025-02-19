from django.contrib import admin
from .models import ServiceRequest, RequestUpdate, Customer, SupportRepresentative

class RequestUpdateInline(admin.TabularInline):
    model = RequestUpdate
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer__username', 'description')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RequestUpdateInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, RequestUpdate):
                instance.updated_by = request.user
            instance.save()
        formset.save_m2m()

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(SupportRepresentative)
class SupportRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_admin')
    list_filter = ('is_admin',)
