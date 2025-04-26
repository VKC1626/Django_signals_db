By default, Django signals like post_save run after the database transaction in memory, but not necessarily after the transaction is fully committed to the database.

If you trigger a post_save signal, it runs right after .save() is called.

But if you have an explicit database transaction (@transaction.atomic), and then an error happens later inside that transaction, the signal would have already run even though the database changes get rolled back.

when we run this command in shell

"from blog.models import Post
from django.db import transaction

try:
    with transaction.atomic():
        post = Post.objects.create(title="My New Post")
        print("Post created inside atomic block")
        raise Exception("Something bad happened!")
except Exception as e:
    print("Caught exception:", e)
"

the expected output should be like ::

"Post created inside atomic block
Signal received inside post_saved_handler
Connection in transaction? True
Caught exception: Something bad happened!
"

This means:

Signal fired even though the transaction was not yet committed.

Signal ran during the transaction, before any rollback.

This is dangerous sometimes because the signal might perform actions (like sending an email or updating another table) even if the transaction finally fails.
