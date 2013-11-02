-module(math).

-export([factorial/1]).


factorial(N) when N == 0 -> 1;
factorial(N) when N > 0 -> factorial(N - 1) * N.