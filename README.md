# Projet de finance dans le cadre du M2 MoSEF
## Stratégie d'investissement basé sur le papier : "Construction of stock portfolios based on k-means clustering of continuous trend features" par Dingming Wu, Xiaolong Wang et Shaocong Wu.
### Introduction

Le but du papier est de construire un portefeuille d'actifs financiers avec aucune limite de titres financiers en entrée. En effet, les méthodes traditionnelles d'optimisation de placements financiers reposent sur la maximisation de la Mean-Variance ou de ratios qui s'en rapportent (Markowitz). 

Ce papier, permet à l'aide d'un prétraitement à base de l'algorithme de clustering K-Means, de réaliser un portefeuille basé sur tous les titres financiers directement sans préselection de la part des investisseurs.

### Fonctionnement de la stratégie

La première partie de l'algorithme consiste à discriminer les titres financiers en un nombre de cluster N choisis.

La deuxième partie est la combinaison d'un Discrete Wavelete Transform (transformation mathématique) avec un Extreme Learning Machine (réseau de neuronne à une couche caché). La méthode Discrete Wavelete Transform permet de lisser les courbes des métriques financières afin d'en effacer le bruit. Par la suite, l'Extreme Machine Learning prédit la tendance d'un actif.
