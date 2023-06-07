#!/usr/bin/env python
# coding: utf-8

# # Tuloperiaate   

#        
# Tilasto-oppiin läheisesti liittyvä käsite on **todennäköisyys**.     
# 
# Monet tilastomuuttujat, kuten esim. ihmisen pituus tai elinaika, tai vaikkapa metsikön puiden läpimitta, noudattavat jakaumaa, jota voidaan kuvata jollakin tunnetulla todennäköisyysjakaumalla. Yleisesti käytettyjä jakaumia ovat mm.  Gaussin normaalijakauma ja Weibull-jakauma. Todennäköisyysjakaumien käyttö tilastomuuttujan mallinnuksessa säästää tiedonkeruuta. Kun dataa on riittävästi mallin parametrien laskemiseen, voidaan siirtyä datan keruusta matemaattisen mallin avulla suoritettavaan laskentaan.  
# 

# ## Todennäköisyyden määritelmä

# Todennäköisyys jaetaan usein kahteen tyyppiin: **klassinen todennäköisyys** ja **tilastollinen todennäköisyys** . Klassista todennäköisyyttä tarvitaan esim. kun lasketaan korttipelien erilaisten käsien todennäköisyyksiä tai nopanheiton tuloksia.  Tilastollista eli empiiristä todennäköisyyttä voi hyödyntää esim. vakioveikkauksessa tai vakuutusten hinnoittelussa.

# ```{admonition} **Klassinen todennäköisyys**
# :class: tip
# Nimitykset:     
# E = **tapahtuma-avaruus** eli *otosavaruus* , joka koostuu alkeistapauksista joiden tiedetään olevan yhtä todennäköisiä     
# A = **tapahtuma**, joka on E:n osajoukko, jonka todennäköisyys halutaan laskea
# 
# Tapahtuman A todennäköisyys P(A) määritellään seuraavasti:      
# 
# $P(A)=\frac {k}{n}$       
# 
# missä n = kaikkien mahdollisten alkeistapausten lukumäärä ja k = tapahtuman A kannalta suotuisten alkeistapausten lukumäärä
# 
# ```

# ```{admonition} Laatikossa on 8 palloa, joista 4 punaista, 3 sinistä ja 1 keltainen. Laatikosta otetaan umpimähkään 1 pallo. Millä todennäköisyydellä se on sininen?
# :class: dropdown
# Ratkaisu P(sininen)=$\frac {3}{8}$        
# *(8 yhtä todennäköisestä alkeistapauksesta 3 on "suotuisaa" eli antaa sinisen pallon)*
# 
# ```
