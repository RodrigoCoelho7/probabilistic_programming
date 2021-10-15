# FICHA 1
### Leander Reascos PG47264
#### MEF Fisica da Informacao 

### 1. Escreva funções que lancem uma moeda ao ar n vezes e:
1. Conte quantas vezes saiu cara;
2. Verifique se todos os lançamentos foram coroa;
3. Verifique se nem todos os lançamentos tiveram o mesmo resultado;

~~~~
var make_coin = function(p){
  return function(){
    return flip(p)
  }
}

var flip_coin = make_coin(0.5)

var n = 10000
//Cara = True, Coroa = False
var results = repeat(n,flip_coin)
console.log('1. CARAS: ',sum(results))
console.log('2. Todos os Lancamentos foram Coroa: ',all(function(x){return !x},results))
console.log('3. Todos os Lancamentos foram Iguais: ',all(function(x){return !x},results) || all(function(x){return x},results))
~~~~

### 2. Escreva uma função que lance 1000 vezes uma moeda ao ar, use a função repeat, e crie um histograma com as frequências;

~~~~
var make_coin = function(p){
  return function(){
    return flip(p)
  }
}

var flip_coin = make_coin(0.5)

var n = 1000
var results = map(function(x){if(x){ return 'Cara'} else {return 'Coroa'}},repeat(n,flip_coin))
viz.hist(results)
~~~~

### 3. Modifique a função anterior para receber a probabilidade de sair cara e experimente com vários casos possíveis;


~~~~
var make_coin = function(p){
  return function(){
    return flip(p)
  }
}
var prob = 0.7
var flip_coin = make_coin(prob)
var n = 1000
var results = map(function(x){if(x){ return 'Cara'} else {return 'Coroa'}},repeat(n,flip_coin))
viz.hist(results)
~~~~

### 4. Modifique a função anterior para lançar 5 moedas de cada vez e criar o histograma com o número de caras;
1. Use a função flip para isso;
2. Use outra distribuição que lhe pareça mais útil;

~~~~
var make_coin = function(p){
  return function(){
    return flip(p)
  }
}
var prob = 0.7
var flip_coin = make_coin(prob)
var n = 1000
var results = map(function(x){if(x){ return 'Cara'} else {return 'Coroa'}},repeat(n,flip_coin))
console.log('COM FLIP')
viz.hist(results)  
var num_True = binomial({p: prob,n: n})
var f = function(x){
  if (x < num_True){
    return 'Cara'
  }
  else{
    return 'Coroa'
  }
}
var results2 = mapN(f,n)
console.log('COM DIST BINOMIAL')
viz.hist(results2)
~~~~

### 5. Crie um histograma correspondente ao lançamento de um dado;

~~~~
var num_faces = 6
var make_dice = function(ps){
  return function() {return discrete({ps:ps})+1}
}
var dice = make_dice(repeat(num_faces,function(){return 1/num_faces}))
var n = 10000
var results = repeat(n,dice)
viz.hist(results)
~~~~

### 6. Modifique o programa anterior para lançar mais do que um dado;


~~~~
var num_faces = 6
var make_dice = function(ps){
  return function() {return discrete({ps:ps})+1}
}
var dice1 = make_dice(repeat(num_faces,function(){return 1/num_faces}))
var dice2 = make_dice(repeat(num_faces,function(){return 1/num_faces}))
var n = 10000
var results1 = repeat(n,dice1)
var results2 = repeat(n,dice2)
viz(map2(function(a,b){return a+b}, results2, results1))
~~~~

### 7. Faça uma função para sortear uma carta;


~~~~
var get_card = function(){
  var cartas = (['A'].concat(mapN(function(x){(x+2).toString()}, 9))).concat(['J','Q','K'])
  var palos = ['C','P','E','O'] // Copas, Paus, Espadas, Ouros
  var carta = discrete({ps:repeat(cartas.length ,function(){return 1/cartas.length})})
  var palo = discrete({ps:repeat(palos.length ,function(){return 1/palos.length})})
  return cartas[carta].concat(palos[palo])
}
var n = 10000
var results = repeat(n,get_card)

viz(results)
Infer(get_card)
~~~~

### 8. Faça uma função que sorteie uma mão de n cartas.


~~~~
var get_card = function(){
  var cartas = (['A'].concat(mapN(function(x){(x+2).toString()}, 9))).concat(['J','Q','K'])
  var palos = ['C','P','E','O'] // Copas, Paus, Espadas, Ouros
  var carta = discrete({ps:repeat(cartas.length ,function(){return 1/cartas.length})})
  var palo = discrete({ps:repeat(palos.length ,function(){return 1/palos.length})})
  return cartas[carta].concat(palos[palo])
}

var hand = function(l,n){
  if (n == 0) return l
  var card = get_card()
  if (any(function(x){x==card},l)) return hand(l,n)
  else return hand(l.concat(card),n-1)
}
var n = 5
var results = hand([],n)
console.log('As cartas sao: ', results)
~~~~