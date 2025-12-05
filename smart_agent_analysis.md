Smart agent analysis : Intelligent VS Aléatoire sur 100 parties

Taux de victoires : 98 % de victoires pour Smart agent contre Random agent 

Efficacité de la stratégie : 'win': 98, 'block': 52, 'centre': 360, 'random': 151

Cas d'échec : les deux plateaux de défaites de smart agent :
array([[0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 2, 0, 0, 0],
       [2, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 2, 1, 0, 2],
       [1, 1, 0, 2, 2, 1, 2],
       [1, 1, 1, 2, 2, 1, 1]], dtype=int8)

array([[0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 2, 1, 0, 0],
       [1, 0, 1, 2, 1, 1, 2],
       [1, 0, 2, 1, 2, 2, 1]], dtype=int8)


Smart agent ne bloque que s'il y a déjà 3 pions alignés alors que il peut en avoir 2, un espace libre, et un autre pion. Ainsi dans ce cas, random agent a une possibilité de gagner et ne sera pas bloqué par smart agent. C'est ce qui ce passe dans les deux cas où random agent gagne.

Améliorations : On peut ajouter une modification qui simule le coup de l'adversaire et le bloque si ce coup entrainerait une victoire

