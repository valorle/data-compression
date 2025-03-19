# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:21:59 2023

@author: valorle
"""
import numpy as np 


########################################
# Methode Globale
########################################
def findFrequences(texte):
    tmp = {};
    longueur = len(texte);
    for t in texte:
        try:
            tmp[t] = tmp[t] + 1/longueur;
        except:
            tmp[t] = 1/longueur;
    return tmp;



########################################
# Noeud
########################################
class Noeud:
    def __init__(self, caractere, freq, gauche=None, droite=None):
        self.caractere = caractere;
        self.freq = freq;
        self.next = {'gauche':gauche, 'droite':droite};
        self.codage = [];
        
    def __str__(self):
        tmp = 'Caractere : {}\nFrequence : {}\n'.format(self.caractere, self.freq);
        # tmp.append('Next = self.next);
        return tmp;
    
    def __lt__(self, other):
        if self.freq < other.freq:
            return True;
        else:
            return False;
    
    def __add__(self, other):
        newNode = Noeud(self.caractere+other.caractere, 
                        self.freq+other.freq,
                        self, other);
        return newNode;
    
########################################
# Arbre
########################################
class Arbre:
    def __init__(self, dicoFreq):
        self.codes = {};
        self.ListeNodes = [];
        for s,f in dicoFreq.items():
            self.ListeNodes.append(Noeud(s, f));
        # for noeud in self.ListeNodes:
        #     print(noeud);
        while len(self.ListeNodes) > 1:
            noeudGauche = self.findMin();
            self.removeNoeud(noeudGauche);
            noeudDroite = self.findMin();
            self.removeNoeud(noeudDroite);
            # newNode = Noeud(noeudGauche.caractere+noeudDroite.caractere, 
            #                 noeudGauche.freq+noeudDroite.freq, 
            #                 noeudGauche, noeudDroite);
            newNode = noeudGauche + noeudDroite;
            self.addNoeud(newNode);
            
    # def __str__(self):
    #     for tmp in self.ListeNodes:
    #         tmp.append(self.ListeNodes)
            
    def findMin(self):
        noeudMin = self.ListeNodes[0];
        for noeud in self.ListeNodes:
            if noeudMin < noeud:
                continue;
            else:
                noeudMin = noeud;
        return noeudMin;
    
    def removeNoeud(self, node):
        if node in self.ListeNodes:
            self.ListeNodes.remove(node);
        else:
            raise Exception('Node is not in the list.');

    def addNoeud(self, node):
        self.ListeNodes.append(node);
        
    def etiquetage(self, node):
        for side, noeud in node.next.items():
            if node == None:
                noeud.codage = ''.join(noeud.codage);
                self.codes[node.caractere] = noeud.codage;
                return;
            else:
                if side == 'gauche':
                    node.codage = node.codage + ['1'];
                elif side == 'droite':
                    node.codage = node.codage + ['0'];
                self.etiquetage(noeud);
    
    
# Programme principal
if __name__  == '__main__':
    file = False;
    
    if file == False:
        textACompresser = 'Gojo Satoru is a silly cat.';
    else:
        with open('name.txt','r') as file:
            textACompresser = np.genfromtxt(file);
            
    freq = findFrequences(textACompresser);    
    arbreTest = Arbre(freq);
    # print(arbreTest.findMin());
    print('noeud racine : ', arbreTest.ListeNodes[0]);
    print(arbreTest.etiquetage(arbreTest.ListeNodes[0]));
