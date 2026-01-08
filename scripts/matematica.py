"""
RAFAELIA - Biblioteca Matemática Avançada
==========================================

Este módulo contém 69 operações matemáticas incluindo:
- Derivadas diretas
- Antiderivadas (integrais)
- Funções inversas
- Funções reversas
- Transformações matemáticas

Autor: Rafael ∞ Verbo Vivo
Licença: Todos os direitos reservados
Assinatura: RAFCODE_𝚽
"""

import math
from typing import Callable, Union, Tuple, Any


class Matematica:
    """Classe principal com operações matemáticas avançadas."""
    
    def __init__(self):
        self.historico = []
        self.precisao = 1e-10
    
    # ==========================================
    # SEÇÃO 1: DERIVADAS DIRETAS (1-15)
    # ==========================================
    
    def derivada_polinomial(self, coeficientes: list, x: float) -> float:
        """1. Derivada de polinômio: d/dx(a_n*x^n + ... + a_1*x + a_0)"""
        resultado = 0
        for i, coef in enumerate(coeficientes[1:], 1):
            resultado += i * coef * (x ** (i - 1))
        return resultado
    
    def derivada_exponencial(self, base: float, x: float) -> float:
        """2. Derivada de exponencial: d/dx(base^x) = base^x * ln(base)"""
        return (base ** x) * math.log(base)
    
    def derivada_logaritmica(self, base: float, x: float) -> float:
        """3. Derivada logarítmica: d/dx(log_base(x)) = 1/(x*ln(base))"""
        return 1 / (x * math.log(base))
    
    def derivada_seno(self, x: float) -> float:
        """4. Derivada do seno: d/dx(sin(x)) = cos(x)"""
        return math.cos(x)
    
    def derivada_cosseno(self, x: float) -> float:
        """5. Derivada do cosseno: d/dx(cos(x)) = -sin(x)"""
        return -math.sin(x)
    
    def derivada_tangente(self, x: float) -> float:
        """6. Derivada da tangente: d/dx(tan(x)) = sec²(x)"""
        return 1 / (math.cos(x) ** 2)
    
    def derivada_cotangente(self, x: float) -> float:
        """7. Derivada da cotangente: d/dx(cot(x)) = -csc²(x)"""
        return -1 / (math.sin(x) ** 2)
    
    def derivada_secante(self, x: float) -> float:
        """8. Derivada da secante: d/dx(sec(x)) = sec(x)*tan(x)"""
        return (1 / math.cos(x)) * math.tan(x)
    
    def derivada_cossecante(self, x: float) -> float:
        """9. Derivada da cossecante: d/dx(csc(x)) = -csc(x)*cot(x)"""
        return -(1 / math.sin(x)) * (math.cos(x) / math.sin(x))
    
    def derivada_arco_seno(self, x: float) -> float:
        """10. Derivada do arco seno: d/dx(arcsin(x)) = 1/sqrt(1-x²)"""
        return 1 / math.sqrt(1 - x**2)
    
    def derivada_arco_cosseno(self, x: float) -> float:
        """11. Derivada do arco cosseno: d/dx(arccos(x)) = -1/sqrt(1-x²)"""
        return -1 / math.sqrt(1 - x**2)
    
    def derivada_arco_tangente(self, x: float) -> float:
        """12. Derivada do arco tangente: d/dx(arctan(x)) = 1/(1+x²)"""
        return 1 / (1 + x**2)
    
    def derivada_hiperbolica_seno(self, x: float) -> float:
        """13. Derivada do seno hiperbólico: d/dx(sinh(x)) = cosh(x)"""
        return math.cosh(x)
    
    def derivada_hiperbolica_cosseno(self, x: float) -> float:
        """14. Derivada do cosseno hiperbólico: d/dx(cosh(x)) = sinh(x)"""
        return math.sinh(x)
    
    def derivada_produto(self, f: Callable, g: Callable, x: float, h: float = 1e-7) -> float:
        """15. Regra do produto: d/dx(f*g) = f'*g + f*g'"""
        f_derivada = (f(x + h) - f(x)) / h
        g_derivada = (g(x + h) - g(x)) / h
        return f_derivada * g(x) + f(x) * g_derivada
    
    # ==========================================
    # SEÇÃO 2: ANTIDERIVADAS/INTEGRAIS (16-30)
    # ==========================================
    
    def integral_polinomial(self, coeficientes: list, x: float) -> float:
        """16. Integral de polinômio: ∫(a_n*x^n + ...)dx"""
        resultado = 0
        for i, coef in enumerate(coeficientes):
            resultado += coef * (x ** (i + 1)) / (i + 1)
        return resultado
    
    def integral_exponencial(self, base: float, x: float) -> float:
        """17. Integral de exponencial: ∫base^x dx = base^x/ln(base)"""
        return (base ** x) / math.log(base)
    
    def integral_logaritmica(self, x: float) -> float:
        """18. Integral logarítmica: ∫ln(x)dx = x*ln(x) - x"""
        return x * math.log(x) - x
    
    def integral_seno(self, x: float) -> float:
        """19. Integral do seno: ∫sin(x)dx = -cos(x)"""
        return -math.cos(x)
    
    def integral_cosseno(self, x: float) -> float:
        """20. Integral do cosseno: ∫cos(x)dx = sin(x)"""
        return math.sin(x)
    
    def integral_tangente(self, x: float) -> float:
        """21. Integral da tangente: ∫tan(x)dx = -ln|cos(x)|"""
        return -math.log(abs(math.cos(x)))
    
    def integral_secante_quadrado(self, x: float) -> float:
        """22. Integral de sec²: ∫sec²(x)dx = tan(x)"""
        return math.tan(x)
    
    def integral_racional_simples(self, x: float) -> float:
        """23. Integral de 1/x: ∫(1/x)dx = ln|x|"""
        return math.log(abs(x))
    
    def integral_numerica_simpson(self, f: Callable, a: float, b: float, n: int = 100) -> float:
        """24. Integral numérica (Regra de Simpson)"""
        if n % 2 == 1:
            n += 1
        h = (b - a) / n
        soma = f(a) + f(b)
        for i in range(1, n):
            x = a + i * h
            soma += (2 if i % 2 == 0 else 4) * f(x)
        return (h / 3) * soma
    
    def integral_numerica_trapezio(self, f: Callable, a: float, b: float, n: int = 100) -> float:
        """25. Integral numérica (Regra do trapézio)"""
        h = (b - a) / n
        soma = (f(a) + f(b)) / 2
        for i in range(1, n):
            soma += f(a + i * h)
        return h * soma
    
    def integral_por_partes(self, u: Callable, dv: Callable, x: float, h: float = 1e-7) -> float:
        """26. Integração por partes: ∫u*dv = u*v - ∫v*du"""
        # Aproximação numérica
        v = lambda t: self.integral_numerica_trapezio(dv, 0, t, 50)
        du = lambda t: (u(t + h) - u(t)) / h
        termo1 = u(x) * v(x)
        termo2 = self.integral_numerica_trapezio(lambda t: v(t) * du(t), 0, x, 50)
        return termo1 - termo2
    
    def integral_senh(self, x: float) -> float:
        """27. Integral de sinh: ∫sinh(x)dx = cosh(x)"""
        return math.cosh(x)
    
    def integral_cosh(self, x: float) -> float:
        """28. Integral de cosh: ∫cosh(x)dx = sinh(x)"""
        return math.sinh(x)
    
    def integral_arctan(self, x: float) -> float:
        """29. Integral de arctan: ∫arctan(x)dx = x*arctan(x) - ln(1+x²)/2"""
        return x * math.atan(x) - math.log(1 + x**2) / 2
    
    def integral_gaussiana(self, x: float, mu: float = 0, sigma: float = 1) -> float:
        """30. Integral gaussiana aproximada usando erf"""
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
    
    # ==========================================
    # SEÇÃO 3: FUNÇÕES INVERSAS (31-45)
    # ==========================================
    
    def inversa_linear(self, m: float, b: float, y: float) -> float:
        """31. Inversa de f(x)=mx+b: x = (y-b)/m"""
        return (y - b) / m
    
    def inversa_quadratica(self, a: float, b: float, c: float, y: float) -> Tuple[float, float]:
        """32. Inversa de f(x)=ax²+bx+c usando fórmula de Bhaskara"""
        discriminante = b**2 - 4*a*(c - y)
        if discriminante < 0:
            raise ValueError("Não há raízes reais")
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (raiz1, raiz2)
    
    def inversa_exponencial(self, base: float, y: float) -> float:
        """33. Inversa de f(x)=base^x: x = log_base(y)"""
        return math.log(y) / math.log(base)
    
    def inversa_logaritmica(self, base: float, y: float) -> float:
        """34. Inversa de f(x)=log_base(x): x = base^y"""
        return base ** y
    
    def inversa_seno(self, y: float) -> float:
        """35. Inversa do seno: arcsin(y)"""
        return math.asin(y)
    
    def inversa_cosseno(self, y: float) -> float:
        """36. Inversa do cosseno: arccos(y)"""
        return math.acos(y)
    
    def inversa_tangente(self, y: float) -> float:
        """37. Inversa da tangente: arctan(y)"""
        return math.atan(y)
    
    def inversa_senh(self, y: float) -> float:
        """38. Inversa do senh: arcsinh(y) = ln(y + sqrt(y²+1))"""
        return math.log(y + math.sqrt(y**2 + 1))
    
    def inversa_cosh(self, y: float) -> float:
        """39. Inversa do cosh: arccosh(y) = ln(y + sqrt(y²-1))"""
        if y < 1:
            raise ValueError("cosh inverso requer y >= 1")
        return math.log(y + math.sqrt(y**2 - 1))
    
    def inversa_tanh(self, y: float) -> float:
        """40. Inversa da tanh: arctanh(y) = 0.5*ln((1+y)/(1-y))"""
        if abs(y) >= 1:
            raise ValueError("tanh inverso requer |y| < 1")
        return 0.5 * math.log((1 + y) / (1 - y))
    
    def inversa_newton_raphson(self, f: Callable, f_derivada: Callable, y: float, 
                               x0: float = 1.0, max_iter: int = 100) -> float:
        """41. Inversa numérica usando Newton-Raphson"""
        x = x0
        for _ in range(max_iter):
            fx = f(x) - y
            if abs(fx) < self.precisao:
                return x
            fpx = f_derivada(x)
            if abs(fpx) < self.precisao:
                raise ValueError("Derivada muito próxima de zero")
            x = x - fx / fpx
        return x
    
    def inversa_potencia(self, n: float, y: float) -> float:
        """42. Inversa de f(x)=x^n: x = y^(1/n)"""
        return y ** (1/n)
    
    def inversa_raiz(self, n: float, y: float) -> float:
        """43. Inversa de f(x)=√x: x = y^n"""
        return y ** n
    
    def inversa_reciproca(self, y: float) -> float:
        """44. Inversa de f(x)=1/x: x = 1/y"""
        return 1 / y
    
    def inversa_composta(self, f_inv: Callable, g_inv: Callable, y: float) -> float:
        """45. Inversa de composição f∘g: (f∘g)⁻¹ = g⁻¹∘f⁻¹"""
        return g_inv(f_inv(y))
    
    # ==========================================
    # SEÇÃO 4: FUNÇÕES REVERSAS (46-60)
    # ==========================================
    
    def reversa_lista(self, lista: list) -> list:
        """46. Reverter ordem de lista"""
        return lista[::-1]
    
    def reversa_string(self, s: str) -> str:
        """47. Reverter string"""
        return s[::-1]
    
    def reversa_bits(self, n: int, bits: int = 32) -> int:
        """48. Reverter bits de um inteiro"""
        resultado = 0
        for i in range(bits):
            if n & (1 << i):
                resultado |= (1 << (bits - 1 - i))
        return resultado
    
    def reversa_matriz(self, matriz: list) -> list:
        """49. Transposta de matriz (reversa dimensional)"""
        return [[matriz[j][i] for j in range(len(matriz))] 
                for i in range(len(matriz[0]))]
    
    def reversa_operacao(self, operacao: str, a: float, b: float) -> float:
        """50. Operação reversa (inversa operacional)"""
        ops_reversas = {
            '+': lambda x, y: x - y,
            '-': lambda x, y: x + y,
            '*': lambda x, y: x / y if y != 0 else float('inf'),
            '/': lambda x, y: x * y,
            '**': lambda x, y: x ** (1/y) if y != 0 else 1
        }
        return ops_reversas.get(operacao, lambda x, y: 0)(a, b)
    
    def reversa_fft(self, dados_freq: list) -> list:
        """51. FFT inversa (transformada de Fourier reversa)"""
        # Implementação simplificada usando DFT
        n = len(dados_freq)
        resultado = [0] * n
        for k in range(n):
            soma = 0
            for t in range(n):
                angulo = 2 * math.pi * t * k / n
                soma += dados_freq[t] * complex(math.cos(angulo), math.sin(angulo))
            resultado[k] = soma / n
        return resultado
    
    def reversa_derivada(self, derivada: Callable, x0: float, C: float = 0) -> Callable:
        """52. Antiderivada (reversa da derivada)"""
        return lambda x: self.integral_numerica_simpson(derivada, x0, x, 100) + C
    
    def reversa_laplace(self, s: float, tempo: float) -> float:
        """53. Transformada inversa de Laplace (simplificada)"""
        # Implementação básica para exponencial
        return math.exp(-s * tempo)
    
    def reversa_logaritmo(self, base: float, log_valor: float) -> float:
        """54. Reversa do log: antilog (exponenciação)"""
        return base ** log_valor
    
    def reversa_codificacao(self, bits: str) -> int:
        """55. Decodificar bits para inteiro"""
        return int(bits, 2)
    
    def reversa_normalizacao(self, valor_norm: float, minimo: float, maximo: float) -> float:
        """56. Des-normalizar valor: x = valor_norm*(max-min) + min"""
        return valor_norm * (maximo - minimo) + minimo
    
    def reversa_padronizacao(self, z: float, media: float, desvio: float) -> float:
        """57. Des-padronizar (z-score reverso): x = z*σ + μ"""
        return z * desvio + media
    
    def reversa_diferenca(self, diferencas: list, valor_inicial: float) -> list:
        """58. Integrar diferenças para recuperar série original"""
        resultado = [valor_inicial]
        for diff in diferencas:
            resultado.append(resultado[-1] + diff)
        return resultado
    
    def reversa_hash_aproximado(self, hash_val: int, universo: list) -> list:
        """59. Busca por força bruta de possíveis originais de hash"""
        candidatos = []
        for item in universo:
            if hash(item) == hash_val:
                candidatos.append(item)
        return candidatos
    
    def reversa_convolucao(self, resultado: list, kernel: list) -> list:
        """60. Deconvolução (reversa da convolução)"""
        # Implementação simplificada no domínio da frequência
        n = len(resultado)
        return [resultado[i] / (kernel[i % len(kernel)] if kernel[i % len(kernel)] != 0 else 1) 
                for i in range(n)]
    
    # ==========================================
    # SEÇÃO 5: TRANSFORMAÇÕES DIRETAS (61-69)
    # ==========================================
    
    def transformada_fourier_discreta(self, dados: list) -> list:
        """61. DFT - Transformada de Fourier Discreta"""
        n = len(dados)
        resultado = []
        for k in range(n):
            soma = 0
            for t in range(n):
                angulo = -2 * math.pi * t * k / n
                soma += dados[t] * complex(math.cos(angulo), math.sin(angulo))
            resultado.append(soma)
        return resultado
    
    def transformada_laplace(self, f: Callable, s: float, t_max: float = 10) -> float:
        """62. Transformada de Laplace aproximada"""
        return self.integral_numerica_simpson(
            lambda t: f(t) * math.exp(-s * t), 0, t_max, 100
        )
    
    def transformada_z(self, sequencia: list, z: complex) -> complex:
        """63. Transformada Z"""
        resultado = complex(0)
        for n, valor in enumerate(sequencia):
            resultado += valor * (z ** (-n))
        return resultado
    
    def transformada_wavelet_haar(self, dados: list) -> Tuple[list, list]:
        """64. Transformada Wavelet de Haar (1 nível)"""
        n = len(dados)
        if n % 2 != 0:
            raise ValueError("Dados devem ter comprimento par para Wavelet de Haar")
        aproximacao = [(dados[i] + dados[i+1]) / math.sqrt(2) for i in range(0, n, 2)]
        detalhe = [(dados[i] - dados[i+1]) / math.sqrt(2) for i in range(0, n, 2)]
        return aproximacao, detalhe
    
    def transformada_box_cox(self, x: float, lambda_param: float) -> float:
        """65. Transformada de Box-Cox"""
        if x <= 0:
            raise ValueError("Box-Cox requer x > 0")
        if lambda_param == 0:
            return math.log(x)
        return (x ** lambda_param - 1) / lambda_param
    
    def transformada_logit(self, p: float) -> float:
        """66. Transformação logit: log(p/(1-p))"""
        if p <= 0 or p >= 1:
            raise ValueError("p deve estar entre 0 e 1")
        return math.log(p / (1 - p))
    
    def transformada_sigmoid(self, x: float) -> float:
        """67. Função sigmoid (inversa do logit): 1/(1+e^(-x))"""
        return 1 / (1 + math.exp(-x))
    
    def transformada_softmax(self, valores: list) -> list:
        """68. Transformação softmax"""
        exp_valores = [math.exp(v) for v in valores]
        soma = sum(exp_valores)
        return [v / soma for v in exp_valores]
    
    def transformada_polar_cartesiana(self, r: float, theta: float) -> Tuple[float, float]:
        """69. Coordenadas polares para cartesianas"""
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return (x, y)
    
    # ==========================================
    # MÉTODOS AUXILIARES
    # ==========================================
    
    def registrar_operacao(self, nome: str, resultado: Any):
        """Registra operação no histórico para auditoria"""
        self.historico.append({
            'operacao': nome,
            'resultado': resultado,
            'assinatura': 'RAFCODE_𝚽'
        })
    
    def limpar_historico(self):
        """Limpa histórico de operações"""
        self.historico = []
    
    def obter_historico(self) -> list:
        """Retorna histórico de operações"""
        return self.historico


