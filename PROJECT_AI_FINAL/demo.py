function minimax(vị trí,độ sâu,người chơi max)
	//Nếu node đang xét là node lá hoặc là chỗ mà trò chơi kết thúc
	if độ sâu = 0 or trò chơi kết thúc in vị trí
		//Trả về giá trị của vị trí đó
		return giá trị of vị trí
	//Nếu người chơi hiện tại là max
	if người chơi max:
		//Khởi tạo giá trị maxEval bằng âm vô cùng
		maxEval = -∞
		//Duyệt các trường hợp con của vị trí đó
		for each child of vị trí
			//Lấy giá trị của từng trường hợp con
			eval = minimax(child,độ sâu - 1,người chơi min)
			//Cập nhật giá trị cho maxEval
			maxEval = max(maxEval, eval)
		//Trả về giá trị max của các trường hợp con
		return maxEval
	//Nếu người chơi hiện tại là min
	else
		//Khởi tạo giá trị minEval bằng dương vô cùng
		minEval = +∞
		//Duyệt các trường hợp con của vị trí đó
		for each child of vị trí
			//Lấy giá trị của từng trường hợp con
			eval = minimax(child,độ sâu - 1,người chơi max)
			//Cập nhật giá trị cho minEval
			minEval = min(minEval, eval)
		//Trả về giá trị min của các trường hợp con
		return minEval