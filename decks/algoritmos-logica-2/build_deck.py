import os
import re
import shutil

base_path = '/home/namerico/meus-slides'
template_path = os.path.join(base_path, '.agents/skills/mira-builder/templates')
videos_path  = os.path.join(base_path, 'mira-templates/videos_header')
logo_src     = os.path.join(base_path, 'logo_canal/canal_sandeco_logo.png')
deck_path    = os.path.join(base_path, 'decks/algoritmos-logica-2')
output_file  = os.path.join(deck_path, 'index.html')

# === ASSETS ===
# Vídeo escolhido: 11.mp4 — "cascata de código estilo Matrix" — perfeito para programação
shutil.copy(os.path.join(videos_path, '11.mp4'), os.path.join(deck_path, 'header-bg.mp4'))
shutil.copy(logo_src, os.path.join(deck_path, 'canal_sandeco_logo.png'))
print("Assets copiados.")

# === CARREGA LAYOUT BASE ===
with open(os.path.join(template_path, 'layout_base.html'), 'r', encoding='utf-8') as f:
    layout_base = f.read()

layout_start, layout_end = layout_base.split('<body class="font-sans">')
layout_start = layout_start.replace('[TITULO_DA_PAGINA]', 'Algoritmos e Lógica de Programação II — Slides Interativos')

# === CARREGA HEADER ===
with open(os.path.join(template_path, 'header.html'), 'r', encoding='utf-8') as f:
    header = f.read()

header = header.replace('[TIPO_CONTEUDO]', 'Material de Aula · Faculdade Católica')
header = header.replace('[TITULO_PRINCIPAL]', 'Algoritmos & Lógica de Programação II')
header = header.replace('[SUBTITULO]', 'Do pseudocódigo ao Python real: domine estruturas, coleções e modularização com clareza e prática.')
header = header.replace('canal_sandeco_logo.png', 'canal_sandeco_logo.png')

# === CARDS ===
cards_html = []

# -----------------------------------------------------------------------
# SLIDE 1 — card_grid: O Mapa da Jornada (abertura impactante)
# -----------------------------------------------------------------------
card_grid_tpl = open(os.path.join(template_path, 'card_grid.html'), encoding='utf-8').read()
slide1 = """<!-- SLIDE 1: Grade de pilares do curso -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="100">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="map" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">4 Pilares Que Vão Mudar Seu Código</h3>
            <p class="text-white/50 text-sm italic">Do básico ao avançado — do algoritmo ao objeto</p>
        </div>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
        <div class="glass-card rounded-xl p-5 text-center border-t-2 border-t-[#FF904D]">
            <i data-lucide="cpu" class="w-8 h-8 primary-color mx-auto mb-3"></i>
            <h4 class="font-bold text-white mb-1">Fundamentos</h4>
            <p class="text-white/60 text-xs">Variáveis, tipos, operadores e controle de fluxo</p>
        </div>
        <div class="glass-card rounded-xl p-5 text-center border-t-2 border-t-[#FF904D]">
            <i data-lucide="repeat" class="w-8 h-8 primary-color mx-auto mb-3"></i>
            <h4 class="font-bold text-white mb-1">Repetição</h4>
            <p class="text-white/60 text-xs">while, for e range para automatizar qualquer tarefa</p>
        </div>
        <div class="glass-card rounded-xl p-5 text-center border-t-2 border-t-[#FF904D]">
            <i data-lucide="database" class="w-8 h-8 primary-color mx-auto mb-3"></i>
            <h4 class="font-bold text-white mb-1">Coleções</h4>
            <p class="text-white/60 text-xs">Arrays, listas e matrizes para organizar dados</p>
        </div>
        <div class="glass-card rounded-xl p-5 text-center border-t-2 border-t-[#FF904D]">
            <i data-lucide="package" class="w-8 h-8 primary-color mx-auto mb-3"></i>
            <h4 class="font-bold text-white mb-1">Modularização</h4>
            <p class="text-white/60 text-xs">Classes, funções e escopo para código escalável</p>
        </div>
    </div>
</div>"""
cards_html.append(slide1)

