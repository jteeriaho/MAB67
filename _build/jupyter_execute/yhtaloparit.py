#!/usr/bin/env python
# coding: utf-8

# # Yhtälöparit

# ## Lineaariset yhtälöparit  

# ```{admonition} Lineaarisen yhtälöparin perusmuoto    
# :class: tip
# $\begin{matrix}
# a_1 x + a_2 y = b_1\\
# a_3 x + a_4 y = b_2
# \end{matrix}$
# 
# ```
# Muuttujat x ja y ovat vasemmalla puolen omissa sarakkeissaan, vakiot oikealla puolen yhtälöitä.
# 

# Perinteisiä ratkaisutapoja ovat  **eliminoimismenetelmä** ja **sijoitusmenetelmä**

# ```{admonition} Eliminoimismenetelmä    
# :class: tip
# Kerrotaan jompikumpi tai molemmat yhtälöistä sopivilla vakioilla siten, että   
# jommankumman muuttujan kertoimet yhtälöissä ovat vastaluvut.   
# Lasketaan yhtälöt yhteen, jolloin saadaan 1. asteen yhtälö, josta toinen muuttujista voidaan ratkaista 
# Ratkaistu muuttuja sijoitetaan johonkin alkuperäisistä yhtälöistä ja ratkaistan toinen muuttuja.
# ```

# ````{admonition} Esim. Ratkaise eliminoimismenetelmällä yhtälöpari    
# :class: note
# $\begin{matrix}
# 2x-5y=-4\\
# 3x+2y=13
# \end{matrix}$  
# ```{admonition} Ratkaisu
# :class: dropdown
# Kerrotaan 1. yhtälö luvulla 2 ja 2. yhtälö luvulla 5 , jolloin saadaan     
# $\begin{matrix}
# 4x-10y=-8 \\
# 15x+10y=65
# \end{matrix}$    
# 
# Lasketaan yhtälöt puolittain yhteen. Saadaan 19 x = 57, josta x = 57/19 = 3    
# Sijoitetaan tämä 1. yhtälöön, jolloin saadaan 2*3-5y=-4 eli 10 = 5y , josta y = 2   
# 
# Vastaus:  **x = 3 ja y = 2**
# 
# ```
# ````

# ```{admonition} Sijoitusmenetelmä    
# :class: tip
# 1. Ratkaistaan 1. (tai 2.) yhtälö esim. x:n suhteen.    
# 2. Sijoitetaan saatu lauseke kyseisen x:n tilalle toiseen yhtälöön, josta ratkaistaan y.    
# 3. x saadaan sijoittamalla y kohdassa 1. saatuun lausekkeeseen
# ```

# ````{admonition} Esim. Ratkaise sijoitusmenetelmällä yhtälöpari 
# :class: note
# $\begin{matrix}
# 2x-5y=-4 \\
# 3x+2y=13
# \end{matrix}$     
# ```{admonition} Ratkaisu
# :class: dropdown
# 1. Ratkaistaan 1. yhtälö x:n suhteen. Saadaan 2x=5y-4 , josta x = 5/2y - 2  
# 2. Sijoitetaan tämä 2.:een yhtälöön => 3(5/2y-2)+2y = 13 => 15/2 y -6 + 2y=13 => 19/2 y = 19 => y = 2 
# 3. Sijoitetaan tämä kohdassa 1 saatuun lausekkeeseen => x = $5/2\cdot2-2$ = 3  
# 
# Vastaus:  **x = 3 ja y = 2**
# 
# ```
# ````
