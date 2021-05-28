import tkinter as tk
import GameProcess as G
import GUI

player = G.Player.Player("Player")
dealer = G.Player.Player("Dealer")
print("Welcome to BlackJack21 By noobcoder810")

GUI.GUI(player,dealer)

