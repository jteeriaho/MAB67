#!/usr/bin/env python
# coding: utf-8

# # 1. asteen yhtälöt ja epäyhtälöt

# ## 1. asteen yhtälöt  
# 
# ### Ongelmia, jotka voidaan ratkaista 1. asteen yhtälön avulla 

# ````{admonition} Esim. 1: Eräällä kokonaisluvulla on ominaisuus, että kun lukuun lisätään 10, luku kolminkertaistuu. Esitä ongelma yhtälönä ja ratkaise yhtälö.  
# :class: dropdown, tip
# Yhtälö: x + 10 = 3x
# ```{admonition} Yhtälön ratkaisu: 
# :class: dropdown
# $ x + 10 = 3x$  
# $ 10 = 3x - x$   
# $ 10 = 2x$   
# $ x = 10/5 = 2$
# ```
# ````

# ````{admonition} Kaukolämmön kuukausilasku koostuu 55 euron perusmaksusta +  kulutukseen perustuvasta energiamaksusta, joka on 50 eur/MWh. Erään perheen maaliskuun lasku oli 185 euroa. Kuinka monta MWh energiaa perhe kulutti maaliskuussa?  
# :class: dropdown, tip
# Vastaus: 2.6 MWh
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ 55 + 50 x = 185$    
# $ 50 x = 185-55 = 130$   
# $ x = 130/50 = 2.6$
# ```
# ````

# ```{admonition} Ensimmäisen asteen yhtälön ratkaiseminen
# :class: tip
# 
# Yhtälö viedään **perusmuotoon** $a x = b$, jonka ratkaisu $x = \frac {b}{a}$
# 
# Perusmuotoon pääsemiseksi tarvitaan mm. seuraavia välivaiheita:    
# 
# 1. Mikäli yhtälössä on sulkulausekkeita, poistetaan sulut käyttäen polynomien laskusääntöjä.
# 2. Siirretään termejä siten, että ratkaistavan muuttujan sisältävät termit ja muut termit (vakiot) erotellaan eri puolille yhtälöä. Tämän jälkeen muuttujan kertoimet yhdistetään, samoin toisen puolen vakiot.   
# > Sääntö: Kun termi siirretään yhtälön puolelta toiselle, sen etumerkki vaihtuu.
# ```

# ### 1. asteen yhtälötyyppejä

# ````{admonition} Yksinkertainen perustapaus: $ 3 x + 2 = 5 x - 1 $
# :class: dropdown, tip
# Vastaus: x = 3/2
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ 3x - 5x = -2 - 1$   
# $ -2x = -3$   
# $ x = -3/-2 = 3/2$
# ```
# ````

# ````{admonition} Yhtälö, jossa on sulkuja: $ 2(3x+1)- 4(x+2) =0 $   
# :class: dropdown, tip
# Vastaus: x = 8
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ 6x + 2 -4x - 8 =0\hspace{2mm}$   (sulut poistettu)   
# $ 6x-4x = 8-2\hspace{10mm}$        (muuttujat ja vakiot eri puolille)  
# $ 2x = 6\hspace{27mm}$             (yhtälö viety perusmuotoon)   
# $ x = 3$
# ```
# ````

# ````{admonition} Kertoimet muita kuin rationaalilukuja: $\sqrt{2}x+4=5-\sqrt{3}x $   
# :class: dropdown, tip
# Vastaus: $x = \frac {1}{\sqrt{2}+\sqrt{3}}$
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ \sqrt{2}x +\sqrt{3}x =5 -4$      
# $ (\sqrt{2} +\sqrt{3})x =1$      
# $ x = \frac {1}{\sqrt{2}+\sqrt{3}}$
# ```
# ````

# ````{admonition} Kertoimet parametreja: $ a x + 1 = b - 5x $   
# :class: dropdown, tip
# Vastaus: $x = \frac {b-1}{a+5} ,\hspace{4mm} a \neq -5$
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ a x + 5 x = b - 1\hspace{15mm}$     muuttujat ja vakiot eroteltu   
# 
# $ (a + 5)x =b - 1\hspace{15mm}$       muuttujan x kertoimet yhdistetty   
# 
# $ x = \frac {b-1}{a+5}\hspace{30mm}$   yhtälö jaettu x:n kertoimella   
# 
# Saatu ratkaisu on mahdollinen vain jos $a \neq -5$. (nimittäjä a+5 ei saa olla 0)  
# (Jos a = -5, yhtälöstä tulee 1 = b, joka on joko identtisesti tosi tai epätosi riippuen b:n arvosta)
# ```
# ````

# ````{admonition} Suureyhtälö: Ratkaise t yhtälöstä $ v = v_{0} + a t $   
# :class: dropdown, tip
# Vastaus: $t = \frac {v-v_{0}}{a}$ 
# ```{admonition} Ratkaisu: 
# :class: dropdown
# $ v - v_{0} = a\cdot t \hspace{15mm}$     muuttujan t sisältävä termi yksin oikealla puolen      
# 
# $ t = \frac {v-v_{0}}{a}\hspace{24mm}$    yhtälö jaettu t:n kertoimella   
# 
# ```
# ````

# ````{admonition} Yhtälössä kokonaislukunimittäjiä $ \frac {2x+1}{3}+x= \frac {x-1}{2}$   
# :class: dropdown, tip
# Vastaus: $x = -\frac {5}{7}$ 
# ```{admonition} Ratkaisu: 
# :class: dropdown
# Kerrotaan yhtälön kaikki termit nimittäjien pienimmällä yhteisellä jaettavalla, luvulla 6    
# $ 6\frac {2x+1}{3}+6x= 6\frac {x-1}{2}$    
# Nimittäjät supistuvat pois, yhtälöön jää vielä poistettavia sulkulausekkeita    
# $2(2x+1)+6x=3(x-1)$   
# $4x+2+6x=3x - 3$    
# $4x+6x-3x=-2 - 3$   
# $7x= -5$    
# $x= -5/7$
# 
# ```
# ````
