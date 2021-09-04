from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import sendNotice, viewNotice, setNoticeTimestamp, endpoints
=======
from .views import CreateNoticeView, CommentReactionAPIView,EditNoticeAPIView, AllNoticesView, deleteNotice, CommentDeleteAPIView
>>>>>>> 1c87e21052b32b6e35cb259d46014e491b3017ee
=======
from .views import sendNotice, viewNotice, setNoticeTimestamp, endpoints
>>>>>>> defb555c88fec7a1172f60e1741523887618becd

#add url routes here

urlpatterns = [

    path("sendNotice/", sendNotice, name="send-notice"),

    path("viewNotice/", viewNotice, name="view-notice"),

<<<<<<< HEAD
<<<<<<< HEAD
    path("setNoticeTimestamp/", setNoticeTimestamp, name="set-notice"),
    
    path("endpoints/", endpoints, name="endpoints"),
    
]
=======
    path('comment/reaction/update', CommentReactionAPIView.as_view()),

    path('notice/update', EditNoticeAPIView.as_view()),
    
    path('delete-notice', deleteNotice, name='delete-notice'),

    path('comment/delete', CommentDeleteAPIView.as_view()),
]
>>>>>>> 1c87e21052b32b6e35cb259d46014e491b3017ee
=======
    path("setNoticeTimestamp/", setNoticeTimestamp, name="set-notice"),
    
    path("endpoints/", endpoints, name="endpoints"),
    
]
>>>>>>> defb555c88fec7a1172f60e1741523887618becd
