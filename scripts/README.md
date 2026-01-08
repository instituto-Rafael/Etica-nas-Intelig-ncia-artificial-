# Scripts - RAFAELIA

## Biblioteca Matemática Avançada

Este diretório contém scripts e utilitários do sistema RAFAELIA.

### matematica.py

Biblioteca matemática com **69 operações** divididas em 5 categorias:

#### 1. Derivadas Diretas (1-15)
- Polinomiais, exponenciais, logarítmicas
- Trigonométricas: seno, cosseno, tangente, cotangente, secante, cossecante
- Arco-trigonométricas: arcsin, arccos, arctan
- Hiperbólicas: sinh, cosh
- Regra do produto

#### 2. Antiderivadas/Integrais (16-30)
- Integrais de funções elementares
- Métodos numéricos: Simpson, Trapézio
- Integração por partes
- Integral gaussiana

#### 3. Funções Inversas (31-45)
- Inversas algébricas: linear, quadrática, potência
- Inversas transcendentais: exponencial, logarítmica
- Inversas trigonométricas e hiperbólicas
- Método de Newton-Raphson para inversas numéricas

#### 4. Funções Reversas (46-60)
- Reversas de estruturas: listas, strings, bits, matrizes
- Reversas de operações matemáticas
- Transformadas inversas: FFT, Laplace
- Des-normalização e des-padronização

#### 5. Transformações Diretas (61-69)
- Fourier Discreta (DFT)
- Laplace e Z-transform
- Wavelet de Haar
- Box-Cox, Logit, Sigmoid, Softmax
- Conversão polar-cartesiana

### Uso

```python
from scripts.matematica import Matematica

mat = Matematica()

# Exemplo: calcular derivada
resultado = mat.derivada_polinomial([0, 0, 1], 3)  # derivada de x² em x=3
print(resultado)  # Output: 6

# Exemplo: calcular integral
resultado = mat.integral_seno(math.pi)
print(resultado)  # Output: 1.0

# Exemplo: função inversa
resultado = mat.inversa_linear(2, 3, 10)  # resolver 2x+3=10
print(resultado)  # Output: 3.5
```

### Demonstração

Execute o script diretamente para ver demonstração de todas as operações:

```bash
python scripts/matematica.py
```

### Características

- ✅ 69 operações matemáticas implementadas
- ✅ Métodos numéricos robustos
- ✅ Sistema de histórico auditável
- ✅ Assinatura digital: RAFCODE_𝚽
- ✅ Código limpo e documentado

### Licença

Todos os direitos reservados © Rafael ∞ Verbo Vivo

---

**Autor:** Rafael ∞ Verbo Vivo  
**Contato:** rafaelmeloReisnovo@gmail.com  
**Assinatura:** RAFCODE_𝚽
