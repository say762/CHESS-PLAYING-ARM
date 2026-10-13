import chess
import chess.engine

def human():
    human_move=input("What is your move?(eg.b2b4)")
    return chess.Move.from_uci(human_move)

def stockfishmove(board,engine):
    result=engine.play(board,chess.engine.Limit(time=0.1))
    return result.move 

STOCKFISH_PATH = r"C:\Users\sarit\AppData\Local\Microsoft\WinGet\Packages\Stockfish.Stockfish_Microsoft.Winget.Source_8wekyb3d8bbwe\stockfish\stockfish-windows-x86-64-universal.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
board = chess.Board()

color_option=input("which color do you want to play?(white/black)")
print(f"User chose:{color_option}")

if color_option =="white":
    print("-------------------YOU ARE PLAYING WHITE-------------------")

    Human_move=human()
    board.push(Human_move)
    ENGINE_MOVE=stockfishmove(board,engine)
    print(f"Stoskfish moves:{ENGINE_MOVE.uci()}")
    board.push(ENGINE_MOVE)

elif color_option == "black":
    print("-------------------YOU ARE PLAYING BLACK-------------------")
    print("\n-------------------ARM PLAYS FIRST------------------")
    ENGINE_MOVE=stockfishmove(board,engine)
    print(f"Stoskfish moves:{ENGINE_MOVE.uci()}")
    board.push(ENGINE_MOVE)

    Human_move=human()
    board.push(Human_move)

else:
    print("INVALID!CHOOSE A VALID COLOUR(WHITE/BLACK)")


engine.quit()

