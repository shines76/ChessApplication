using ChessStockfish;
using Microsoft.Extensions.DependencyInjection;

public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddStockFish(this IServiceCollection services)
    {
        services.AddSingleton<IStockfishService, StockfishService>();
        return services;
    }
}