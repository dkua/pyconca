import bcrypt

from pyramid.security import unauthenticated_userid
from pyramid.security import Allow
from pyramid.security import Authenticated
from pyramid.security import Everyone
from pyramid.security import ALL_PERMISSIONS

from pyconca.dao.user_dao import UserDao
from pyconca.dao.talk_dao import TalkDao
from pyconca.dao.schedule_slot_dao import ScheduleSlotDao


PERMISSIONS = {'admin': ['group:admin']}


def generate_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password(password, hashed):
    def _constant_time_is_equal(a, b):
        result = len(a) ^ len(b)
        for x, y in zip(a, b):
            result |= ord(x) ^ ord(y)
        return result == 0
    return _constant_time_is_equal(bcrypt.hashpw(password, hashed), hashed)


def is_admin(request):
    if getattr(request, 'user'):
        return request.user.is_admin
    return False


def get_user(request):
    user_id = unauthenticated_userid(request)
    if user_id:
        user_dao = UserDao(None)
        return user_dao.get(user_id)


def permission_finder(username, request):
    permissions = []
    user = request.user
    if user:
        for group in user.groups:
            permissions.extend(PERMISSIONS.get(group.name, []))
    return permissions


class RootFactory(object):
    __acl__ = [
        (Allow, 'group:admin', ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        self.request = request


class UserFactory(object):
    __acl__ = [
        (Allow, Everyone, 'user_create'),
        (Allow, Everyone, 'api_user_create'),

        (Allow, 'group:admin', 'user_index'),
        (Allow, 'group:admin', 'api_user_index'),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, id):
        return UserDao(self.request.user).get(id)


class TalkFactory(object):
    __acl__ = [
        (Allow, Authenticated, 'talk_create'),
        (Allow, Authenticated, 'api_talk_create'),

        (Allow, Authenticated, 'talk_index'),
        (Allow, Authenticated, 'api_talk_index'),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, id):
        return TalkDao(self.request.user).get(id)


class ScheduleSlotFactory(object):
    __acl__ = [
        (Allow, Authenticated, 'api_schedule_slot_create'),
        (Allow, Authenticated, 'api_schedule_slot_index'),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, id):
        return ScheduleSlotDao(self.request.user).get(id)
