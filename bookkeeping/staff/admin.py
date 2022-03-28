from django.contrib import admin
from .models import Staff, Boss
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(Staff)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "post", "Salary_amount", "salary_paid", "boss", "level")
    list_filter = ("post",)

    def boss(self, obj):
        count = obj.post
        url = (
            reverse("admin:staff_boss_changelist")
            + "?"
            + urlencode({"subordinate_level": f"{obj.post}"})
        )
        return format_html('<a href="{}">{} Boss</a>', url, count)

    def level(self, obj):
        level = 4
        if obj.post == '0':
            level = 0
        if obj.post == '1':
            level = 1
        if obj.post == '2':
            level = 2
        if obj.post == '3':
            level = 3
        if obj.post == '4':
            level = 4
        return level

    actions = ['sweep']

    @admin.action(description='!!!Налоговая зашла!!!')
    def sweep(self, request, queryset):
        queryset.update(salary_paid=0)


@admin.register(Boss)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("boss_name", "subordinate_level")