# -----------------------------------------------------------------------
# SLIDE 2 — card_destaques: Sintaxe vs Semântica
# -----------------------------------------------------------------------
slide2 = """<!-- SLIDE 2: Comparativo Sintaxe vs Semântica -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="200">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="book-open" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">A Diferença Que Salva ou Quebra Seu Programa</h3>
            <p class="text-white/50 text-sm italic">Sintaxe é a regra. Semântica é o significado.</p>
        </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
        <div class="glass-card rounded-xl p-6 border-l-4 border-l-red-400">
            <div class="flex items-center gap-3 mb-4">
                <i data-lucide="alert-triangle" class="w-6 h-6 text-red-400"></i>
                <h4 class="text-xl font-bold text-red-300">Erro de Sintaxe</h4>
            </div>
            <p class="text-white/70 text-sm mb-3">A gramática está errada. Python nem executa.</p>
            <div class="bg-black/40 rounded-lg p-3 font-mono text-xs text-red-300">
                <span class="text-white/40"># SyntaxError</span><br>
                prit("Olá") <span class="text-red-400">← função inexistente</span>
            </div>
        </div>
        <div class="glass-card rounded-xl p-6 border-l-4 border-l-[#FF904D]">
            <div class="flex items-center gap-3 mb-4">
                <i data-lucide="check-circle" class="w-6 h-6 primary-color"></i>
                <h4 class="text-xl font-bold primary-color">Código Correto</h4>
            </div>
            <p class="text-white/70 text-sm mb-3">Sintaxe válida e semântica coerente.</p>
            <div class="bg-black/40 rounded-lg p-3 font-mono text-xs text-green-300">
                <span class="text-white/40"># Correto</span><br>
                print("Olá, mundo!") <span class="text-green-400">← funciona</span>
            </div>
        </div>
    </div>
    <p class="text-white/60 text-sm mt-4 text-center italic">Python é tipado dinamicamente (o tipo é inferido) mas fortemente tipado (não mistura tipos implicitamente).</p>
</div>"""
cards_html.append(slide2)

# -----------------------------------------------------------------------
# SLIDE 3 — card_tabela: Tipos nativos do Python
# -----------------------------------------------------------------------
slide3 = """<!-- SLIDE 3: Tabela de tipos nativos -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="300">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="tag" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Tipos que Você Vai Usar Todo Dia</h3>
            <p class="text-white/50 text-sm italic">Os 4 tipos nativos do Python que constroem qualquer sistema</p>
        </div>
    </div>
    <div class="overflow-x-auto">
        <table class="w-full text-sm">
            <thead>
                <tr class="border-b border-white/20">
                    <th class="text-left py-3 px-4 primary-color font-bold">Tipo</th>
                    <th class="text-left py-3 px-4 primary-color font-bold">Exemplo</th>
                    <th class="text-left py-3 px-4 primary-color font-bold">Uso típico</th>
                    <th class="text-left py-3 px-4 primary-color font-bold">Função</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                    <td class="py-3 px-4 font-mono text-[#FF904D] font-bold">int</td>
                    <td class="py-3 px-4 font-mono text-green-300">42, -7, 0</td>
                    <td class="py-3 px-4 text-white/80">Contadores, índices, idades</td>
                    <td class="py-3 px-4 font-mono text-white/60">int()</td>
                </tr>
                <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                    <td class="py-3 px-4 font-mono text-[#FF904D] font-bold">float</td>
                    <td class="py-3 px-4 font-mono text-green-300">3.14, -0.5</td>
                    <td class="py-3 px-4 text-white/80">Notas, preços, médias</td>
                    <td class="py-3 px-4 font-mono text-white/60">float()</td>
                </tr>
                <tr class="border-b border-white/10 hover:bg-white/5 transition-colors">
                    <td class="py-3 px-4 font-mono text-[#FF904D] font-bold">str</td>
                    <td class="py-3 px-4 font-mono text-green-300">"Python"</td>
                    <td class="py-3 px-4 text-white/80">Nomes, mensagens, caminhos</td>
                    <td class="py-3 px-4 font-mono text-white/60">str()</td>
                </tr>
                <tr class="hover:bg-white/5 transition-colors">
                    <td class="py-3 px-4 font-mono text-[#FF904D] font-bold">bool</td>
                    <td class="py-3 px-4 font-mono text-green-300">True, False</td>
                    <td class="py-3 px-4 text-white/80">Flags, condições, filtros</td>
                    <td class="py-3 px-4 font-mono text-white/60">bool()</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="mt-4 p-4 bg-[#FF904D]/10 rounded-lg border border-[#FF904D]/20">
        <p class="text-white/70 text-sm"><span class="primary-color font-bold">Convenção PEP 8:</span> Constantes são escritas em MAIÚSCULAS — ex: <span class="font-mono text-green-300">PI = 3.14159</span></p>
    </div>
</div>"""
cards_html.append(slide3)

