import chess
import chess.engine

STOCKFISH_PATH = r"C:\Users\sarit\AppData\Local\Microsoft\WinGet\Packages\Stockfish.Stockfish_Microsoft.Winget.Source_8wekyb3d8bbwe\stockfish\stockfish-windows-x86-64-universal.exe"

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

board = chess.Board()

move=input("What is your initial move?(eg.b2b4)")
HumanMove=chess.Move.from_uci(move)

board.push(HumanMove)
result = engine.play(board, chess.engine.Limit(time=0.1))

print(f"The move entered is:{HumanMove}")

print("Arm has to move:",result.move.uci())

engine.quit()

