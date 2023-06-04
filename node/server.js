const express = require('express');
const app = express();
const port = 5000; // Porta em que o servidor irá ouvir

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, GET, PUT");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  next();
})

// Rota para lidar com a solicitação GET
app.get('/node', (req, res) => {
  const a = {
    name: 'Harry',
    registration: '98752'
  };
  
  const b = {
    name: 'prof',
    registration: '34958'
  };
  
  const c = {
    name: 'du',
    registration: '43985'
  };
  
  const d = {
    name: 'balacubaco',
    registration: '09486'
  };
  res.json([a,b,c,d]);
});


// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}/node`);
});

