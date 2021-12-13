# Ficha 4

### 1. Crie uma função sondagens(tamanho) que gere sondagens baseada nas probabilidades dadas abaixo

~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var sondagens = function(N,l){
  if (N == 0){return l}
  var vote = function(){categorical({ps:map(function(x){x/100},_.values(perc)),vs:_.keys(perc)})}
  return sondagens(N-1,l.concat(vote()))
}

viz.table(sondagens(10000,[]))
~~~~

### 2. Utilizando os resultados da sondagem, crie um modelo para as probabilidades de um eleitor votar em cada partido

~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var sondagens = function(N,l){
  if (N == 0){return l}
  var vote = function(){categorical({ps:map(function(x){x/100},_.values(perc)),vs:_.keys(perc)})}
  return sondagens(N-1,l.concat(vote()))
}

var probabilities = function(N){
  var probs = repeat(N,function(){uniform({a:0,b:1})})
  return map(function(x){x/sum(probs)},probs)
}

var count_from_values = function(values,list,counts,i){
  if (i == values.length){return counts}
  var count = sum(map(function(x){x == values[i]},filter(function(x){x == values[i]},list)))
  return count_from_values(values,list,counts.concat(count),i+1)
}


var model = function(obs){
  var probs = probabilities(_.values(perc).length)
  observe(Multinomial({ps:probs,n:sum(_.values(obs))}),_.values(obs))
  return _.fromPairs(_.zip(_.keys(obs),probs))
}

var votes = sondagens(10000,[])
var counts = count_from_values(_.keys(perc),votes,[],0)
var dic = _.fromPairs(_.zip(_.keys(perc),counts))

viz.marginals(Infer({method:'MCMC',samples:10000},function(){model(dic)}))
~~~~

### 4. Use o estimador do High Density Interval para estimar o intervalo da probabilidade para cada partido



~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var sondagens = function(N,l){
  if (N == 0){return l}
  var vote = function(){categorical({ps:map(function(x){x/100},_.values(perc)),vs:_.keys(perc)})}
  return sondagens(N-1,l.concat(vote()))
}

var probabilities = function(N){
  var probs = repeat(N,function(){uniform({a:0,b:1})})
  return map(function(x){x/sum(probs)},probs)
}

var count_from_values = function(values,list,counts,i){
  if (i == values.length){return counts}
  var count = sum(map(function(x){x == values[i]},filter(function(x){x == values[i]},list)))
  return count_from_values(values,list,counts.concat(count),i+1)
}


var model = function(obs){
  var probs = probabilities(_.values(perc).length)
  observe(Multinomial({ps:probs,n:sum(_.values(obs))}),_.values(obs))
  return _.fromPairs(_.zip(_.keys(obs),probs))
}

var votes = sondagens(2500,[])
var counts = count_from_values(_.keys(perc),votes,[],0)
var dic = _.fromPairs(_.zip(_.keys(perc),counts))

var estimar_intervalo = function(dist, margem, low, high) {
  expectation(marginalize(dist, margem), function(p) {low < p && p < high})
}

var HDI = function(dist, margem, low, high, delta) {
  var p = estimar_intervalo(dist, margem, low, high)
  if (p <= 0.95) return [low, high]
  var A  = estimar_intervalo(dist, margem, low + delta, high)
  var B  = estimar_intervalo(dist, margem, low, high - delta)
  return A > B ? HDI(dist, margem, low + delta, high, delta) : HDI(dist, margem, low, high - delta, delta)
}

var print_intervals = function(dist, margens) {
  map(function(m) {
    print(m + ": " + HDI(dist, m, 0, 1, 0.005))
  }, margens) 
}

var votes = sondagens(10000,[])
var counts = count_from_values(_.keys(perc),votes,[],0)
var dic = _.fromPairs(_.zip(_.keys(perc),counts))

var dist = Infer({method:'MCMC',samples:10000},function(){model(dic)})
var dummy = print_intervals(dist, _.keys(dic))
~~~~