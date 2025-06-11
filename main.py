from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora DZX-CORE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        h1 { color: #333; margin-bottom: 1rem; }
        .subtitle { color: #666; margin-bottom: 2rem; }
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 1rem;
        }
        input {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        .buttons {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 1rem;
        }
        button {
            padding: 15px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            background: #4CAF50;
            color: white;
        }
        button:hover {
            background: #45a049;
            transform: translateY(-2px);
        }
        #resultado {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #4CAF50;
            margin: 1rem 0;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .footer {
            margin-top: 1rem;
            color: #888;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 Calculadora DZX-CORE</h1>
        <p class="subtitle">Criada pelo orquestrador inteligente</p>
        
        <div class="input-group">
            <input type="number" id="num1" placeholder="Número 1" step="any">
            <input type="number" id="num2" placeholder="Número 2" step="any">
        </div>
        
        <div class="buttons">
            <button onclick="calcular('+')">+ Somar</button>
            <button onclick="calcular('-')">- Subtrair</button>
            <button onclick="calcular('*')">× Multiplicar</button>
            <button onclick="calcular('/')">> Dividir</button>
            <button onclick="calcularPotencia()">^ Potência</button>
            <button onclick="calcularRaiz()">√ Raiz</button>
            <button onclick="calcularFatorial()">! Fatorial</button>
            <button onclick="limpar()">🗑 Limpar</button>
        </div>
        
        <div id="resultado">Digite os números e escolha uma operação</div>
        
        <div class="footer">Powered by DZX-CORE</div>
    </div>
    
    <script>
        function calcular(op) {
            const n1 = parseFloat(document.getElementById('num1').value);
            const n2 = parseFloat(document.getElementById('num2').value);
            
            if (isNaN(n1) || isNaN(n2)) {
                mostrarResultado('Por favor, digite números válidos');
                return;
            }
            
            let resultado;
            switch(op) {
                case '+': resultado = n1 + n2; break;
                case '-': resultado = n1 - n2; break;
                case '*': resultado = n1 * n2; break;
                case '/': 
                    if (n2 === 0) {
                        mostrarResultado('Erro: Divisão por zero');
                        return;
                    }
                    resultado = n1 / n2;
                    break;
            }
            
            mostrarResultado(`${n1} ${op} ${n2} = ${resultado}`);
        }
        
        function calcularPotencia() {
            const base = parseFloat(document.getElementById('num1').value);
            const exp = parseFloat(document.getElementById('num2').value);
            
            if (isNaN(base) || isNaN(exp)) {
                mostrarResultado('Digite base e expoente');
                return;
            }
            
            const resultado = Math.pow(base, exp);
            mostrarResultado(`${base}^${exp} = ${resultado}`);
        }
        
        function calcularRaiz() {
            const num = parseFloat(document.getElementById('num1').value);
            
            if (isNaN(num)) {
                mostrarResultado('Digite um número no primeiro campo');
                return;
            }
            
            if (num < 0) {
                mostrarResultado('Erro: Raiz de número negativo');
                return;
            }
            
            const resultado = Math.sqrt(num);
            mostrarResultado(`√${num} = ${resultado}`);
        }
        
        function calcularFatorial() {
            const num = parseInt(document.getElementById('num1').value);
            
            if (isNaN(num) || num < 0 || num > 20) {
                mostrarResultado('Digite um número inteiro entre 0 e 20');
                return;
            }
            
            let resultado = 1;
            for (let i = 2; i <= num; i++) {
                resultado *= i;
            }
            
            mostrarResultado(`${num}! = ${resultado}`);
        }
        
        function limpar() {
            document.getElementById('num1').value = '';
            document.getElementById('num2').value = '';
            mostrarResultado('Campos limpos');
        }
        
        function mostrarResultado(texto) {
            document.getElementById('resultado').innerHTML = texto;
        }
    </script>
</body>
</html>
""")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