# -----------------------------------------------------------------------
# SLIDE 4 — card_d3: Fluxo de Decisão com Condicionais
# -----------------------------------------------------------------------
slide4 = """<!-- SLIDE 4: Gráfico D3 de fluxo de controle -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="400">
    <div class="flex items-center gap-4 mb-4">
        <div class="icon-container">
            <i data-lucide="git-branch" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Decida ou Trave: O Poder do if-elif-else</h3>
            <p class="text-white/50 text-sm italic">Todo programa inteligente faz escolhas</p>
        </div>
    </div>
    <p class="text-white/70 mb-6 leading-relaxed max-w-3xl">
        Estruturas condicionais são o cérebro do seu código. Veja as 4 variantes do Python e quando usar cada uma.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-black/40 rounded-xl p-5 border border-white/10">
            <div class="flex items-center gap-2 mb-3">
                <i data-lucide="chevron-right" class="w-4 h-4 primary-color"></i>
                <span class="text-[#FF904D] font-bold text-sm">Desvio Simples</span>
            </div>
            <pre class="font-mono text-xs text-green-300 leading-relaxed">if nota &gt;= 7:
    print("Aprovado")</pre>
            <p class="text-white/50 text-xs mt-2">Executa apenas se verdadeiro</p>
        </div>
        <div class="bg-black/40 rounded-xl p-5 border border-white/10">
            <div class="flex items-center gap-2 mb-3">
                <i data-lucide="split" class="w-4 h-4 primary-color"></i>
                <span class="text-[#FF904D] font-bold text-sm">Desvio Composto</span>
            </div>
            <pre class="font-mono text-xs text-green-300 leading-relaxed">if nota &gt;= 7:
    print("Aprovado")
else:
    print("Reprovado")</pre>
            <p class="text-white/50 text-xs mt-2">Sempre executa um dos ramos</p>
        </div>
        <div class="bg-black/40 rounded-xl p-5 border border-white/10">
            <div class="flex items-center gap-2 mb-3">
                <i data-lucide="layers" class="w-4 h-4 primary-color"></i>
                <span class="text-[#FF904D] font-bold text-sm">Aninhado</span>
            </div>
            <pre class="font-mono text-xs text-green-300 leading-relaxed">if nota &gt;= 7:
    if frequencia &gt;= 75:
        print("Aprovado")
    else:
        print("Falta")</pre>
            <p class="text-white/50 text-xs mt-2">Condição dentro de condição</p>
        </div>
        <div class="bg-black/40 rounded-xl p-5 border border-white/10">
            <div class="flex items-center gap-2 mb-3">
                <i data-lucide="list" class="w-4 h-4 primary-color"></i>
                <span class="text-[#FF904D] font-bold text-sm">Múltipla Escolha</span>
            </div>
            <pre class="font-mono text-xs text-green-300 leading-relaxed">if nota &gt;= 9:
    print("A")
elif nota &gt;= 7:
    print("B")
else:
    print("C")</pre>
            <p class="text-white/50 text-xs mt-2">Múltiplos caminhos possíveis</p>
        </div>
    </div>
</div>"""
cards_html.append(slide4)

# -----------------------------------------------------------------------
# SLIDE 5 — card_cta (CTA obrigatório entre slides 4-8)
# -----------------------------------------------------------------------
slide5 = open(os.path.join(template_path, 'card_cta.html'), encoding='utf-8').read()
slide5 = slide5.replace('[DELAY]', '500')
slide5 = slide5.replace('[ICONE_CTA]', 'youtube')
slide5 = slide5.replace('[TITULO_CTA]', 'Aprenda Programação com o Canal Sandeco')
slide5 = slide5.replace('[DESCRICAO_CTA]', 'Vídeo-aulas práticas sobre Python, algoritmos, inteligência artificial e desenvolvimento de sistemas. Conteúdo para quem quer ir além da teoria.')
slide5 = slide5.replace('[TEXTO_BOTAO]', 'Acessar o Canal')
slide5 = slide5.replace('[URL_BOTAO]', 'https://youtube.com/@canalSandeco')
slide5 = slide5.replace('[TEXTO_RODAPE_CTA]', 'Mais de 15 capítulos cobrindo do básico ao avançado em Python')
cards_html.append(slide5)

