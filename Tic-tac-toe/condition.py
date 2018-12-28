def win_condition():
	if board[0]==board[1]==board[2]==1 or board[3]==board[4]==board[5]==1 or board[6]==board[7]==board[8]==1:
		game_state=0
		print("Win!")