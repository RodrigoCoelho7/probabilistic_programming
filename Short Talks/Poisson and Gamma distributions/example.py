import tensorflow_probability as tfp
import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.reset_defaults()
sns.set_context(context='talk',font_scale=0.7)
plt.rcParams['image.cmap'] = 'viridis'
td = tfp.distributions


#Valor expectavel Lambda = 10
def example():
    LAMBDA = 10
    Nmax = 25
    step = 2
    n = 12
    model = td.Poisson(rate=LAMBDA, name='Fila_Continente')
    x = np.arange(0,Nmax)
    plt.bar(x[:n],model.prob(x)[:n],width=1,edgecolor='black')
    p = 1-model.cdf(n-1)
    plt.bar(x[n:],model.prob(x)[n:],width=1,edgecolor='black',label=f'$P(x\geq{n})={p:.2f}$')
    axes = plt.gca()
    axes.yaxis.grid(linewidth=1,color='gray')
    plt.title(f'Fila de epera do Continente, $\lambda={LAMBDA}$')
    plt.xticks(np.arange(0,Nmax,step),np.arange(0,Nmax,step))
    plt.xlabel('Número de Pessoas $k$')
    plt.ylabel('Probabilidade $P(X=k)$')
    plt.legend()
    plt.show()

def gammas():
    gs = [1,2,3,5,9,7.5,0.5]
    ts = [2,2,2,1,0.5,1,1]
    fig,ax = plt.subplots(figsize=(10,8))
    x = np.linspace(0,20,500)
    for i,g in enumerate(gs):
        b = 1/ts[i]
        model = td.Gamma(g,b)
        y = model.prob(x)
        ax.plot(x,y,label=f'$\\alpha={g},\\beta={b}$')
    ax.set_title(f'Probability density function')
    ax.yaxis.grid(linewidth=1,color='gray')
    ax.set_ylim(0,0.5)
    ax.legend()
    plt.show()

gammas()