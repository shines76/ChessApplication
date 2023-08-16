

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddStockFish();

var app = builder.Build();
var stockfish = app.Services.GetRequiredService<IStockfishService>();

var test = await stockfish.Start("white");

app.MapGet("/", () => "Hello World!");

app.Run();
