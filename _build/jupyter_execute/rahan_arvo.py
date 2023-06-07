#!/usr/bin/env python
# coding: utf-8

# # Rahan arvo

# ## Prosentin määritelmä

# ```{admonition} Prosentin määritelmä
# :class: tip
# Prosentti tarkoittaa sadasosaa. Se voidaan esittää myös murtolukuna ja desimaalilukuna.   
# 
# 1% = $\frac {1}{100} = 0.01$ 
# ```

# ### Prosenttiosuuden laskeminen:  Montako prosenttia a on b:stä?

# Lukua a sanotaan usein *vertailuarvoksi* ja lukua b *perusarvoksi.*      
# 
# Ratkaisu:  $p =\frac {a}{b}\cdot 100\%$ 

# ```{admonition} Poliisi puhallutti 240 autoilijaa, joilla 7:llä oli alkoholia veressä. Monellako prosentilla puhallutetuista oli alkoholia veressä? 
# :class: dropdown
# $p =\frac {7}{240}\cdot 100\% = 2.9\%$   
# 
# Vastaus: 2.9 prosentilla oli alkoholia veressä
# ```

# ### Paljonko on p prosenttia a:sta?  

# Ratkaisu:  $\frac {p}{100}\cdot a$ 

# ```{admonition} Puseron hinta oli 39.80.  Myyjä antoi siitä 35% alennuksen. Mikä oli alennettu hinta?
# :class: dropdown
# Alennus oli $\frac {35}{100}\cdot 39.80 = 13.93$      
# Alennettu hinta on siten 39.80 -13.93 = 25.87.
# ```

# ### Montako prosenttia a on suurempi kuin b? 

# Tässä vertailuarvona on lukujen erotus ja perusarvona luku b. Ratkaisu: $\frac {a-b}{b}\cdot100\%$

# ```{admonition} Ruotsalaisten keskipalkka on 3680 Eur/kk ja suomalaisten 3570 Eur/kk. Kuinka monta prosenttia ruotsalaisten keskipalkka on suurempi kuin suomalaisten?
# :class: dropdown
# $\frac {3680-3570}{3570}\cdot100\% = 3.1\%$   
# 
# Vastaus:  3.1%
# ```

# ### Montako prosenttia a on pienempi kuin b?

# Vertailuarvona on lukujen erotus ja perusarvona luku b. Ratkaisu: $\frac {b-a}{b}\cdot100\%$

# ```{admonition} Prismassa Valion arkijuusto maksaa 5.95, kun sen hinta K-marketissa on 6.35. Kuinka monta prosenttia vähemmän juusto maksaa Prismassa verrattuna K-marketiin?
# :class: dropdown
# $\frac {6.35-5.95}{6.35}\cdot100\% = 6.3\%$    
# 
# Vastaus:  6.3%
# ```

# ### Perusarvon laskeminen

# Yhtälöstä $\frac {a}{b}=\frac {p}{100}$ ratkaistuna     
# 
# perusarvo $b=\frac {a}{p/100}=\frac{a}{p}\cdot 100$

# ```{admonition} Maijalle kevään 2.5% palkankorotus toi lisää palkkaa 45 Euroa kk:ssa. Mikä oli Maijan kuukausipalkka ennen korotusta?
# :class: dropdown
# $\frac {45}{x} = \frac{2.5}{100} => x = \frac{45}{2.5}\cdot100 = 1800 $   
# 
# Vastaus:  1800 Euroa
# ```

# ## Perättäiset prosenttikorotukset, lisäyskerroin

# Esim. Jos 2500 euron palkkaa korotetaan 3.5 prosenttia, on kätevintä laskea uusi palkka käyttämällä ns. **lisäyskerrointa**  1.035.   
# 
# Uusi palkka on $1.035\cdot2500$ = 2587.50. 

# ```{admonition} Lisäyskerroin
# :class: tip
# Lisäyskerroin eli korkotekijä   
# 
# r = $1 + \frac {p}{100}$ 
# ```

# ```{admonition} Maijan palkkaa korotettiin sopimuskaudella kolme kertaa. Korotukset olivat 3.0%, 2.5% ja 1.5%. Kuinka paljon Maijan palkka nousi yhteensä sopimuskaudella?
# :class: dropdown
# Koko sopimuskauden lisäyskerroin on korotuksia vastaavien lisäyskertoimien tulo. 
# $1.03\cdot1.025\cdot1.015 = 1.0716$  
# Tämä vastaan n. 7.2% palkankorotusta   
# 
# Vastaus:  7.2%
# ```

# ```{admonition} Kiinteistön arvo v.2010 oli 125000 euroa. Mikä oli kiinteistön arvo v.2018, jos oletetaan että arvo nousi tuolla aikavälillä 2.5% vuodessa? 
# :class: dropdown
# Vuotuinen lisäyskerroin on 1.025. Arvo 8 vuotta vertailuvuoden 2010 jälkeen on    
# 
# $125000\cdot1.025^8 = 152300$   
# 
# Vastaus:  152300 euroa
# ```
