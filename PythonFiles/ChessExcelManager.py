import pandas as pd
import ChessGame
import ChessDataBase
from ChessParser import * 

def ExportChessGameToExcel(game, sheet_name):
    metadata = game.Game_GetMetaData()
    moves = game.Game_GetMoves()
    df = pd.DataFrame(metadata, columns=["Key", "Value"])
    df2 = pd.DataFrame(moves, columns=['Moves'])
    writer = pd.ExcelWriter('chessgame.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name,
                header='Metadata', index=False)
    df2.to_excel(writer, sheet_name=sheet_name,
                 index=False, header='Moves', startcol=2, startrow=0)
    writer.save()


def ImportChessGameFromExcel(filepath):
    open_file = pd.read_excel(filepath, sheet_name=0)
    keys = list(open_file['Key'])
    values = list(open_file['Value'])
    moves = list(open_file['Moves'])
    metadata = []
    for i in range(12):
        metadata.append([keys[i], values[i]])
    newGame = ChessGame.ChessGame(metadata, moves)
    return newGame

#RUN THIS ONE TO EXPORT CHESSGAME TO EXCEL-FILE
def runTest(inputLocalPathForPNGfile):
    games = ImportChessDataBase(inputLocalPathForPNGfile)
    testgame = games[0]
    ExportChessGameToExcel(testgame, '1')
    test = ImportChessGameFromExcel('chessgame.xlsx')

#INSERT FILEPATH FOR PNG FILE HERE:
pathForPng = ''
runTest(pathForPng)

