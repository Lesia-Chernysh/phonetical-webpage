from django.urls import path
from . import views

#app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('allsounds', views.allsounds, name='sounds'),
    path('pictures', views.pictures, name='pictures'),
    path('pronunciation_checker', views.pronunciation_checker, name='pronunciation_checker'),
    path('glossary', views.glossary, name='glossary'),
    path('sound_i', views.sound_i, name='sound_i'),
    path('sound_ɪ', views.sound_y, name='sound_ɪ'),
    path('sound_ɛ', views.sound_e, name='sound_ɛ'),
    path('sound_u', views.sound_u, name='sound_u'),
    path('sound_ɔ', views.sound_o, name='sound_ɔ'),
    path('sound_ɑ', views.sound_a, name='sound_ɑ'),
    path('sound_b_p', views.sound_b_p, name='sound_b_p'),
    path('sound_d_t', views.sound_d_t, name='sound_d_t'),
    path("sound_dj_tj", views.sound_dj_tj, name='sound_dj_tj'),
    path("sound_f", views.sound_f, name='sound_f'),
    path("sound_ʒ_ʃ", views.sound_ʒ_ʃ, name='sound_ʒ_ʃ'),
    path("sound_z_s", views.sound_z_s, name='sound_z_s'),
    path("sound_zj_sj", views.sound_zj_sj, name='sound_zj_sj'),
    path("sound_g_k", views.sound_g_k, name='sound_g_k'),
    path("sound_x", views.sound_x, name='sound_x'),
    path("sound_ɦ", views.sound_ɦ, name='sound_ɦ'),
    path("sound_dz_ts", views.sound_dz_ts, name='sound_dz_ts'),
    path("sound_dʒ_tʃ", views.sound_dʒ_tʃ, name='sound_dʒ_tʃ'),
    path("sound_dzj_tsj", views.sound_dzj_tsj, name='sound_dzj_tsj'),
    path("sound_m", views.sound_m, name='sound_m'),
    path("sound_n", views.sound_n, name='sound_n'),
    path("sound_nj", views.sound_nj, name='sound_nj'),
    path("sound_w", views.sound_w, name='sound_w'),
    path("sound_v", views.sound_v, name='sound_v'),
    path("sound_r", views.sound_r, name='sound_r'),
    path("sound_rj", views.sound_rj, name='sound_rj'),
    path("sound_l", views.sound_l, name='sound_l'),
    path("sound_lj", views.sound_lj, name='sound_lj'),
    path("sound_j", views.sound_j, name='sound_j'),
]
