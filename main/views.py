from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

from .models import InformationAboutVowels
from .models import InformationAboutConsonants
from .models import Exercises


# Create your views here.
def home(request):
    trans = translate(language='en')
    return render(request, 'main/home_page.html', {'trans': trans})


def translate(language):
    current_lang = get_language()
    try:
        activate(language)
        text = gettext('привіт')
    finally:
        activate(current_lang)
    return text


def allsounds(request):
    return render(request, 'main/allsounds.html')


def glossary(request):
    return render(request, 'main/glossary.html')


def pictures(request):
    information = InformationAboutVowels.objects.filter(row__contains='передній').order_by('id')
    information_i = InformationAboutVowels.objects.filter(sound__contains='і')
    information_y = InformationAboutVowels.objects.filter(sound__contains='ɪ')
    information2 = InformationAboutVowels.objects.filter(row__contains='задній').order_by('id')
    information_p = InformationAboutConsonants.objects.filter(sound__contains='p')
    information_f = InformationAboutConsonants.objects.filter(sound__contains='f')
    information_d = InformationAboutConsonants.objects.filter(sound__contains='d',
                                                              place_of_articulation__contains='альвеолярний',
                                                              way_of_articulation__contains='проривний').order_by('id')

    information_t = InformationAboutConsonants.objects.filter(sound__contains='t',
                                                              place_of_articulation__contains='альвеолярний',
                                                              way_of_articulation__contains='проривний').order_by('id')

    information_dz = InformationAboutConsonants.objects.filter(sound__contains='dz',
                                                             place_of_articulation__contains='альвеолярний',
                                                             way_of_articulation__contains='африката').order_by('id')
    information_ts = InformationAboutConsonants.objects.filter(sound__contains='ts',
                                                               place_of_articulation__contains='альвеолярний',
                                                               way_of_articulation__contains='африката').order_by('id')

    information_l = InformationAboutConsonants.objects.filter(sound__contains='l').order_by('id')
    information_r = InformationAboutConsonants.objects.filter(sound__contains='r').order_by('id')
    information_g = InformationAboutConsonants.objects.filter(sound__contains='g')
    information_x = InformationAboutConsonants.objects.filter(sound__contains='x')
    information_ɦ = InformationAboutConsonants.objects.filter(sound__contains='ɦ')
    return render(request, 'main/pictures.html', {'information': information, 'information_i': information_i,
        'information_y': information_y, 'information2':information2,
        'information_p':information_p, 'information_f':information_f, 'information_d':information_d,
        'information_t': information_t, 'information_dz': information_dz, 'information_ts': information_ts,
        'information_l': information_l, 'information_r': information_r,
        'information_g': information_g, 'information_x': information_x, 'information_ɦ': information_ɦ})


def pronunciation_checker(request):
    information = Exercises.objects.order_by('id')
    return render(request, 'main/pronunciation_checker.html', {'information': information})


def sound_i(request):
    information = InformationAboutVowels.objects.filter(sound__contains='і')
    return render(request, 'main/sound_i.html', {'information': information})


def sound_y(request):
    information = InformationAboutVowels.objects.filter(sound__contains='ɪ')
    return render(request, 'main/sound_y.html', {'information': information})


def sound_e(request):
    information = InformationAboutVowels.objects.filter(sound__contains='ɛ')
    return render(request, 'main/sound_e.html', {'information': information})


def sound_u(request):
    information = InformationAboutVowels.objects.filter(sound__contains='u')
    return render(request, 'main/sound_u.html', {'information': information})


def sound_o(request):
    information = InformationAboutVowels.objects.filter(sound__contains='ɔ')
    return render(request, 'main/sound_o.html', {'information': information})


def sound_a(request):
    information = InformationAboutVowels.objects.filter(sound__contains='ɑ')
    return render(request, 'main/sound_a.html', {'information': information})


def sound_b_p(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='b')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='p')
    return render(request, 'main/sound_b_p.html', {'information': information, 'information2': information2})


def sound_d_t(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='d̪')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='t̪')
    return render(request, 'main/sound_d_t.html', {'information': information, 'information2': information2})


def sound_dj_tj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='dʲ')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='tʲ')
    return render(request, 'main/sound_dj_tj.html', {'information': information, 'information2': information2})


def sound_f(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='f')
    return render(request, 'main/sound_f.html', {'information': information})


def sound_ʒ_ʃ(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[ʒ]')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='[ʃ]')
    return render(request, 'main/sound_zh_sh.html', {'information': information, 'information2': information2})


def sound_z_s(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[z]')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='[s]')
    return render(request, 'main/sound_z_s.html', {'information': information, 'information2': information2})


def sound_zj_sj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[zʲ]')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='[sʲ]')
    return render(request, 'main/sound_zj_sj.html', {'information': information, 'information2': information2})


def sound_g_k(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='g')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='k')
    return render(request, 'main/sound_g_k.html', {'information': information, 'information2': information2})


def sound_x(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='x')
    return render(request, 'main/sound_x.html', {'information': information})

def sound_ɦ(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='ɦ')
    return render(request, 'main/sound_h.html', {'information': information})

def sound_dz_ts(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[dz]')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='[ts]')
    return render(request, 'main/sound_dz_ts.html', {'information': information, 'information2': information2})


def sound_dʒ_tʃ(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='dʒ')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='tʃ')
    return render(request, 'main/sound_dzh_tsh.html', {'information': information, 'information2': information2})

def sound_dzj_tsj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='dzʲ')
    information2 = InformationAboutConsonants.objects.filter(sound__contains='tsʲ')
    return render(request, 'main/sound_dzj_tsj.html', {'information': information, 'information2': information2})


def sound_m(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='m')
    return render(request, 'main/sound_m.html', {'information': information})


def sound_n(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='n̪')
    return render(request, 'main/sound_n.html', {'information': information})


def sound_nj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='nʲ')
    return render(request, 'main/sound_nj.html', {'information': information})


def sound_w(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='w')
    return render(request, 'main/sound_w.html', {'information': information})


def sound_v(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='v')
    return render(request, 'main/sound_v.html', {'information': information})


def sound_r(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[r]')
    return render(request, 'main/sound_r.html', {'information': information})


def sound_rj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='rʲ')
    return render(request, 'main/sound_rj.html', {'information': information})


def sound_l(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[l]')
    return render(request, 'main/sound_l.html', {'information': information})


def sound_lj(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='lʲ')
    return render(request, 'main/sound_lj.html', {'information': information})


def sound_j(request):
    information = InformationAboutConsonants.objects.filter(sound__contains='[j]')
    return render(request, 'main/sound_j.html', {'information': information})