# -----------------------------------------------------------------------
# SLIDE 6 — card_timeline: Estruturas de Repetição
# -----------------------------------------------------------------------
slide6 = """<!-- SLIDE 6: Timeline de Repetição -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="600">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="refresh-cw" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">3 Maneiras de Repetir Sem Repetir Código</h3>
            <p class="text-white/50 text-sm italic">O computador trabalha, você descansa</p>
        </div>
    </div>
    <div class="flex flex-col gap-0 mt-2">
        <div class="flex gap-4">
            <div class="flex flex-col items-center">
                <div class="w-10 h-10 rounded-full bg-[#FF904D] flex items-center justify-center font-bold text-black shrink-0">1</div>
                <div class="w-0.5 flex-1 bg-[#FF904D]/30 my-2"></div>
            </div>
            <div class="glass-card rounded-xl p-5 mb-4 flex-1">
                <h4 class="text-lg font-bold primary-color mb-1">while — Teste no Início</h4>
                <p class="text-white/70 text-sm mb-2">Verifica a condição ANTES de executar. Pode não rodar nenhuma vez.</p>
                <div class="font-mono text-xs text-green-300 bg-black/40 rounded-lg p-3">while saldo &gt; 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;saldo -= parcela</div>
            </div>
        </div>
        <div class="flex gap-4">
            <div class="flex flex-col items-center">
                <div class="w-10 h-10 rounded-full bg-[#FF904D] flex items-center justify-center font-bold text-black shrink-0">2</div>
                <div class="w-0.5 flex-1 bg-[#FF904D]/30 my-2"></div>
            </div>
            <div class="glass-card rounded-xl p-5 mb-4 flex-1">
                <h4 class="text-lg font-bold primary-color mb-1">while True + break — Teste no Fim</h4>
                <p class="text-white/70 text-sm mb-2">Executa ao menos uma vez. A condição de saída fica dentro do bloco.</p>
                <div class="font-mono text-xs text-green-300 bg-black/40 rounded-lg p-3">while True:<br>&nbsp;&nbsp;&nbsp;&nbsp;cmd = input("&gt;")<br>&nbsp;&nbsp;&nbsp;&nbsp;if cmd == "sair": break</div>
            </div>
        </div>
        <div class="flex gap-4">
            <div class="flex flex-col items-center">
                <div class="w-10 h-10 rounded-full bg-[#FF904D] flex items-center justify-center font-bold text-black shrink-0">3</div>
            </div>
            <div class="glass-card rounded-xl p-5 flex-1">
                <h4 class="text-lg font-bold primary-color mb-1">for + range — Contagem Controlada</h4>
                <p class="text-white/70 text-sm mb-2">Ideal quando você sabe exatamente quantas vezes repetir.</p>
                <div class="font-mono text-xs text-green-300 bg-black/40 rounded-lg p-3">for i in range(10):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f"Item {i}")</div>
            </div>
        </div>
    </div>
</div>"""
cards_html.append(slide6)

# -----------------------------------------------------------------------
# SLIDE 7 — card_citacao: insight sobre listas
# -----------------------------------------------------------------------
slide7 = """<!-- SLIDE 7: Citação sobre Listas -->
<div class="glass-card rounded-xl p-10 w-full max-w-5xl relative overflow-hidden" data-aos="fade-up" data-aos-delay="700">
    <div class="absolute top-0 left-0 w-2 h-full bg-[#FF904D]"></div>
    <div class="pl-6">
        <i data-lucide="quote" class="w-12 h-12 primary-color mb-6 opacity-60"></i>
        <blockquote class="text-2xl md:text-3xl font-light text-white leading-relaxed mb-6">
            "A lista do Python não é apenas um array — é uma estrutura <span class="primary-color font-bold">dinâmica, heterogênea e mutável</span> que resolve 90% dos seus problemas de armazenamento."
        </blockquote>
        <footer class="text-white/50 text-sm">
            <span class="primary-color font-semibold">Capítulo 10 · Algoritmos e Lógica de Programação II</span><br>
            <span>list() → append, extend, sort, reverse, del, in, len, min, max, sum</span>
        </footer>
    </div>
</div>"""
cards_html.append(slide7)

