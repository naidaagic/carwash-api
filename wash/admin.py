from django.contrib import admin

from wash.models.bill import Bill
from wash.models.user import User
from wash.models.washing_program import WashingProgram
from wash.models.washing_step import WashingStep

admin.site.register(User)
admin.site.register(WashingStep)
admin.site.register(WashingProgram)
admin.site.register(Bill)
