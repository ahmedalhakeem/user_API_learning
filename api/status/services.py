import dataclasses
import datetime
from user import services as user_service
from typing import TYPE_CHECKING
from . import models as status_models
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework import exceptions

if TYPE_CHECKING:
    from .models import Status 
@dataclasses.dataclass
class StatusDataClass:
    content : str
    date_published: datetime.datetime = None
    user : user_service.UserDataClass = None
    id: int = None

    @classmethod
    def from_instance(cls, status_model: "Status") -> "StatusDataClass":
        return cls (
            content = status_model.content,
            date_published = status_model.date_published,
            id = status_model.id,
            user = status_model.user
        )
def create_status(user, status: "StatusDataClass") -> "StatusDataClass":
    status_create = status_models.Status.objects.create(
        content = status.content,
        user = user
    )
    return StatusDataClass.from_instance(status_model=status_create)

def status_per_user(user: "User")-> "StatusDataClass":
    status_list = status_models.Status.objects.filter(user=user)
    return [StatusDataClass.from_instance(single_status) for single_status in status_list]

def user_status_detail(user: "User", status_id)->"StatusDataClass":
    status = get_object_or_404(status_models.Status, pk=status_id)
    return StatusDataClass.from_instance(status_model=status)

def delete_user_status(user: "User", status_id: int)-> "StatusDataClass":
    status = get_object_or_404(status_models.Status, pk=status_id)
    if user.id != status.user.id:
        raise exceptions("you are not allowed bro")
    status.delete()

def update_user_status(user: "User", status_id: int, status_data: "StatusDataClass"):
    status_update = get_object_or_404(status_models.Status, pk=status_id)
    if user.id != status_update.user.id:
        raise exceptions("you are not allowed bro")
    status_update.content = status_data.content
    status_update.save()
    return StatusDataClass.from_instance(status_model=status_update)
