#!/usr/bin/env python
# coding: utf-8

# # Trabajo Práctico – Variables Aleatorias y distribuciones conocidas

# # Ejercicio 1
# Se X una variable aleatoria discreta que toma valores entre 0 y 4.
# 
# a. ¿Cuál de las siguientes funciones es una posible función de probabilidad de X? Justifica cual si y cual no. X 0 1 2 3 4 

# ![ejercicio1.JPG](attachment:ejercicio1.JPG)

# b. Para la función de probabilidad seleccionada calcule la media y la varianza.
# 
# c. Determine 𝑃(𝑋<2) y la 𝑃(𝑋>1)

# ## Solución
# ### Parte a
# Para la función de probabilidad de la variable aleatoria discreta X, la sumatoria de todas la probabilidades debe ser igual a 1.
# 
# Probando con la primera
# Σp1(x)=0,2+0,2+0,3+0,1+0,1=0,9 --> No es igual a 1, no es una función válida
# 
# Σp2(x)=0,1+0,3+0,3+0,2+0,2=1,1 --> Es mayor a 1, no es una función válida
# 
# Σp3(x)=0,1+0,2+0,4+0,2+0,1=1,1 --> Es igual a 1, por ende p3(x) es una función válida
# 
# ### Parte b
# Para la función válida p3
# E(X) = ∑(𝑥 * 𝑝(𝑥))
# E(X) = ((0*0,1)+(1*,02)+(3*0,4)+(4*0,2)+(5*0,1))
# E(X) = 2,52
# 
# Para calcular la varianza, utilizamos la fórmula:
# 
# Var(X) = ∑((𝑥 - 𝐸(X))² * 𝑝(x))
# 
# Var(X) = (0 - 2.3)^2 * 0.1 + (1 - 2.3)^2 * 0.3 + (2 - 2.3)^2 * 0.3 + (3 - 2.3)^2 * 0.2 + (4 - 2.3)^2 * 0.2
# 
# Var(X) = 1,21
# 
# ### Parte c
# 
# P(X < 2) = p3(0) + p3(1) = 0.1 + 0.2 = 0.3
# 
# P(X > 1) = p3(2) + p3(3) + p3(4) = 0.4 + 0.2 + 0.1 = 0.7

# # Ejercicio 2
# 
# La última novela de cierto autor ha tenido un importante éxito, hasta el punto de que el 80 % de los lectores ya la han leído. Un grupo de cuatro amigos son aficionados a la lectura:
# 
# a. ¿Cuál es la probabilidad de que en el grupo hayan leído la obra dos personas? ¿Y al menos dos?
# 
# b. Calcule la media y la varianza. Interprete los resultados.

# ## Solución
# ## Definición de la solución
# #### Este pertenece a una Distribución Binomial
# P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
# 
# Donde P(X = k) representa la probabilidad de que k personas hayan leído la obra. La variable aleatoria sería la cantidad de personas que hayan leído la obra.

# In[1]:


from scipy.stats import binom

prob_exito = 0.8
num_ensayos = 4

# Probabilidad de exactamente 2 personas hayan leído la obra
prob_2_pers = binom.pmf(2, num_ensayos, prob_exito)

# Probabilidad de al menos dos personas hayan leído la obra
prob_al_menos_2_pers = 1 - binom.cdf(1, num_ensayos, prob_exito)

# Media y varianza
media = num_ensayos * prob_exito
varianza = num_ensayos * prob_exito * (1 - prob_exito)

print("Probabilidad de que en el grupo hayan leído la obra dos personas:", prob_2_pers)
print("Probabilidad de que en el grupo hayan leído la obra al menos dos personas:", prob_al_menos_2_pers)
print("Media:", media)
print("Varianza:", varianza)


# # Ejercicio 3 
# Si 0,05 es la probabilidad de que cierta pieza en una línea de producción sufra una desviación excesiva. ¿cuál es la probabilidad de que la sexta pieza probados sea la primera en mostrar dicha desviación?

# ## Solución
# ## Definición de la solución
# #### Este pertenece a una Distribución Geométrica
# P(X = k) = (1 - p)^(k - 1) * p
# 
# P(X = k) es la probabilidad de que el evento ocurra en el ensayo número k

# In[2]:


from scipy.stats import binom

prob_desv = 0.05
num_piezas = 6
pos_fallo = 1

prob_primera= binom.pmf(pos_fallo, num_piezas, prob_desv)

print("La probabilidad de que la sexta pieza sea la primera en mostrar desviación es:", prob_primera)


# # Ejercicio 4
# Una máquina de bebidas se regula para que sirva 200 ml por vaso. Si la cantidad de bebida se distribuye normalmente con desvió estándar de 15 ml.
# 
# a. ¿Cuál es la probabilidad de que una bebida contenga más de 224 ml?
# 
# b. Determine el porcentaje de bebidas que contendrán entre 191 ml y 209 ml.
# 
# c. ¿Cuál es la probabilidad de que una bebida contenga menos de 190 ml?
# 
# d. En todos los casos anteriores grafiqué la probabilidad como el área debajo de la curva.

# ## Solución
# ## Definición de la solución
# #### Este pertenece a una Distribución Normal
# 
# Y la variable aleatoria es la cantidad de bebida servida por vaso

# In[3]:


#Colocando los datos de Entrada
import scipy.stats as stats

media = 200
desv_std = 15


# ### Parte a

# In[4]:


x = 224

prob = 1 - stats.norm.cdf(x, media, desv_std)
print("La probabilidad de que una bebida contenga más de 224 ml es:", prob)


# ### Parte b

# In[5]:


x1 = 191
x2 = 209

prob_rango = stats.norm.cdf(x2, media, desv_std) - stats.norm.cdf(x1, media, desv_std)
porc = prob_rango * 100
print("El porcentaje de bebidas que contendrán entre 191 ml y 209 ml es:", porc)


# ### Parte c

# In[6]:


x3 = 190

prob_menor = stats.norm.cdf(x3, media, desv_std)
print("La probabilidad de que una bebida contenga menos de 190 ml es:", prob_menor)


# ### Parte d

# In[7]:


import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(media - 3 * desv_std, media + 3 * desv_std, 100)

# Calculate y values using PDF
y_values = stats.norm.pdf(x_values, media, desv_std)

# Plot the PDF
plt.plot(x_values, y_values)

# Shade the area for the desired probabilities
plt.fill_between(x_values, y_values, where=(x_values > x), alpha=0.5, color='red')
plt.fill_between(x_values, y_values, where=((x1 < x_values) & (x_values < x2)), alpha=0.5, color='green')
plt.fill_between(x_values, y_values, where=(x_values < x3), alpha=0.5, color='blue')

# Set labels and title
plt.xlabel('Cantidad de bebida (ml)')
plt.ylabel('Probabilidad')
plt.title('Distribución Normal de la Cantidad de Bebida')

# Show the plot
plt.show()

