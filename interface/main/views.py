from django.shortcuts import render
from .models import InformationAboutVowels
from .models import InformationAboutConsonants


# Create your views here.
def home(request):
    return render(request, 'main/home_page.html')


def allsounds(request):
    return render(request, 'main/allsounds.html')


def pictures(request):
    information = InformationAboutVowels.objects.filter(row__contains='передній').order_by('id')
    information2 = InformationAboutVowels.objects.filter(row__contains='задній').order_by('id')
    information3 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='білабіальний').order_by('id')
    information4 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='лабіодентальний').order_by('id')
    information5 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='альвеолярний',
                                                             way_of_articulation__contains='проривний').order_by('id')
    information6 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='альвеолярний',
                                                             way_of_articulation__contains='щілинний').order_by('id')
    information7 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='альвеолярний',
                                                             way_of_articulation__contains='африката',
                                                             palatalization__contains="твердий").order_by('id')
    information14 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='альвеолярний',
                                                             way_of_articulation__contains='африката',
                                                              palatalization__contains="м'який").order_by('id')

    information8 = InformationAboutConsonants.objects.filter(way_of_articulation__contains='апроксимальний').order_by('id')
    information9 = InformationAboutConsonants.objects.filter(way_of_articulation__contains='вібрант').order_by('id')
    information10 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='постальвеолярний').order_by('id')
    information11 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='середньоязиковий').order_by('id')
    information12 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='задньоязиковий').order_by('id')
    information13 = InformationAboutConsonants.objects.filter(place_of_articulation__contains='глотковий').order_by('id')
    return render(request, 'main/pictures.html', {'information': information,'information2':information2,
        'information3':information3, 'information4':information4, 'information5':information5,
        'information6': information6, 'information7': information7,
        'information8': information8, 'information9': information9,
        'information10': information10, 'information11': information11, 'information12': information12,
        'information13': information13, 'information14': information14})


def pronunciation_checker(request):
    return render(request, 'main/pronunciation_checker.html')


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