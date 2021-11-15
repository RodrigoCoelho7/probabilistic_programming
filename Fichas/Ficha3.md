# Ficha 3

### 1. Assuma que 1% da população tem COVID. Dos que têm COVID, 70% tem um teste rápido positivo mas 10% das pessoas que não têm COVID tem um teste rápido positivo. Imprima o histograma correspondente aos positivos;

~~~~
var p_C = 0.01 // Probabilidade de ter covid
var p_AC = 0.7 // Probabilidade de teste A sabendo q tem Covid P(A|C)
var p_ANC = 0.1 // Probabilidade de teste A positivo sabendo q nao tem Covid P(A|~C)

var Bool2Text = function(x){return x?"Positivo":"Negativo"}

var model = function(){
  return Bool2Text(flip(p_C) ? flip(p_AC):flip(p_ANC))
}

viz.table(Infer(model))
~~~~

### 2. Assuma agora que existe o teste B (em oposição ao teste A referido acima) em que 90% das pessoas com COVID tem um teste positivo enquanto que só 1% das pessoas sem COVID tem um teste positivo. Assuma também que das pessoas que ligam para o Saúde24, 80% das pessoas fizeram o teste A e as restantes fizeram o teste B. Imprima o histograma correspondente aos positivos.

~~~~
var p_C = 0.01 // Probabilidade de ter covid
var p_AC = 0.7 // Probabilidade de teste A sabendo q tem Covid P(A|C)
var p_ANC = 0.1 // Probabilidade de teste A positivo sabendo q nao tem Covid P(A|~C)
var p_BC = 0.9 // Probabilidade de teste A sabendo q tem Covid P(B|C)
var p_BNC = 0.01 // Probabilidade de teste A positivo sabendo q nao tem Covid P(B|~C)
var p_AL = 0.8 // Probabilidade de ter teste A e ligar a Saude 24 P(A|L)

var Bool2Text = function(x){return x?"Positivo":"Negativo"}

var TestA = function(){
  return Bool2Text(flip(p_C) ? flip(p_AC):flip(p_ANC))
}

var TestB = function(){
  return Bool2Text(flip(p_C) ? flip(p_BC):flip(p_BNC))
}

var model = function(){
  return flip(p_AL) ? TestA():TestB()
}
viz.table(Infer(model))
~~~~

### 3. Calcule p(COVID|positivo) para a pergunta 1 da ficha 3;


~~~~
var p_C = 0.01 // Probabilidade de ter covid
var p_AC = 0.7 // Probabilidade de teste A sabendo q tem Covid P(A|C)
var p_ANC = 0.1 // Probabilidade de teste A positivo sabendo q nao tem Covid P(A|~C)

var model = function(){
  var covid = flip(p_C)
  var positivo = covid ? flip(p_AC):flip(p_ANC)
  condition(positivo)
  return covid
}

viz.table(Infer(model))
~~~~

### 4. Se tiver um teste positivo para a pergunta 2 da ficha 3, calcule:
- A probabilidade de ter COVID;
- A probabilidade de ter feito o teste A;
- A probabilidade de ter feito o teste A com teste positivo e COVID;

~~~~
var p_C = 0.01 // Probabilidade de ter covid
var p_AC = 0.7 // Probabilidade de teste A sabendo q tem Covid P(A|C)
var p_ANC = 0.1 // Probabilidade de teste A positivo sabendo q nao tem Covid P(A|~C)
var p_BC = 0.9 // Probabilidade de teste A sabendo q tem Covid P(B|C)
var p_BNC = 0.01 // Probabilidade de teste A positivo sabendo q nao tem Covid P(B|~C)
var p_AL = 0.8 // Probabilidade de ter teste A e ligar a Saude 24 P(A|L)

var model = function(){
  var feitoA = flip(p_AL)
  var covid = flip(p_C)
  var TestA = covid ? flip(p_AC):flip(p_ANC)
  var TestB = covid ? flip(p_BC):flip(p_BNC)
  var positivo = feitoA ? TestA:TestB
  return {feitoA:feitoA,covid:covid,TestA:TestA,TestB:TestB,positivo:positivo}
}

var CovidPositivo = function(){
  var result = model()
  condition(result["positivo"])
  return result["covid"]
}

console.log("P(Covid|Positivo)")
viz.table(Infer(CovidPositivo))

var FezAPositivo = function(){
  var result = model()
  condition(result["positivo"])
  return result["feitoA"]
}

console.log("P(FezTestA|Positivo)")
viz.table(Infer(FezAPositivo))

var FezAPositivoCovid = function(){
  var result = model()
  condition(result["covid"] && result["positivo"])
  return result["feitoA"]
}

console.log("P(FezTestA|Positivo^Covid)")
viz.table(Infer(FezAPositivoCovid))
~~~~