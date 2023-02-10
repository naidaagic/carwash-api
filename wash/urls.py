from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from wash.views import bill, user, washing_program, washing_step

urlpatterns = [
    path("user/", user.UserList.as_view(), name="user_list"),
    path("user/<int:pk>/", user.UserDetail.as_view(), name="user_detail"),
    path("bill/", bill.BillList.as_view(), name="bill_list"),
    path("bill/<int:pk>/", bill.BillDetail.as_view(), name="bill_detail"),
    path(
        "washing_program/",
        washing_program.WashingProgramList.as_view(),
        name="washing_program_list",
    ),
    path(
        "washing_program/<int:pk>/",
        washing_program.WashingProgramDetail.as_view(),
        name="washing_program_detail",
    ),
    path(
        "washing_step/",
        washing_step.WashingStepList.as_view(),
        name="washing_step_list",
    ),
    path(
        "washing_step/<int:pk>/",
        washing_step.WashingStepDetail.as_view(),
        name="washing_step_detail",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
