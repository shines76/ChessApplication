using Stockfish.NET;

namespace ChessStockfish;

public class StockfishService : IStockfishService
{
    private readonly Stockfish.NET.Stockfish _stockfish;
    public StockfishService(Stockfish.NET.Stockfish stockfish)
    {
        _stockfish = stockfish;
    }
    public async Task<bool> CheckMate()
    {
        throw new NotImplementedException();
    }

    public Task<Stockfish.NET.Stockfish> PlayMove(string move)
    {
        throw new NotImplementedException();
    }

    public async Task<Stockfish.NET.Stockfish> Start(string playerTeam)
    {
        throw new NotImplementedException();
    }
}
