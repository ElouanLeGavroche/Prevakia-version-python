import pygame


class Niveau_3():
    def __init__(self):

        self.pos_carte = [0, 0]


        self.mur = [#strucutre théorique du jeu
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,3,3,3,1,1,1,1,    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,       0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,8,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,       0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,4,8,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,       0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,4,8,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,       0,4,0,0,0,0,0,0,0,0,0,1,1,1,1,1,4,8,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,4,1,1,1,1,1,1,1,0,0,3,3,3,3,1,1,1,0,0,5,6,1,1,1,    1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,    1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,4,3,3,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,1,    1,0,0,0,0,0,0,0,3,3,52,0,0,4,1,3,3,3,0,0,0,0,0,0,1,    1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,       1,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,       1,0,0,0,0,0,0,4,1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,       1,0,0,0,0,0,0,4,1,0,0,0,1,1,1,1,1,1,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,       1,0,1,1,1,1,1,4,1,4,0,0,1,1,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,       1,0,0,0,0,0,0,4,1,4,0,0,1,1,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [0,0,0,0,0,0,0,0,0,0,0,5,6,1,1,1,1,1,1,1,1,1,0,0,0,       0,0,0,0,0,0,0,4,1,4,0,0,1,1,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [0,0,0,0,0,0,0,0,0,0,5,6,1,1,1,1,1,1,1,1,1,1,0,0,0,       0,0,0,0,0,0,0,4,1,4,1,1,1,1,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1 ],
            [0,0,0,0,0,0,0,0,0,5,6,1,1,1,1,1,1,1,1,1,1,1,0,0,0,       0,0,0,0,0,0,0,4,1,4,8,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1 ],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,       0,0,0,5,6,1,1,1,1,4,8,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1 ],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,1,1,1,1,1,1,1,1,4,8,0,0,0,0,0,0,0,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1 ],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,1,1,1,1,1,1,1,1,4,8,0,0,0,0,0,0,5,1,4,0,0,0,0,1,    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,4,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1 ],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,       1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ],
            ]
           #position X et Y, Type d'objet, ID de l'objet, Si il est toujours sur la carte
           # 1 = clé exemple, qui ouvrira la porte qui à le même ID
        self.pos_items = [[187,143,1,3, True],[3492,300,3,3, True],[3492,300,2,3, True],[1398, 320, 7, 20, True], [1398, 320, 6, 20, True],
                          [2298, 320, 7, 20, True], [2298, 320, 6, 20, True], [3465, 100, 8, 20, True], [3105,110,9,20, True],
                          [1329, 20, 7, 20, True], [1329, 20, 6, 20, True], [2512, 30, 11,0, True], [2512, 30, 10,0, True]
                          ]
        self.eteindre = 3
        self.bouclier = True
        
        self.a = 0
        self.tableau = []
        self.tableau_move_plan_1 = []
        self.tableau_move_plan_fond = 100
        for i in range(4):
            
            self.tableau.append(self.a) #Nombre de scrolls pour afficher tout le niveau
            self.tableau_move_plan_1.append(self.a)#même tableau mais qui va être modifier quand on bouge
            self.a += 900
            
        
        
