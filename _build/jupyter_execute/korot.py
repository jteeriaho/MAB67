#!/usr/bin/env python
# coding: utf-8

# # Korko  

# ## Mitä tarkoitetaan korolla?

# ```{admonition} Koron määritelmä
# :class: tip
# **Korko** on rahan lainaamisesta lainan antajalle maksettava korvaus.   
# 
# ```

# ### Korkotyypit

# >**Yksinkertainen korko** on harvinaisempi korkotyypeistä. Sitä voidaan käyttää alle vuoden kestävien lainojen yhteydessä, mm. >viivästyskorkojen laskennassa, ja pikavipeissä joiden laina-aika on muutamia kuukausia    
# 
# >**Koronkorko** on yleisin koron laskentatapa, jota käytetään asuntolainoissa, kulutusluotoissa, osamaksukaupoissa, ja >luottokorteissa.  (koronkorkoa käsitellään tarkemmin kurssissa MAB7)

# ### Yksinkertaisen korkolaskun kaavat ja kaavassa käytetyt symbolit

# **i = korkoprosentti** p.a (per annum = vuotta kohden).  Laskuissa des.lukuna: esim. 12% = 0.12        
# 
# **t = laina-aika vuosina** ( esim. 2 kk => t = 2/12 v,   30 pv =>  t = 30/365 v)       
# 
# **k = otettu lainamäärä**, alkupääoma      
# 
# **I = maksettava korko**, joka lasketaan kaavalla $I = k i t$     
# 
# **K = takaisin maksettava summa** = lainasumma + korko:   kaava  $K = k + I = k + k i t = k (1 + i t)$
# 

# ### Esimerkkejä

# ```{admonition} Laske korko ja takaisin maksettava summa 2 kk:n pikalainasta, jonka korkoprosentti on 12 ja lainan määrä 500 euroa.
# :class: dropdown
# Korko = $I = k i t = 500\cdot0.12\frac{2}{12} = 10 $ euroa   
# Maksettava summa = k + I = 500 + 10 = 510 euroa
# ```

# ```{admonition} Matti maksaa 400 euron kiinteistöveron 30 pv myöhässä. Viivästyskorko on 9 %. Verovelvollinen joutuu laskemaan itse maksettavan summan. Mikä se on tässä tapauksessa?
# :class: dropdown
# Viivästysorko = $I = k i t = 400\cdot0.09\frac{30}{365} = 2.96 $ euroa   
# Maksettava summa $K = k + I = 400 + 2.96 = 402.96 $ euroa
# ```

# ### Nykyarvon laskeminen eli diskonttaus

# Esim. panttilainaamoissa korko voidaan periä jo lainan antohetkellä etukäteen. Asiakas saa siten käteen lainasummaa pienemmän rahamäärän, joka on takaisin maksettavan lainasumman nykyarvo lainanantohetkellä. 
# 
# >Nykyarvo lasketaan ratkaisemalla k  kaavasta K = k (1 + i t) , jolloin saadaan        
# 
# >Nykyarvo $k =\frac{K}{1+i t}$ 

# ```{admonition} Seija ottaa panttilainaamosta erästä maisemataulua vastaan 1000 euron lainan, jonka laina-aika on 3 kk ja korko 12 %.  Korko peritään laina-ajan alussa ja takaisin maksettava summa on tasan 1000 euroa 3kk kuluttua.
# :class: dropdown
# Seijan käteen saama summa $k = \frac {K}{1+it}=\frac {1000}{1+0.12\frac{3}{12}} = 970.87$€       
# (etukäteen peritty korko on siten n. 29 euroa) 
# 
# Vastaus: 970.87$
# ```

# ### Kaavassa esiintyvän ajan t muuntaminen vuosiksi vaihtelee eri maissa

# **Suomi, pohjoismaat, Englanti:**   $t = \frac{kalenteripäivät}{365} $      
# 
# **Saksa, Ranska:**   $t = \frac{kalenteripäivät}{360} $     
# 
# **Sveitsi:**   $t = \frac{pv}{360} $, missä päiviä pv laskettaessa oletetaan, että jokaisessa kuussa on 30 päivää   

# Esim. jos 1000 euron laina 12% korolla otetaan 1.2.2023 ja maksupäivä on 1.5.2023, niin 
# >Suomessa korko olisi 1000*0.12*89/365 = 29.26 euroa,      
# >Ranskassa korko olisi 1000*0.12*89/360 = 29.67 euroa     
# >Sveitsissä 1000*0.12*90/360 = 30 euroa.
