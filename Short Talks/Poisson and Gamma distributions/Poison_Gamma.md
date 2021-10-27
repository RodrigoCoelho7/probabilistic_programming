~~~~
var Lambda = 10
var p = function(){return poisson(Lambda)}
viz(Poisson({mu:Lambda}))
viz(Infer({method:'rejection',samples:100000},p))
~~~~

~~~~
var Lambda = 10
//Poisson Model
var p = function(){return poisson(Lambda)}

var factorial = function(n){
  return reduce(function(x, acc) {return x*acc}, 1, mapN(function(x){return x+1}, n))
}
//Probability P(X=x) by model
var prob = function(x,N){
  return sum(reduce(function(y,acc){
    if (y==x) return acc.concat(1)
    return acc
  },[],repeat(N,p)))/N
}
//Probability P(X=x) by definition
var p_def = function(x){
  return Math.exp(-Lambda)*Math.pow(Lambda,x)/factorial(x)
}
//Cumulative Probability P(X<=x)
var cp = function(x){
  return sum(mapN(function(x){p_def(x)},x))
}

console.log('Por Iteracao: ',prob(6,100000))
console.log('Por Definicao: ',p_def(6))
console.log('P(x>=12) = ',1 - cp(12))
~~~~

~~~~
var beta = 1/10
var alpha = 20
var g = function(){return gamma({shape:alpha,scale:beta})}
viz(Gamma({shape:alpha,scale:beta}))
viz(Infer({method:'rejection',samples:100000},g))
~~~~