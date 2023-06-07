#!/usr/bin/env python
# coding: utf-8

# # Lukujonot

# ## Lukujonon määritelmä

# ```{admonition} Lukujonon määritelmä
# :class: tip
# **Lukujonolla** tarkoitetaan järjestettyä jonoa lukuja.
# Esim. (1,3,2,5,6) ja (1.5, 3.5, 6.5, 8.5, 9.2) ovat lukujonoja   
# 
# ```

# ### Aritmeettinen jono

# **Aritmeettinen jono** on lukujono, jossa perättäisten termien erotus on vakio.
# 
# >esim.  (1,5,9,13,17,21)  on aritmeettinen jono, jossa perättäisten termien erotus on 4 

# ```{admonition} Yleiskaava aritmeettisen jonon n:nen alkion laskemiseksi
# :class: tip
# Olkoon jonon 1. termi $a_1$, n:s termi $a_n$ ja perättäisten termien erotus d. Tällöin      
#      
# $a_{n} = a_1 + (n-1)\cdot d$
# ```  
# 

# ```{admonition} Esim. Mikä on jonon (1,5,9,...) kymmenes luku?
# :class: dropdown
# Sijoitetaan yo. kaavaan $a_1=1, d = 4$ ja $n = 10$    
# 
# =>   $a_{10} = 1 + (10-1)\cdot 4 =  37$
# ```

# ### Aritmeettisen jonon termien summan laskeminen  

# Esim. Jonon (1,5,9,13,17,21) lukujen summa voidaan laskea korvaamalla luvut 1. ja viimeisen luvun keskiarvolla.      
# 1  + 5  + 9  + 13 + 17 + 21   =         
# 11 + 11 + 11 + 11 + 11 + 11   = 6*11 = 66        
# 
# **Luku 11 on lukujen 1 ja 21 keskiarvo. Kun jokainen luku korvataan sillä summa pysyy samana**

# ```{admonition} Aritmeettisen jonon alkioiden summan kaava
# :class: tip
# Aritmeettisen jonon lukujen summa = lukujen lukumäärä * ensimmäisen ja viimeisen luvun keskiarvo       
#      
# $S_{n} = n\frac{a_1+a_n}{2}$
# ```  
# 

# ```{admonition} Laske summa 1 + 5 + 9 + .... + 1005
# :class: dropdown
# Kyseessä on aritmeettinen jono, jossa 1. ja viimeinen termi ovat $a_1=1, a_n=1005$, erotus d = 4.        
# Summan laskemiseen tarvitaan vielä tieto termien lukumäärästä n.       
# Ratkaistaan n kaavasta $a_{n} = a_1 + (n-1)\cdot d$       
# => 1005 = 1 + (n-1)*4 => 1004 = (n-1)*4 =>  n-1 = 1004/4 = 251 => n = 254        
# 
# Nyt summa voidaan laskea 
# $S_{n} = n\frac{a_1+a_n}{2} $ => $S_{254} = 254\frac{1+1005}{2} = 126756$  
# 
# Vastaus: 126756
# ```

# ```{admonition} Aritmeettisen jonon 3. termi on 12 ja 8. termi -3. Määritä jono kokonaisuudessaan,kun siinä on 10 termiä.
# :class: dropdown
# Sijoittamalla kaavaan $a_{n} = a_1 + (n-1)\cdot d$ annetut tiedot, saadaan yhtälöt    
# $12 = a_1 + (3-1)d = a_1 + 2d$      
# $-3 = a_1 + (8-1)d = a_1 + 7d$         
# Vähentämällä yhtälöt puolittain, saadaan   
# $12-(-3) = (2-7)d$  eli  $15 = -5)d$, josta d = -15/-5 = -3. Sijoitus  1. yhtälöön antaa
# 
# $12 = = a_1 + 2*(-3) = a_1 - 6d$, josta $a_1 = 12 + 6 = 18$       
# 
# Vastaus: Koko jono on (18,15,12,9,6,3,0,-3,-6,-9)
# ```

# ```{admonition} 100000 euron tasalyhennyslainan laina-aika on 10 vuotta, ja nimelliskorko 6% p.a. Lyhennys ja korko maksetaan puolivuosittain. Laske koko laina-aikana maksettujen korkojen summa.   
# :class: dropdown
# Eriä on 20 kpl, joten lyhennys on 100000/20 = 5000 euroa. Puolen vuoden korko on 3%, joten 1. korko on 3%*100000 = 3000 euroa, seuraava 3%*95000 = 2850 euroa, viimeinen korko on 3%*5000 = 150 euroa.     
# Korot muodostavat aritmeettisen sarjan jossa 1. termi $a_1 = 3000$ ja erotus $d = -150$.      
# Maksettavien korkojen summa saadaan aritmeettisen sarjan summakaavalla:     
# 
# $S = n\frac{a_1+a_n}{2} = 20\frac{3000+150}{2} = 31500$      
# 
# Vastaus: 31500 euroa

