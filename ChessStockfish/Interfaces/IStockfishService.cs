using Stockfish.NET;

public interface IStockfishService
{
    Task<Stockfish.NET.Stockfish> Start(string playerTeam);
    Task<Stockfish.NET.Stockfish> PlayMove(string move);
    Task<bool> CheckMate();
}