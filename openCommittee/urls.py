from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from committeeVotes import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openCommittee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', views.index, name='index'),
    url(r'^bills/$', views.bills, name='bills'),
    url(r'^bills/(?P<bill_id>\d+)/$', views.bill, name='bill'),

    url(r'^minister/$', views.ministers, name='ministers'),
    url(r'^minister/(?P<minister_id>\d+)/$', views.minister_details, name='minister'),

    url(r'meetings/$',views.meetings, name='meetings'),
    url(r'^meetings/(?P<meeting_id>\d+)/$', views.meeting_details, name='meeting'),

    url(r'about/$',views.about, name='about'),

    url(r'^search.json', views.search, name='search'),
    url(r'^bills.json', views.searchBills, name='searchBills'),
    url(r'^ministers.json', views.searchMinisters, name='searchMinisters'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