# -----------------------------------------------------------------------
# SLIDE 8 — card_lista: Operações de Lista com counters
# -----------------------------------------------------------------------
slide8 = """<!-- SLIDE 8: Lista de operações com contadores -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="800">
    <div class="flex items-center mb-6">
        <div class="icon-container"><i data-lucide="layers" class="primary-color"></i></div>
        <div class="w-10 h-1 primary-bg ml-4 mr-4"></div>
        <h3 class="text-3xl font-bold text-white">O Arsenal Completo das Listas</h3>
    </div>
    <ul class="space-y-5">
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="10">0</span>
            <div>
                <p class="text-white/90 text-lg"><strong>Funções nativas</strong> para manipular listas sem escrever nenhum loop: <span class="font-mono text-[#FF904D]">len, min, max, sum, sorted, reversed</span></p>
            </div>
        </li>
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="5">0</span>
            <div>
                <p class="text-white/90 text-lg"><strong>Métodos de modificação</strong> integrados ao objeto: <span class="font-mono text-[#FF904D]">append, extend, insert, remove, pop, clear</span></p>
            </div>
        </li>
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="1">0</span>
            <div>
                <p class="text-white/90 text-lg"><strong>Operador</strong> <span class="font-mono text-[#FF904D]">in</span> para busca instantânea: <span class="font-mono text-green-300">if "Python" in linguagens:</span></p>
            </div>
        </li>
    </ul>
</div>"""
cards_html.append(slide8)

# -----------------------------------------------------------------------
# SLIDE 9 — card_code: Matrizes como lista de listas
# -----------------------------------------------------------------------
slide9 = """<!-- SLIDE 9: Código de Matrizes -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="900">
    <div class="flex items-center gap-4 mb-4">
        <div class="icon-container">
            <i data-lucide="grid" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Matrizes: O Excel dos Programadores</h3>
            <p class="text-white/50 text-sm italic">Dados bidimensionais organizados em linhas e colunas</p>
        </div>
    </div>
    <p class="text-white/70 mb-6">Em Python, uma matriz é uma lista de listas. Cada elemento é acessado por dois índices: <span class="font-mono text-[#FF904D]">matriz[linha][coluna]</span></p>
    <div class="bg-black/50 border border-white/10 rounded-xl p-6">
        <div class="flex items-center gap-2 mb-4">
            <div class="w-3 h-3 rounded-full bg-red-500"></div>
            <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
            <div class="w-3 h-3 rounded-full bg-green-500"></div>
            <span class="text-white/40 text-xs ml-2">matriz_notas.py</span>
        </div>
        <pre class="font-mono text-sm text-green-300 leading-relaxed overflow-x-auto"><span class="text-white/40"># Declara matriz 3x3</span>
notas = [
    [7.5, 8.0, 9.0],
    [6.5, 7.0, 8.5],
    [5.0, 6.0, 7.5]
]

<span class="text-white/40"># Acessa nota da linha 0, coluna 2</span>
print(notas[0][2])  <span class="text-white/40"># → 9.0</span>

<span class="text-white/40"># Transpõe a matriz</span>
linhas, colunas = 3, 3
transposta = [[0]*colunas for _ in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        transposta[j][i] = notas[i][j]</pre>
    </div>
</div>"""
cards_html.append(slide9)

# -----------------------------------------------------------------------
# SLIDE 10 — card_destaques: Array vs Lista
# -----------------------------------------------------------------------
slide10 = """<!-- SLIDE 10: Comparativo Array vs Lista -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1000">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="scale" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Array ou Lista? Escolha a Arma Certa</h3>
            <p class="text-white/50 text-sm italic">Cada estrutura tem sua força — use com intenção</p>
        </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
        <div class="glass-card rounded-2xl p-8 flex flex-col items-center text-center border-t-4 border-t-white/20">
            <i data-lucide="hard-drive" class="w-10 h-10 mb-4 text-white/70"></i>
            <h4 class="text-xl font-bold mb-2">array (módulo)</h4>
            <p class="text-white/60 text-sm mb-4">Homogêneo — apenas um tipo por array. Mais eficiente em memória para dados numéricos em massa.</p>
            <div class="font-mono text-xs text-green-300 bg-black/40 rounded-lg p-3 w-full text-left">
                from array import array<br>
                nums = array('i', [1,2,3])
            </div>
            <ul class="text-left text-sm text-white/70 space-y-2 mt-4 w-full">
                <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 primary-color"></i> Alta performance numérica</li>
                <li class="flex items-center gap-2"><i data-lucide="x" class="w-4 h-4 text-red-400"></i> Não aceita tipos mistos</li>
            </ul>
        </div>
        <div class="glass-card rounded-2xl p-8 flex flex-col items-center text-center border-t-4 border-t-[#FF904D] relative transform scale-105 z-10 shadow-2xl">
            <div class="absolute -top-3 bg-[#FF904D] text-black text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-tighter">Mais Usado</div>
            <i data-lucide="list" class="w-10 h-10 mb-4 primary-color"></i>
            <h4 class="text-xl font-bold mb-2">list</h4>
            <p class="text-white/60 text-sm mb-4">Heterogênea — aceita qualquer tipo. Flexível, dinâmica e com dezenas de métodos embutidos.</p>
            <div class="font-mono text-xs text-green-300 bg-black/40 rounded-lg p-3 w-full text-left">
                alunos = ["Ana", 20, 9.5, True]<br>
                alunos.append("Pedro")
            </div>
            <ul class="text-left text-sm text-white/80 space-y-2 mt-4 w-full">
                <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 primary-color"></i> Tipos mistos e dinâmica</li>
                <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 primary-color"></i> Métodos ricos embutidos</li>
            </ul>
        </div>
    </div>
</div>"""
cards_html.append(slide10)

