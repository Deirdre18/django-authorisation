# all view from django which allows us to implement reset password functionality.

from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# base url, done url, unique url (token generated for each user, create unique p/w - uid created. This is a unque url for reset password), password reset complete url.
urlpatterns = [
    url('^$', password_reset, {'post_reset_redirect': reverse_lazy(
        'password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url('^complete/$', password_reset_complete, name='password_reset_complete')
]
