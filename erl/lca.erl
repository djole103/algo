-module(lca).


-record(node, {val, left, right}).

-export([lca/3, test_lca/0]).

lca(undefined, _Node1, _Node2) ->
  no_lca;
lca(Root, Node1, _Node2) when Root#node.val =:= Node1#node.val ->
  Node1;
lca(Root, _Node1, Node2) when Root#node.val =:= Node2#node.val ->
  Node2;
lca(Root, Node1, Node2) ->
  lca(Root#node.left, Node1, Node2) || lca(Root#node.right, Node1, Node2).


test_lca() ->
  Node1 = #node{val = 1},
  Node2 = #node{val = 2},
  Node3 = #node{val = 3, left = Node2, right = Node1},
  Node4 = #node{val = 4},
  Node5 = #node{val = 5, left = Node3},
  Node6 = #node{val = 6, left = Node5, right = Node4},
  
  Test1 = lca(Node6, Node1, Node2),
  ct:pal("~p", [Test1]).