# -----------------------------------------------------------------------
# SLIDE 11 — card_code: Classes e Objetos
# -----------------------------------------------------------------------
slide11 = """<!-- SLIDE 11: Classes e Objetos -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1100">
    <div class="flex items-center gap-4 mb-4">
        <div class="icon-container">
            <i data-lucide="box" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Modelar o Mundo Real com Classes</h3>
            <p class="text-white/50 text-sm italic">Dados heterogêneos que representam entidades reais</p>
        </div>
    </div>
    <p class="text-white/70 mb-6">Uma classe agrupa atributos de tipos diferentes em uma entidade coesa. O construtor <span class="font-mono text-[#FF904D]">__init__</span> inicializa o objeto no momento da criação.</p>
    <div class="bg-black/50 border border-white/10 rounded-xl p-6">
        <div class="flex items-center gap-2 mb-4">
            <div class="w-3 h-3 rounded-full bg-red-500"></div>
            <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
            <div class="w-3 h-3 rounded-full bg-green-500"></div>
            <span class="text-white/40 text-xs ml-2">aluno.py</span>
        </div>
        <pre class="font-mono text-sm text-green-300 leading-relaxed overflow-x-auto"><span class="text-white/40"># Define a classe (molde)</span>
class Aluno:
    def __init__(self, nome: str, idade: int, nota: float):
        self.nome  = nome
        self.idade = idade
        self.nota  = nota

    def situacao(self):
        return "Aprovado" if self.nota &gt;= 7 else "Reprovado"

<span class="text-white/40"># Instancia objetos (exemplares)</span>
a1 = Aluno("Ana", 20, 9.5)
a2 = Aluno("Bruno", 22, 5.0)

print(a1.situacao())  <span class="text-white/40"># → Aprovado</span>
print(a2.situacao())  <span class="text-white/40"># → Reprovado</span></pre>
    </div>
</div>"""
cards_html.append(slide11)

# -----------------------------------------------------------------------
# SLIDE 12 — card_grid: Manipulação de Strings
# -----------------------------------------------------------------------
slide12 = """<!-- SLIDE 12: Grid de métodos de string -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1200">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="type" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Strings: Mais Poderosas Do Que Parecem</h3>
            <p class="text-white/50 text-sm italic">Python trata texto como objeto — e isso muda tudo</p>
        </div>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">.upper() / .lower()</div>
            <p class="text-white/60 text-xs">Converte maiúsculas e minúsculas</p>
            <div class="font-mono text-xs text-green-300 mt-2">"Python".upper()<br>→ "PYTHON"</div>
        </div>
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">.strip()</div>
            <p class="text-white/60 text-xs">Remove espaços nas bordas</p>
            <div class="font-mono text-xs text-green-300 mt-2">"  oi  ".strip()<br>→ "oi"</div>
        </div>
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">.find()</div>
            <p class="text-white/60 text-xs">Busca substring, retorna índice (-1 se não achar)</p>
            <div class="font-mono text-xs text-green-300 mt-2">"abc".find("b")<br>→ 1</div>
        </div>
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">Fatiamento</div>
            <p class="text-white/60 text-xs">Extrai pedaços por índice</p>
            <div class="font-mono text-xs text-green-300 mt-2">"Python"[0:3]<br>→ "Pyt"</div>
        </div>
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">f-string</div>
            <p class="text-white/60 text-xs">Interpolação moderna e legível</p>
            <div class="font-mono text-xs text-green-300 mt-2">f"Olá, {nome}!"<br>→ "Olá, Ana!"</div>
        </div>
        <div class="glass-card rounded-xl p-4">
            <div class="font-mono text-[#FF904D] font-bold text-sm mb-1">.replace()</div>
            <p class="text-white/60 text-xs">Substitui partes da string</p>
            <div class="font-mono text-xs text-green-300 mt-2">"a,b".replace(","," ")<br>→ "a b"</div>
        </div>
    </div>
</div>"""
cards_html.append(slide12)

