import chess # imports the python-chess library to track rules, valid chess movement//
import chess.engine #imports module that handles bg communicaiton with chess engine usign standard protocols

STOCKFISH_PATH = r"C:\Users\sarit\AppData\Local\Microsoft\WinGet\Packages\Stockfish.Stockfish_Microsoft.Winget.Source_8wekyb3d8bbwe\stockfish\stockfish-windows-x86-64-universal.exe"

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)#stockfish.exe is opened as a bg process and two way command pipe using UCI porotcol

board = chess.Board()#initializes 8*8 chess board in memory with all 32 pieces in their default starting points
result = engine.play(board, chess.engine.Limit(time=0.1))#sends current board status to stockfish over uci channel / gives stockfish 0.1 sec to give best move

print("---------------------------------------")
print("Stockfish recommends move:", result.move.uci())#prints the rec move by stockfish like e2e4 meaning move piece form e1 to e4
print("---------------------------------------")

engine.quit()#terminates stockfish.exe