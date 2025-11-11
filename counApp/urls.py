from django.urls import path #(1)
from . import views #(1)

app_name = 'counApp'

urlpatterns = [
    path('', views.home, name="home"), #(1)
    path('aboutme/',views.aboutme, name="aboutme" ), #(2)
    path('childCounselling/',views.childCounselling, name="childCounselling" ), #(3)
    path('coupleCounselling/',views.coupleCounselling, name="coupleCounselling" ), #(4)
    path('groupCounselling/',views.groupCounselling, name="groupCounselling" ), #(5)
    path('narcissm/',views.narcissm, name="narcissm" ), #(6)
    path('selfFree/',views.selfFree, name="selfFree" ), #(7)
    path('breakTrauma/',views.breakTrauma, name="breakTrauma" ), #(8)
    path('detachment/',views.detachment, name="detachment" ), #(9)
    path('parentNarcisst/',views.parentNarcisst, name="parentNarcisst" ), #(10)
    path('gut/',views.gut, name="gut" ), #(11)
    path('anxiety/',views.anxiety, name="anxiety" ), #(12)
    path('toxic/',views.toxic, name="toxic" ), #(13)
    path('selfEsteem/',views.selfEsteem, name="selfEsteem" ), #(14)
    # user details submission block-CODE (15)
    path('', views.home, name='home'),#(15)
    path('submit-contact/', views.submit_contact, name='submit_contact'), #(15)
    #path('submit-contact-ajax/', views.submit_contact_ajax, name='submit_contact_ajax'), #(15)
    path('thanks/', views.contact_thanks, name='contact_thanks'), #(15)
]