# ==========================================
# FUNÇÕES AUXILIARES E EXEMPLOS DE USO
# ==========================================

def demonstracao():
    """Demonstra o uso das 69 operações matemáticas"""
    mat = Matematica()
    
    print("=" * 60)
    print("RAFAELIA - Demonstração de Operações Matemáticas")
    print("=" * 60)
    
    # Exemplos de derivadas
    print("\n1. DERIVADAS:")
    print(f"   Derivada de x² em x=3: {mat.derivada_polinomial([0, 0, 1], 3)}")
    print(f"   Derivada de sin(π/4): {mat.derivada_seno(math.pi/4):.4f}")
    
    # Exemplos de integrais
    print("\n2. INTEGRAIS:")
    print(f"   Integral de x² de 0 a 1: {mat.integral_polinomial([0, 0, 1], 1):.4f}")
    print(f"   Integral de sin(x) em π: {mat.integral_seno(math.pi):.4f}")
    
    # Exemplos de inversas
    print("\n3. FUNÇÕES INVERSAS:")
    print(f"   Inversa de 2x+3=10: x = {mat.inversa_linear(2, 3, 10)}")
    print(f"   Inversa de e^x=10: x = {mat.inversa_exponencial(math.e, 10):.4f}")
    
    # Exemplos de reversas
    print("\n4. FUNÇÕES REVERSAS:")
    print(f"   Reversa de [1,2,3,4]: {mat.reversa_lista([1,2,3,4])}")
    print(f"   Reversa de 'RAFAELIA': {mat.reversa_string('RAFAELIA')}")
    
    # Exemplos de transformadas
    print("\n5. TRANSFORMADAS:")
    print(f"   Sigmoid de 0: {mat.transformada_sigmoid(0):.4f}")
    print(f"   Softmax de [1,2,3]: {[f'{v:.4f}' for v in mat.transformada_softmax([1,2,3])]}")
    
    print("\n" + "=" * 60)
    print("Total: 69 operações matemáticas implementadas")
    print("Assinatura: RAFCODE_𝚽")
    print("=" * 60)


if __name__ == "__main__":
    demonstracao()
