{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(237, 4)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age Range</th>\n",
       "      <th>Head Size(cm^3)</th>\n",
       "      <th>Brain Weight(grams)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4512</td>\n",
       "      <td>1530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3738</td>\n",
       "      <td>1297</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4261</td>\n",
       "      <td>1335</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3777</td>\n",
       "      <td>1282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4177</td>\n",
       "      <td>1590</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gender  Age Range  Head Size(cm^3)  Brain Weight(grams)\n",
       "0       1          1             4512                 1530\n",
       "1       1          1             3738                 1297\n",
       "2       1          1             4261                 1335\n",
       "3       1          1             3777                 1282\n",
       "4       1          1             4177                 1590"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plot\n",
    "plot.rcParams['figure.figsize']=(20.0,10.0)\n",
    "data = pd.read_csv('headbrain.csv')\n",
    "print(data.shape)\n",
    "data.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "X= data['Head Size(cm^3)'].values\n",
    "Y= data['Brain Weight(grams)'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_x= np.mean(X)\n",
    "mean_y= np.mean(Y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.26342933948939945 325.57342104944223\n"
     ]
    }
   ],
   "source": [
    "n = len(X)\n",
    "numer=0\n",
    "denom=0\n",
    "for i in range(n):\n",
    "    numer+= (X[i]-mean_x) * (Y[i]-mean_y)\n",
    "    denom+=(X[i]-mean_x)**2\n",
    "m= numer/denom\n",
    "c= mean_y-(m*mean_x)\n",
    "print(m,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYsAAAEGCAYAAACUzrmNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nO2daZgU1dWA38MIIuICAzFGpAcBWUTZBpdgcBdFxTWKQcWAoqhx+0QkaNyC0UBUcAlBgxsIokZFRAVcAFccEBXZUdRBE1lE2bc534+qZnp6qrqre7qnu6fP+zz1TPetW/feKpp76p7tiqpiGIZhGLGolekBGIZhGNmPCQvDMAwjLiYsDMMwjLiYsDAMwzDiYsLCMAzDiMtumR5AOmjUqJEWFRVlehiGYRg5xZw5c1aramOvczVSWBQVFVFSUpLpYRiGYeQUIvKN3zlTQxmGYRhxMWFhGIZhxMWEhWEYhhGXGmmz8GL79u2UlpayZcuWTA/FSIK6devSpEkTateunemhGEZekjfCorS0lL322ouioiJEJNPDMRJAVVmzZg2lpaU0a9Ys08MxjLwkb9RQW7ZsobCw0ARFDiIiFBYW2qrQMDJI3ggLwARFDmP/doaRWfJKWBiGYRjJYcKiGikoKKBDhw60a9eOM844g3Xr1mV6SBXo0aNHSsZ0xx13MHz4cAD+8pe/MH369Cq3aRj5wzigCGd6LnK/Zx4TFtXIHnvswbx585g/fz4NGzbkkUceSUm7O3bsSEk7U6ZMYd99901JW2HuuusuTjzxxJS2aRg1l3FAf+AbQN2//ckGgWHCIkMcddRRrFy5ctf3YcOG0aVLFw477DBuv/32XeV33303rVu35qSTTuLCCy/c9cZ+7LHH8uc//5ljjjmGESNGsGrVKs4991y6dOlCly5deP/99wGYMWMGHTp0oEOHDnTs2JH169fzww8/0K1bt12rnFmzZgFOmpTVq1cDcP/999OuXTvatWvHgw8+CMCKFSto06YNl19+OYcccggnn3wymzdvjnmfl156KS+88MKu9m+//XY6derEoYceyqJFiwDYuHEjffv2pUuXLnTs2JFXXnklFY/YMHKQIcCmqLJNbnlmyRvX2Uiuvx7mzUttmx06gDunxmXnzp289dZb9OvXD4CpU6eydOlSZs+ejarSs2dPZs6cSb169XjxxRf59NNP2bFjB506daJz58672lm3bh0zZswA4A9/+AM33HADRx99NN9++y3du3dn4cKFDB8+nEceeYSuXbuyYcMG6taty+jRo+nevTtDhgxh586dbNpU8cc5Z84cnnjiCT7++GNUlSOOOIJjjjmGBg0asHTpUsaPH89jjz3G+eefz4svvshFF10U+Dk1atSIuXPn8uijjzJ8+HAef/xxhg4dyvHHH8+YMWNYt24dhx9+OCeeeCJ77rln4HYNo2bwbYLl1UdeCotMsXnzZjp06MCKFSvo3LkzJ510EuAIi6lTp9KxY0cANmzYwNKlS1m/fj1nnnkme+yxBwBnnHFGhfYuuOCCXZ+nT5/OggULdn3/5ZdfWL9+PV27duXGG2+kd+/enHPOOTRp0oQuXbrQt29ftm/fzllnnUWHDh0qtPvee+9x9tln75qszznnHGbNmkXPnj1p1qzZrvqdO3dmxYoVCT2Dc845Z9e1//nPf3bd/6RJk3atmrZs2cK3335LmzZtEmrbMPwZh/N2/i3QFBgK9M7oiLxpiqN68irPLHkpLIKuAFJN2Gbx888/c/rpp/PII49w7bXXoqoMHjyYK664okL9Bx54IGZ7kW/eZWVlfPjhh7sES5hbbrmF0047jSlTpnDkkUcyffp0unXrxsyZM3nttde4+OKLGThwIJdccsmua1TVt8/dd9991+eCgoK4aii/6wsKCnbZWlSVF198kVatWiXUlmEEI2wHCK+gw3YAyD6BMZSKYwWo55ZnFrNZZIB99tmHkSNHMnz4cLZv30737t0ZM2YMGzZsAGDlypX8+OOPHH300bz66qts2bKFDRs28Nprr/m2efLJJ/Pwww/v+j7P1bMtX76cQw89lEGDBlFcXMyiRYv45ptv+NWvfsXll19Ov379mDt3boW2unXrxssvv8ymTZvYuHEjL730Er/73e/S8CQcunfvzkMPPbRLSH366adp68vIR7LXDlCZ3sBoIASI+3c02SDU8nJlkQ107NiR9u3bM2HCBC6++GIWLlzIUUcdBUD9+vUZO3YsXbp0oWfPnrRv355QKERxcTH77LOPZ3sjR47k6quv5rDDDmPHjh1069aNUaNG8eCDD/LOO+9QUFBA27ZtOfXUU5kwYQLDhg2jdu3a1K9fn6effrpCW506deLSSy/l8MMPB+Cyyy6j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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "min_x = np.min(X)-100\n",
    "max_x= np.max(X)+100\n",
    "x = np.linspace(min_x,max_x,1000)\n",
    "y = m*x+c\n",
    "plot.plot(x,y,color='blue',label='Regression line')\n",
    "plot.scatter(X,Y,c='yellow',label='data')\n",
    "plot.xlabel('head size')\n",
    "plot.ylabel('brain size')\n",
    "plot.legend()\n",
    "plot.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6393117199570003\n"
     ]
    }
   ],
   "source": [
    "st=0\n",
    "sr=0\n",
    "for i in range(len(Y)):\n",
    "    y1= m*X[i]+c\n",
    "    st+= (Y[i]-mean_y)**2\n",
    "    sr+=(Y[i]-y1)**2\n",
    "r2= 1-(sr/st)\n",
    "print(r2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.639311719957\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error\n",
    "X= X.reshape((n, 1))\n",
    "reg = LinearRegression()\n",
    "reg = reg.fit(X,Y)\n",
    "Y1 = reg.predict(X)\n",
    "r2 = reg.score(X,Y)\n",
    "print(r2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Gender  Age Range  Head Size(cm^3)  Brain Weight(grams)\n",
      "0       1          1             4512                 1530\n",
      "1       1          1             3738                 1297\n",
      "2       1          1             4261                 1335\n",
      "3       1          1             3777                 1282\n",
      "4       1          1             4177                 1590\n",
      "5       1          1             3585                 1300\n",
      "6       1          1             3785                 1400\n",
      "7       1          1             3559                 1255\n"
     ]
    }
   ],
   "source": [
    "print(data.head(8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(237, 4)\n"
     ]
    }
   ],
   "source": [
    "print(data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
