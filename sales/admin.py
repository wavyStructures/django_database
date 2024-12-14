from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype


class CustomerAdmin(admin.ModelAdmin):
    list_filter=["first_name", "last_name"]
    # list_display=["last_name", "account"]
    readonly_fields=["account"]

prepopulated_fields = {"slug":["first_name", "last_name"]}

fieldsets = [
    (
        None, 
        {
            "fields": [
                "first_name",
                "last_name",
                "newsletter_abo",
                "email_address",
                "account"]
        },
    ),
    (
        "Advanced options",
        {
            "classes": ["collapse"],
            "fields": ["newsletter_abo", "slug"],
        },
    ), 
]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Order)
# Register your models here.


 