from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from material.frontend.apps import ModuleMixin


class Admin_dashboardConfig(ModuleMixin, AppConfig):
    name = 'Admin Dashboard'
    icon = '<i class="material-icons">verified_user</i>'
    verbose_name = _('Dashboard')

    def has_perm(self, user):
        return user.is_superuser