from collections import OrderedDict
from .models import Comment, Message

class MessageList(object):
    @staticmethod
    def build_tree(records):
        tree = []
        for record in records:
            record.children = []
            if record.parent_id is None:
                tree.append(record)
            else:
                try:
                    parent = [p for p in records if p.id == record.parent_id][0]
                    parent.children.append(record)
                except ValueError:
                    tree.append(record)
        return tree

    @staticmethod
    def get_list():
        result = OrderedDict()
        messages = Message.objects.all()
        messages_ids = messages.values_list('id', flat=True)
        comment_replies = Comment.objects.filter(message_id__in=messages_ids)
        comment_tree = MessageList.build_tree(comment_replies)

        for mes in messages:
            result[mes] = [comment for comment in comment_tree if comment.message_id == mes.id]

        return result
