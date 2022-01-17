# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:15:44 2020

@author: Saqib
"""
import numpy as np  #importing libraries here.
class test:
    def __init__(self):
        self.board=np.zeros((3,3)) #initializing a array of size 3x3 with 0s.
        
    def displayBoard(self): #function to display current status of the board
        print(self.board)
        
    def takeInput(self,player): # In this function, take input from user and 
        #then validate the input using isLeagl function. This function takes
        #one parameter: player: which contains either 1 or 2. 
        #if it is turn of player 1 then player will contain 1 otherwise 2.
        
        #taking indicies as input on which user wants to make move.
        r=int(input("Enter Row"))
        c=int(input("Enter col"))
        
        #validating the input using isLegalMove function.
        islegal=self.isLegalMove(r,c)
        if(islegal==1):
            
            #if move is legal then board will be updated.
            self.board[r,c]=player
            
    def hasWon(self,player):
        
    def Drawn(self):  #add your code to check whether game is drawn
       ##there is no 0 at any position in the array         
        
    def turnChange(self,play): #The purpose of this function is to change turn
        if play==1:
            play=2
        else:
            play=1
        return play
    
    def isLegalMove(self,r,c):# the purpose of this function is to validate the
        #input given by user on the following conditions.
        ##r and c are between 0 and 2
        ##board[r][c] is equal to 0
        ##return 1 or 0
play=1  #at start it is turn of player 1.

finish=0 # if value of finsish in other than 0, game should be stopped.

t1=test() #creating object of the class.

t1.displayBoard()

while (finish==0):
    
    t1.takeInput(play)
    t1.displayBoard()
    play=t1.turnChange(play)
