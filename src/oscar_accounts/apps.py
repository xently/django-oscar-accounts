from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig


class AccountsConfig(OscarConfig):

    name = 'oscar_accounts'
    verbose_name = _('Accounts')
    namespace = 'oscar_accounts'
    # Matches the primary keys of the existing migrations
    default_auto_field = 'django.db.models.AutoField'