# -----------------------------------------------------------------------
# SLIDE 13 — card_progresso: Jornada de aprendizado
# -----------------------------------------------------------------------
slide13 = """<!-- SLIDE 13: Barras de progresso da jornada -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1300">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="trending-up" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Sua Jornada em Números</h3>
            <p class="text-white/50 text-sm italic">15 capítulos, uma trajetória completa de crescimento</p>
        </div>
    </div>
    <div class="space-y-6">
        <div>
            <div class="flex justify-between mb-2">
                <span class="text-white/80 font-medium">Lógica e Fundamentos (Cap. 1–4)</span>
                <span class="primary-color font-bold counter" data-target="25">0</span>
            </div>
            <div class="h-3 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-[#FF904D] rounded-full progress-bar-fill" data-width="25" style="width: 0%; transition: width 1.5s ease;"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="text-white/80 font-medium">Estruturas de Repetição (Cap. 5–7)</span>
                <span class="primary-color font-bold counter" data-target="45">0</span>
            </div>
            <div class="h-3 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-[#FF904D] rounded-full progress-bar-fill" data-width="45" style="width: 0%; transition: width 1.5s ease;"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="text-white/80 font-medium">Coleções e Matrizes (Cap. 8–11)</span>
                <span class="primary-color font-bold counter" data-target="70">0</span>
            </div>
            <div class="h-3 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-[#FF904D] rounded-full progress-bar-fill" data-width="70" style="width: 0%; transition: width 1.5s ease;"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="text-white/80 font-medium">OOP, Strings e Modularização (Cap. 12–15)</span>
                <span class="primary-color font-bold counter" data-target="100">0</span>
            </div>
            <div class="h-3 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-[#FF904D] rounded-full progress-bar-fill" data-width="100" style="width: 0%; transition: width 1.5s ease;"></div>
            </div>
        </div>
    </div>
</div>"""
cards_html.append(slide13)

# -----------------------------------------------------------------------
# SLIDE 14 — card_code: Modularização com def e escopo
# -----------------------------------------------------------------------
slide14 = """<!-- SLIDE 14: Modularização -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1400">
    <div class="flex items-center gap-4 mb-4">
        <div class="icon-container">
            <i data-lucide="puzzle" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">Funções: Escreva Uma Vez, Use Sempre</h3>
            <p class="text-white/50 text-sm italic">Modularize para escalar. Escopo garante a segurança.</p>
        </div>
    </div>
    <p class="text-white/70 mb-6">Variáveis <span class="font-mono text-[#FF904D]">locais</span> vivem dentro da função. Variáveis <span class="font-mono text-[#FF904D]">globais</span> existem fora. Listas passadas como argumento são referências — modificar dentro modifica fora.</p>
    <div class="bg-black/50 border border-white/10 rounded-xl p-6">
        <div class="flex items-center gap-2 mb-4">
            <div class="w-3 h-3 rounded-full bg-red-500"></div>
            <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
            <div class="w-3 h-3 rounded-full bg-green-500"></div>
            <span class="text-white/40 text-xs ml-2">modulos.py</span>
        </div>
        <pre class="font-mono text-sm text-green-300 leading-relaxed overflow-x-auto"><span class="text-white/40"># Função com retorno</span>
def calcular_media(notas: list) -&gt; float:
    return sum(notas) / len(notas)

<span class="text-white/40"># Passagem por referência (lista é mutável)</span>
def adicionar_nota(notas: list, nova: float):
    notas.append(nova)  <span class="text-white/40"># altera a lista original</span>

minhas_notas = [8.0, 7.5, 9.0]
adicionar_nota(minhas_notas, 6.5)
print(calcular_media(minhas_notas))  <span class="text-white/40"># → 7.75</span></pre>
    </div>
    <div class="mt-4 grid grid-cols-2 gap-4">
        <div class="p-4 bg-white/5 rounded-xl border border-white/10">
            <span class="text-white/50 text-xs font-bold uppercase tracking-wider">Escopo Local</span>
            <p class="text-white/70 text-sm mt-1">Variável criada dentro da função. Invisível fora dela.</p>
        </div>
        <div class="p-4 bg-[#FF904D]/10 rounded-xl border border-[#FF904D]/20">
            <span class="primary-color text-xs font-bold uppercase tracking-wider">Escopo Global</span>
            <p class="text-white/70 text-sm mt-1">Variável visível em todo o programa. Use com moderação.</p>
        </div>
    </div>
</div>"""
cards_html.append(slide14)

