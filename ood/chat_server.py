from enum import Enum
from datetime import datetime

class ChatServer:
    def __init__(self):
        pass

class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.status = UserStatus()
        self.friends = {}           # map from user id to user
        self.sent_requests = {}     # map from user id to sent add requests
        self.received_requests = {} # map from user id to received add requests
        self.private_chats = {}     # map from user id to private chat
        self.group_chats = {}       # map from group id to group chat

    def set_status(self, type = None, message = None):
        if type is not None:
            self.status.set_type(type)
        if message is not None:
            self.status.set_message(message)

    def add_to_friends(self, user):
        if user.id not in self.friends:
            self.friends[user.id] = user
            return True
        return False

    def add_to_sent_requests(self, req):
        to_user_id = req.to_user.id
        if to_user_id not in self.sent_requests:
            self.sent_requests[to_user_id] = req
            return True
        return False

    def add_to_received_requests(self, req):
        from_user_id = req.from_user.id
        if from_user_id not in self.received_requests:
            self.received_requests[from_user_id] = req
            return True
        return False

    def remove_request(self, req):
        if req.from_user.id == self.id:
            del self.sent_requests[req.to_user.id]
        else:
            del self.received_requests[req.from_user.id]

    def add_to_private_chats(self, chat):
        other = chat.get_other_participant(self)
        if other.id not in self.private_chats:
            self.private_chats[other.id] = chat

    def add_to_group_chats(self, chat):
        if chat.group_id not in self.group_chats:
            self.group_chats[chat.group_id] = chat

    def send_request(self, user_id):
        UserManager.get_instance().add_user(self, user_id)

    def send_private_message(self, user, content):
        chat = self.private_chats.get(user.id, None)
        if chat is None:
            chat = PrivateChat(self, user)
            self.private_chats[user.id] = chat
        chat.add_message(Message(content, self, user))

    def send_group_message(self, group_id, content):
        chat = self.group_chats.get(group_id, None)
        if chat is not None:
            chat.add_message(Message(content, self))
        return False

class UserManager:
    instance = None

    def __init__(self):
        self.users = {}             # from user id to a user
        self.online_users = {}      # from user id to a user

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = UserManager()
        return cls.instance
    
    def add_user(self, from_user, to_id):
        to_user = self.get_user(to_id)
        request = AddRequest(from_user, to_user)
        from_user.add_to_sent_requests(request)
        to_user.add_to_received_requests(request)

    def get_user(self, id):
        user = self.users.get(id, None)
        if user is None: raise Exception("In valid user")
        return user

    def approve_request(self, req):
        req.status = RequestStatus.Accepted
        req.from_user.add_to_friends(req.to_user)
        req.to_user.add_to_friends(req.from_user)

    def reject_rqeust(self, req):
        req.status = RequestStatus.Rejected
        req.from_user.remove_request(req)
        req.to_user.remove_request(req)

    def user_sign_on(self, id):
        user = self.users.get(id, None)
        if user is not None:
            user.set_status(UserStatusType.Available)
            self.online_users[id] = user

    def user_sign_off(self, id):
        user = self.users.get(id, None)
        if user is not None:
            user.set_status(UserStatusType.Offline)
            del self.online_users[id]

class Conversation:
    def __init__(self):
        self.participants = []
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

class PrivateChat(Conversation):
    def __init__(self, from_user, to_user):
        super().__init__()
        self.participants.append(from_user)
        self.participants.append(to_user)

    def get_other_participant(self, user):
        if self.participants[0] == user:
            return self.participants[1]
        else:
            return self.participants[0]

class GroupChat(Conversation):
    def __init__(self, group_id):
        super().__init__()
        self.group_id = group_id

    def add_participant(self, user):
        self.participants.append(user)

    def remove_participant(self, user):
        self.participants.remove(user)

class Message:
    def __init__(self, content, from_user, to_user = None):
        self.from_user = from_user
        self.to_user = to_user
        self.content = content
        self.date = datetime.now()

class AddRequest:
    def __init__(self, from_user, to_user):
        self.from_user = from_user
        self.to_user = to_user
        self.date = datetime.now()
        self.status = RequestStatus.Unread

class RequestStatus(Enum):
    Unread = 0
    Read = 1
    Accepted = 2
    Rejected = 3

class UserStatus:
    def __init__(self):
        self.type = UserStatusType.Available
        self.message = ''

    def set_type(self, type):
        self.type = type

    def set_message(self, message):
        self.message = message

class UserStatusType(Enum):
    Offline = 0
    Available = 1
    Away = 2
    Busy = 3
    Idle = 4
