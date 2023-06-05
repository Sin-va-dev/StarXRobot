import threading

from sqlalchemy import Column, String, UnicodeText

from StarRobot.modules.sql import BASE, SESSION




def blacklist_user(user_id, reason=None):
    with BLACKLIST_LOCK:
        user = SESSION.query(BlacklistUsers).get(str(user_id))
        if not user:
            user = BlacklistUsers(str(user_id), reason)
        else:
            user.reason = reason

        SESSION.add(user)
        SESSION.commit()
        __load_blacklist_userid_list()


def unblacklist_user(user_id):
    with BLACKLIST_LOCK:
        user = SESSION.query(BlacklistUsers).get(str(user_id))
        if user:
            SESSION.delete(user)

        SESSION.commit()
        __load_blacklist_userid_list()


def get_reason(user_id):
    user = SESSION.query(BlacklistUsers).get(str(user_id))
    rep = ""
    if user:
        rep = user.reason

    SESSION.close()
    return rep


def is_user_blacklisted(user_id):
    return user_id in BLACKLIST_USERS


def __load_blacklist_userid_list():
    global BLACKLIST_USERS
  
    finally:
        SESSION.close()


__load_blacklist_userid_list()