# -----------------------------------------------------------------------
# SLIDE 15 — card_grid: Resumo visual dos conceitos
# -----------------------------------------------------------------------
slide15 = """<!-- SLIDE 15: Grid de resumo final -->
<div class="glass-card rounded-xl p-8 w-full max-w-5xl" data-aos="fade-up" data-aos-delay="1500">
    <div class="flex items-center gap-4 mb-6">
        <div class="icon-container">
            <i data-lucide="star" class="primary-color w-6 h-6"></i>
        </div>
        <div>
            <h3 class="text-3xl font-bold text-white">O Que Você Dominou Neste Curso</h3>
            <p class="text-white/50 text-sm italic">Uma visão panorâmica da sua nova competência em Python</p>
        </div>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">Variáveis e Tipos</h5><p class="text-white/50 text-xs mt-1">int, float, str, bool e constantes</p></div>
        </div>
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">Operadores</h5><p class="text-white/50 text-xs mt-1">Aritméticos, relacionais e lógicos</p></div>
        </div>
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">Condicionais</h5><p class="text-white/50 text-xs mt-1">if / elif / else aninhados</p></div>
        </div>
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">Repetição</h5><p class="text-white/50 text-xs mt-1">while, while True e for + range</p></div>
        </div>
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">Coleções</h5><p class="text-white/50 text-xs mt-1">Arrays, listas e matrizes</p></div>
        </div>
        <div class="glass-card rounded-xl p-5 flex items-start gap-3">
            <i data-lucide="check-circle" class="w-5 h-5 primary-color shrink-0 mt-0.5"></i>
            <div><h5 class="font-bold text-white text-sm">OOP e Funções</h5><p class="text-white/50 text-xs mt-1">Classes, objetos, def e escopo</p></div>
        </div>
    </div>
</div>"""
cards_html.append(slide15)

# -----------------------------------------------------------------------
# SLIDE 16 — card_video_bg: CTA Final inspiracional
# -----------------------------------------------------------------------
slide16_tpl = open(os.path.join(template_path, 'card_video_bg.html'), encoding='utf-8').read()
slide16 = slide16_tpl
slide16 = slide16.replace('[DELAY]', '1600')
slide16 = slide16.replace('[VIDEO_SRC]', 'header-bg.mp4')
slide16 = slide16.replace('[ICONE]', 'rocket')
slide16 = slide16.replace('[TITULO_CARD]', 'Seu Próximo Passo Começa Aqui')
slide16 = slide16.replace('[SUBTITULO]', 'Programação é prática — agora é hora de codar')
slide16 = slide16.replace('[DESCRICAO]', 'Você absorveu 15 capítulos de Algoritmos e Lógica de Programação II. A diferença entre quem sabe e quem domina é uma: exercício diário. Abra o editor e comece agora.')
slide16 = slide16.replace('<!-- [CONTEUDO_INTERNO] -->', '')
cards_html.append(slide16)

# === FOOTER ===
footer_html = open(os.path.join(template_path, 'footer.html'), encoding='utf-8').read()
footer_html = footer_html.replace('[FONTE_REFERENCIA]', 'Fonte: Material didático Algoritmos e Lógica de Programação II · Faculdade Católica')

# === MONTA O HTML FINAL ===
html_parts = [
    layout_start,
    '<body class="font-sans">',
    header,
    '\n'.join(cards_html),
    footer_html,
    layout_end
]

final_html = '\n'.join(html_parts)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"\n✅ Deck gerado com sucesso!")
print(f"   Arquivo: {output_file}")
print(f"   Total de slides: {len(cards_html)}")