# ## Geometrinen jono

# **Geometrinen jono on lukujono $(a_1,a_1 q,a_1 q^2,...,a_1 q^{n-1})$, jossa perättäisten termien suhde on vakio**
# 
# >esim1.  (1,1/2,1/4,1/8,1/16)  on geometrinen jono, jossa perättäisten termien suhde on 1/2. Ts. kukin termi saadaan edellisestä termistä kertomalla vakiolla 1/2.     
# 
# >esim2. (1,3,9,27,81) on geometrinen jono, jossa suhdeluku on 3.

# ```{admonition} Kaava geometrisen jonon n:nnen termin laskemiselle
# :class: tip
# Merkitään 1. termiä $a_1$ ja perättäisten termien suhdelukua $q$. 
# Tällöin yleiskaava n:nnen termin laskemiselle on    
# 
# $a_n = a_1 q^{n-1}$ 
# ```

# ### Geometrisen jonon lukujen summan laskukaava

# Summakaava perustuu taulukkokirjan kaavaan $\frac{1-x^n}{1-x}= 1 + x + x^2 + .... + x^{n-1}$

# ```{admonition} Kaava geometrisen jonon summalle
# :class: tip
# Merkitään 1. termiä $a_1$ ja perättäisten termien suhdelukua $q$. 
# Jonon alkioiden summa $S_n = a_1+a_1 q+a_1 q^2+...+a_1 q^{n-1})$ on tällöin      
# 
# 
# $S_n = a_1\frac{1-q^n}{1-q}$   ( rajoitus $q\neq 1$)
# ```

# ```{admonition} Mikä on jonon (1,3,9,27,81) alkioiden summa?
# :class: dropdown
# Kyseessä on geometrinen jono, jossa $a_1=1$,$n=5$ ja suhdeluku $q=3$     
# 
# Summa on $1\frac{1-3^5}{1-3}$ = (1- 243)/-2 = -242/-2 = $121$
# 
# ```

# ```{admonition} Mikä on jonon (2,1,1/2,1/4,1/8,1/16) alkioiden summa?
# :class: dropdown
# Kyseessä on geometrinen jono, jossa $a_1=2$,$n=6$, ja suhdeluku $q=1/2$     
# 
# Summa on $2\frac{1-(1/2)^5}{1-1/2}$ =  $63/16$     
# 
# *(tulos saatu laskimella syötteellä 2*(1-(1/2)^6)/(1-1/2))*
# 
# ```

# ```{admonition} Lapsenlapsen syntyessä mumm0 päättää tallettaa 10 euroa kk tilille, jonka kk-korko on 0.5%, tarkoituksena luovuttaa kertynyt summa, kun lapsenlapsi täyttää 20 vuotta. Kuinka paljon rahaa on kertynyt? 
# :class: dropdown      
# 0.5% korkoa vastaava korkokerroin on 1 + 0.5/100 = 1.005.     
# 
# 1. sataselle korkoa maksetaan 240 kertaa, joten sen loppuarvo on $10\cdot 1.005^{240}$.   
# 2. sataselle korkoa maksetaan 239 kertaa, joten sen loppuarvo on $10\cdot 1.005^{239}$ 
# ...        
# Viimeiselle maksetaan vain 1 kk korko, joten sen loppuarvo on $10\cdot 1.005$
# 
# Tilin loppusaldo on  $10\cdot 1.005 +  10\cdot 1.005^2 +...+ 10\cdot 1.005^{240}$. 
# 
# Kyseessä on geometrinen sarja, jossa suhdeluku q = 1.005 ja 1. termi 10*1.005 = 10.05.       
# 
# Summakaava $S_n = a_1\frac{1-q^n}{1-q}$ antaa $S_n = 10.5\frac{1-1.005^240}{1-1.005} = 4644 $     
# 
# Vastaus: 4644 euroa.
# ```

# >Huom! Seuraavassa luvussa *pitkäaikaisista lainoista* esitetään kaava tasaerälainan lyhennyksen laskemiselle.  Kaava perustuu geometrisen sarjan summan kaavaan. Myös yo. kuukausisäästämiselle esitetään yleinen laskukaava.
