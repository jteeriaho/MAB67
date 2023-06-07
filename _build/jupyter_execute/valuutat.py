#!/usr/bin/env python
# coding: utf-8

# # Valuutat

# ## Valuuttakurssit

# ```{admonition} Mikä on valuuttakurssi
# :class: tip
# Valuuttakurssi kertoo 1 Euron arvon ulkomaan valuutassa: 1 Euro = X Muu_Valuutta
# Suomi on Euromaa, joten Euroopan keskuspankki määrittää päivittäin ns. **keskikurssit**
# >Pankin laskevat keskikurssista **myyntikurssin** ja **ostokurssin**, jolla ne myyvät ja ostavat muita valuuttoja. 
# >Ero keskikurssiin johtuu pankin haluamasta valuutanvaihtoon liittyvästä marginaalista.   
# >Sähköiselle "tilivaluutalle" marginaali on pienempi kuin käteiselle rahalle.
# ```

# ### Esim. Nordean valuuttakursseista

# ![nordea](images/valuutat.png)

# ### Ulkomaan valuutan vaihto euroiksi / esimerkkejä

# ```{admonition} Muunnos euroiksi kun pankki myy ulkomaan rahaa
# :class: tip
# euromäärä = ulkomaan valuutan määrä / myyntikurssi
# ```

# ```{admonition} Maksat Nordean kautta 400 SEK:n laskun Ruotsiin. Paljonko maksat euroina?
# :class: dropdown
# Nordea siis myy sinulla 400 Ruotsin kruunua, jonka myyntikurssi on 11.358 (ts. 1 € = 11.358 SEK)
# Euroiksi muutettuna summa on **400/11.358 = 32.22 euroa** 
# 
# ```

# Jos on epävarma, pitääkö jakaa vai kertoa kurssilla, voi ajatella ratkaisua myös verrannon avulla:
# 
#  1 euro  = 11.358 SEK 
#  x euroa = 400 SEK    
# 
# Tästä saadaan verranto $\frac {x}{1} = \frac {400}{11.358}$

# ```{admonition} Muunnos euroiksi kun pankki ostaa ulkomaan rahaa
# :class: tip
# euromäärä = ulkomaan valuutan määrä /ostokurssi
# ```

# ```{admonition} Sinulle on jäänyt Lontoon matkalta ylimääräiset 150 GBP (puntaa), jonka haluat vaihtaa Helsingin lentoasemalla Euroiksi. Paljonko saat (olettaen, että käytetään Nordean taulukkoa, eikä vaihdosta menisi toimitusmaksua) 
# :class: dropdown
# Pankki ostaa sinulta 150 GBP, ostokurssin ollessa 0.8748  (ts. 1 € = 0.8748 GBP)
# Euroiksi muutettuna summa on 150/0.8748 = 171.48 euroa.
# 
# ```

# ### Määrätyn euromäärän vaihtaminen ulkomaan valuutaksi

# **Tässä tapauksessa euromäärä kerrotaan ulkomaan valuutan kurssilla**

# ```{admonition} Vaihdat laivalla 200 euroa Ruotsin kruunuiksi. Montako kruunua saat?
# :class: dropdown
# Oletaan, että kurssit on ilmoitettu vaihtopisteessä kuten Suomessa (muoto 1 euro = X SEK)
# Saamasi määrä kruunuja on  200*11.358 = 2271.60 SEK
# ```

# ### Pankkikortilla maksu ja pankkiautomaatit ulkomailla

# Pankkikortit käyvät maksuvälineenä ulkomailla. Käteistä voi nostaa automaateista.
# Valuutan vaihto toimistoista ei ole kannattavaa kortin käyttöön verrattuna
