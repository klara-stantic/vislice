import model

def izpis_igre(igra):
    tekst = (
        '''Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n
        Pravilni ugibi: {pravilni_del_gesla} \n\n
        Neuspeli poskusi: {neuspeli_poskusi} '''
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        "Wii, zmaga! Geslo je bilo: {geslo}"
    ).format(
        geslo = igra.geslo()
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        "Poraz! Geslo je bilo: {geslo}"
    ).format(
        geslo = igra.geslo()
    )
    return tekst

def izpis_napake(igra):
    tekst = "Pazi, ugibaš lahko samo eno črko na enkrat!"
    return tekst

def zahtevaj_vnos():
    return input('črka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        #najprej izpišemo stanje, da vidimo, koliko črk je ipd.#
        print(izpis_igre(igra))
        #čakamo na črko od uporabnika#
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake(igra))
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            break
    return 

pozeni_vmesnik()