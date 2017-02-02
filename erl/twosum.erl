-module(twosum).

-export([twosum/2]).


twosum(Sum, []) ->
  false;
twosum(Sum, [Num]) ->
  false;
twosum(Sum, Nums) ->
  case Nums[0] + Nums[-1] of
    A when A > Sum ->
      twosum(Sum, Nums[:-2]);
    A when A < Sum ->
      twosum(Sum, Nums[1:]);
    A ->
      true
  end.
