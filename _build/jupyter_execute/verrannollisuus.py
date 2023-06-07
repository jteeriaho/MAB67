#!/usr/bin/env python
# coding: utf-8

# # Verrannollisuus

# ## Verranto

# ```{admonition} Määritelmä    
# :class: tip
# Verranto on yhtälö, jossa kaksi suureen suhdetta on merkitty yhtäsuuriksi.   
# 
# $\frac{A}{B}=\frac{C}{D}$   
# 
# Lukuja A ja D sanotaan verrannon **äärimmäisiksi jäseniksi** ja   
# lukua B ja C verrannon **keskimmäisiksi jäseniksi**
# ```

# Mikä tahansa suureista A,B,C tai D voidaan ratkaista verrannosta, kun kolme muuta jäsentä tunnetaan.    
# Yleisesti käytetty menettely on ns **"ristiin kertominen"**

# ```{admonition} Ristiin kertominen
# :class: tip
# Verrannon $\frac{A}{B}=\frac{C}{D}$ äärimmäisten jäsenten tulo = keskimmäisten jäsenten tulo. Ts.     
# 
# $A\cdot D =B\cdot C$
# ```

# ````{admonition} Esimerkki
# :class: note 
# Ratkaise x verrannosta $\frac{24}{40}=\frac{x}{60}$
# 
# ```{admonition} Ratkaisu
# :class: dropdown
# Ristiin kertomalla saadaan $24\cdot 60 =40\cdot x$  , josta ratkaistuna   
# $x =\frac{24\cdot60}{40} = 36 $
# ```
# ````

# ````{admonition} Esimerkki
# :class: note 
# Ratkaise x verrannosta $\frac{5}{x}=\frac{12}{8}$
# 
# ```{admonition} Ratkaisu
# :class: dropdown
# Ristiin kertomalla saadaan $5\cdot 8 =x\cdot 12$  , josta ratkaistuna   
# $x =\frac{5\cdot8}{12} = \frac{40}{8}\approx 3.33 $
# ```
# ````

# ## Verrannollisuus ja sen lajeja

# Verrantoa ja sen ratkaisutekniikkoja voidaan hyödyntää käytännön ongelmien ratkaisuissa silloin, kun tarkasteltavien suureiden välillä on jonkin tyyppinen verrannollisuus. Seuraavassa on muutamia verrannollisuustyyppejä.

# ```{admonition} Suoraan verrannollisuus  
# :class: tip
# Suureet x ja y ovat **suoraan verrannolliset** , jos   
# 
# $y = k\cdot x$ , missä k on jokin vakiokerroin. 
# 
# Tällöin on voimassa verranto   
# 
# 
# $\frac{x_1}{x_2}=\frac{y_1}{y_2}$ 
# ```

# ````{admonition} Esimerkki
# :class: note 
# Talon 3.0 m² seinän maalaamiseen kului 0.25 ltr maalia. Kuinka paljon maalia kuluu olohuoneen maalaamiseen, kun olohuoneen seinäpinta-ala on 32 m².
# 
# ```{admonition} Ratkaisu
# :class: dropdown
# On ilmeistä, että maalin kulutus on suoraan verrannollnen maalattavaan pinta-alaan. Jos merkitään x:llä kysyttyä maalinkulutusta, saadaan verranto   
# $\frac{\text{32 }m^2}{\text{3.0 } m^{2}}=\frac{x}{\text{0.25 ltr}}$, josta laskettuna  
# $x = 32/3.0*0.25 ltr = 2.7 ltr$
# 
# ```
# ````

# ```{admonition} Kääntäen verrannollisuus  
# :class: tip
# Suureet x ja y ovat **kääntäen verrannolliset** , jos   
# 
# $y = \frac{k}{x} $ , missä k on vakio. 
# 
# Kääntäen verrannollisuus voidaan esittää myös niin, että suureiden tulo x y = vakio     
# $x\cdot y= k$
# 
# Verrantomuodossa sama asia voidaan ilmaista seuraavasti    
# 
# $\frac{x_1}{x_2}=\frac{y_2}{y_1}$ 
# ```

# ````{admonition} Esimerkki
# :class: note 
# Mika ajaa töihin 20 minuutissa, kun keskinopeus työmatkalla on 80 km/h.  Kuinka kauan työmatkaan menee, kun keskinopeus on 65 km/h
# 
# ```{admonition} Ratkaisu
# :class: dropdown
# Työmatkaan kuluvan ajan ja nopeuden tulo on esimerkin tilanteessa sama kuin työmatkan pituus, joka pysyy samana. Aika ja nopeus ovat siten kääntäen verrannolliset. Jos ajoaikaa nopeudella 65 km/h merkitään t:llä, voidaan t ratkaista joko yhtälöstä   
# $20 min*80 km/h = t \cdot 65 km/h$  
# 
# tai verrannosta, jossa indeksit ovat käänteisessä järjestyksessä ($\frac{t_1}{t_2}=\frac{v_2}{v_1}$)
# 
# 
# $\frac{t}{20min}=\frac{80km/h}{65km/h}$.  Ratkaisu on molemmilla tavoilla sama: 
# $t = 80/65*20 min = 24.6 min$
# 
# ```
# ````

# ```{admonition} "y on verrannollinen x:n neliöön"
# :class: tip
# y on verrannollinen x:n neliöön tarkoittaa, että  
# 
# $y = k\cdot x^2 $ , missä k on vakio. 
# 
# 
# Verrantomuodossa sama asia voidaan ilmaista seuraavasti    
# 
# $\frac{y_1}{y_2}=\frac{{x_1}^2}{{x_2}^2}$ 
# ```

# ````{admonition} Esimerkki
# :class: note 
# Henkilöauton ilmanvastus on verrannollinen auton nopeuden neliöön. Oletetaan, että Audin ilmanvastus nopeudella 100 km/h ajettaessa on 230 N (*Newtonia*).  Mikä on ilmanvastus, kun nopeus on 120 km/h?
# 
# ```{admonition} Ratkaisu
# :class: dropdown
# Jos käytetään ilmanvastuksesta ja nopeudesta symboleja F ja v,  saadaan verranto 
# $\frac{F_1}{F_2}=\frac{{v_1}^2}{{v_2}^2}$
# 
# 
# $\frac{F}{230 N}=\frac{{(120km/h)}^2}{{(80km/h)}^2}$.     
# Ratkaisu on molemmilla tavoilla sama: 
# $F = \frac{{120}^2}{{80}^2}\cdot 230N \approx \text{518 }N$
# 
# ```
# ````
