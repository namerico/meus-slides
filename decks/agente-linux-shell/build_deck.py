import os
import re

base_path = '/home/namerico/meus-slides'
template_path = os.path.join(base_path, '.agents/skills/mira-builder/templates')
deck_path = os.path.join(base_path, 'decks/agente-linux-shell')
output_file = os.path.join(deck_path, 'index.html')

# 1. Carregar Layout Base
with open(os.path.join(template_path, 'layout_base.html'), 'r', encoding='utf-8') as f:
    layout_base = f.read()

layout_start, layout_end = layout_base.split('<body class="font-sans">')
layout_start = layout_start.replace('[TITULO_DA_PAGINA]', 'SSH Orchestrator - Agente Linux Shell')
layout_start = layout_start.replace('</head>', """
<script type="importmap">
{ "imports": {
    "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
} }
</script>
</head>
""")

# 2. Carregar e preencher o Header
with open(os.path.join(template_path, 'header.html'), 'r', encoding='utf-8') as f:
    header = f.read()

header = header.replace('[TIPO_CONTEUDO]', 'Apresentação de Projeto')
header = header.replace('[TITULO_PRINCIPAL]', 'SSH Orchestrator')
header = header.replace('[SUBTITULO]', 'Cliente SSH/SFTP moderno com sincronização descentralizada via GitHub e segurança Zero-Knowledge.')
header = header.replace('canal_sandeco_logo.png', 'logo.png')

# 3. Gerar os Cards
cards_html = []

# Slide 1: card_video_bg (Abertura)
with open(os.path.join(template_path, 'card_video_bg.html'), 'r', encoding='utf-8') as f:
    card_video = f.read()
card_video = card_video.replace('[DELAY]', '100')
card_video = card_video.replace('[VIDEO_SRC]', 'header-bg.mp4')
card_video = card_video.replace('[ICONE]', 'terminal')
card_video = card_video.replace('[TITULO_CARD]', 'O Novo Padrão de Acesso SSH')
card_video = card_video.replace('[SUBTITULO]', 'Interface integrada e alta performance')
card_video = card_video.replace('[DESCRICAO]', 'Conecte-se a múltiplos servidores remotos, transfira arquivos com dual-pane e sincronize seus workspaces sem intermediários centralizados.')
card_video = card_video.replace('<!-- [CONTEUDO_INTERNO] -->', '')
cards_html.append(card_video)

# Slide 2: card_citacao (A Dor da Sincronização Isolada)
with open(os.path.join(template_path, 'card_citacao.html'), 'r', encoding='utf-8') as f:
    card_citacao = f.read()
card_citacao = card_citacao.replace('[DELAY]', '200')
card_citacao = card_citacao.replace('[TEXTO_DA_CITACAO]', '\"Manter chaves privadas, configurações de host e workspaces sincronizados entre múltiplos notebooks de forma segura e descentralizada era um pesadelo — até aplicarmos Git e CRDTs locais.\"')
card_citacao = card_citacao.replace('[AUTOR]', 'Engenheiro de Confiabilidade de Sistemas (SRE)')
card_citacao = card_citacao.replace('[CARGO_OU_FONTE]', 'Especialista em DevOps & Infraestrutura')
cards_html.append# Slide 3: card_d3 (Rede de Nós Distribuídos 3D)
with open(os.path.join(template_path, 'card_d3.html'), 'r', encoding='utf-8') as f:
    card_d3 = f.read()
card_d3 = card_d3.replace('[DELAY]', '300')
card_d3 = card_d3.replace('[ICONE]', 'globe')
card_d3 = card_d3.replace('[TITULO_GRAFICO]', 'Rede de Nós Distribuídos')
card_d3 = card_d3.replace('[SUBTITULO]', 'Visualização tridimensional interativa da topologia')
card_d3 = card_d3.replace('[DESCRICAO]', 'Arraste com o mouse para rotacionar a rede de servidores remotos e dê zoom usando a rolagem. A auto-rotação reinicia automaticamente após interações.')
card_d3 = card_d3.replace('[CONTAINER_ID]', 'vault-3d-canvas')
card_d3 = card_d3.replace('[ALTURA]', '450')
card_d3 = card_d3.replace('[LARGURA]', '800')

# Lógica procedural Three.js
three_js_code = """
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const wrap = document.getElementById('vault-3d-canvas');
if (wrap) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, wrap.clientWidth / wrap.clientHeight, 0.1, 100);
    camera.position.set(0, 0, 8);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(wrap.clientWidth, wrap.clientHeight);
    wrap.appendChild(renderer.domElement);

    // Criar grupo de nós
    const holder = new THREE.Group();
    scene.add(holder);

    // Criar partículas (nós)
    const particleCount = 60;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const velocities = [];

    for (let i = 0; i < particleCount; i++) {
        const x = (Math.random() - 0.5) * 4.5;
        const y = (Math.random() - 0.5) * 4.5;
        const z = (Math.random() - 0.5) * 4.5;
        positions[i * 3] = x;
        positions[i * 3 + 1] = y;
        positions[i * 3 + 2] = z;
        velocities.push({
            x: (Math.random() - 0.5) * 0.006,
            y: (Math.random() - 0.5) * 0.006,
            z: (Math.random() - 0.5) * 0.006
        });
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({
        color: 0x00FF7F,
        size: 0.16,
        transparent: true,
        opacity: 0.85
    });

    const points = new THREE.Points(geometry, material);
    holder.add(points);

    // Linhas
    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0x00FF7F,
        transparent: true,
        opacity: 0.2
    });

    let lineSegments = new THREE.LineSegments(new THREE.BufferGeometry(), lineMaterial);
    holder.add(lineSegments);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.enablePan = false;
    controls.minDistance = 4;
    controls.maxDistance = 15;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.8;

    let resume = null;
    controls.addEventListener('start', () => { controls.autoRotate = false; clearTimeout(resume); });
    controls.addEventListener('end', () => { resume = setTimeout(() => controls.autoRotate = true, 2500); });

    let rafId = null;
    function animate() {
        rafId = requestAnimationFrame(animate);

        const pos = points.geometry.attributes.position.array;
        const linePositions = [];

        for (let i = 0; i < particleCount; i++) {
            pos[i * 3] += velocities[i].x;
            pos[i * 3 + 1] += velocities[i].y;
            pos[i * 3 + 2] += velocities[i].z;

            if (Math.abs(pos[i * 3]) > 2.5) velocities[i].x *= -1;
            if (Math.abs(pos[i * 3 + 1]) > 2.5) velocities[i].y *= -1;
            if (Math.abs(pos[i * 3 + 2]) > 2.5) velocities[i].z *= -1;
        }
        points.geometry.attributes.position.needsUpdate = true;

        for (let i = 0; i < particleCount; i++) {
            for (let j = i + 1; j < particleCount; j++) {
                const dx = pos[i * 3] - pos[j * 3];
                const dy = pos[i * 3 + 1] - pos[j * 3 + 1];
                const dz = pos[i * 3 + 2] - pos[j * 3 + 2];
                const dist = Math.sqrt(dx*dx + dy*dy + dz*dz);

                if (dist < 1.4) {
                    linePositions.push(pos[i * 3], pos[i * 3 + 1], pos[i * 3 + 2]);
                    linePositions.push(pos[j * 3], pos[j * 3 + 1], pos[j * 3 + 2]);
                }
            }
        }

        holder.remove(lineSegments);
        const lineGeometry = new THREE.BufferGeometry();
        lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
        lineSegments = new THREE.LineSegments(lineGeometry, lineMaterial);
        holder.add(lineSegments);

        controls.update();
        renderer.render(scene, camera);
    }

    new IntersectionObserver((es) => es.forEach(e => {
        if (e.isIntersecting && rafId === null) animate();
        else if (!e.isIntersecting && rafId !== null) { cancelAnimationFrame(rafId); rafId = null; }
    }), { threshold: 0.1 }).observe(wrap);

    new ResizeObserver(() => {
        const w = wrap.clientWidth, h = wrap.clientHeight;
        if (!w || !h) return;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h);
    }).observe(wrap);
}
</script>
"""

# Substituir o script D3 no card_d3 pelo script Three.js
card_d3 = re.sub(
    r'<script>.*?</script>',
    three_js_code,
    card_d3,
    flags=re.DOTALL
)

cards_html.append(card_d3)

# Slide 4: card_lista (Poder de Terminal)
with open(os.path.join(template_path, 'card_lista.html'), 'r', encoding='utf-8') as f:
    card_lista = f.read()
card_lista = card_lista.replace('[DELAY]', '400')
card_lista = card_lista.replace('[ICONE]', 'monitor-play')
card_lista = card_lista.replace('[TITULO_CARD]', 'Poder de Terminal Sem Limites')

list_body = """
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="6">0</span>
            <p class="text-white/90 text-lg"><strong>Temas Visuais Inclusos:</strong> Escolha a paleta de cores perfeita para o seu terminal e evite fadiga visual.</p>
        </li>
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="4">0</span>
            <p class="text-white/90 text-lg"><strong>Split-Pane Nativo:</strong> Divida a tela horizontal ou verticalmente para monitorar múltiplos servidores em paralelo.</p>
        </li>
        <li class="flex items-start">
            <span class="text-5xl font-black primary-color mr-4 counter" data-target="1">0</span>
            <p class="text-white/90 text-lg"><strong>Abas Dedicadas:</strong> Alterne rapidamente entre terminais SSH remotos e sessões de shell locais na mesma interface.</p>
        </li>
"""
card_lista = re.sub(r'<li class="flex items-start">.*?</li>', list_body, card_lista, flags=re.DOTALL)
cards_html.append(card_lista)

# Slide 5: card_destaques (Vault Zero-Knowledge)
with open(os.path.join(template_path, 'card_destaques.html'), 'r', encoding='utf-8') as f:
    card_destaques = f.read()
card_destaques = card_destaques.replace('[DELAY]', '500')

card_destaques = card_destaques.replace('[ICONE_1]', 'shield-alert')
card_destaques = card_destaques.replace('[TITULO_1]', 'PBKDF2 KDF')
card_destaques = card_destaques.replace('[DESCRICAO_1]', 'Derivação de chaves locais usando 100.000 iterações de hashing para deter força bruta.')
card_destaques = card_destaques.replace('[VALOR_1]', 'Cofre Forte')

card_destaques = card_destaques.replace('[ICONE_2]', 'lock')
card_destaques = card_destaques.replace('[TITULO_2]', 'AES-256-GCM')
card_destaques = card_destaques.replace('[DESCRICAO_2]', 'Criptografia simétrica com autenticação integrada para proteger o cofre localmente.')
card_destaques = card_destaques.replace('[VALOR_2]', 'Blindagem')

card_destaques = card_destaques.replace('[ICONE_3]', 'key-round')
card_destaques = card_destaques.replace('[TITULO_3]', 'Sem Custódia')
card_destaques = card_destaques.replace('[DESCRICAO_3]', 'A senha mestre nunca é armazenada local ou remotamente, garantindo privacidade absoluta.')
card_destaques = card_destaques.replace('[VALOR_3]', 'Zero-Knowledge')

items = [
    ('[ITEM_A]', 'Derivação robusta baseada em PBKDF2', 1),
    ('[ITEM_B]', 'Impenetrável por força bruta', 1),
    ('[ITEM_A]', 'Ciphertext seguro e autenticado', 1),
    ('[ITEM_B]', 'Integridade garantida do chaveiro', 1),
    ('[ITEM_A]', 'Ninguém além de você lê as chaves', 1),
    ('[ITEM_B]', 'Sem servidores de custódia centralizados', 1)
]
for target, val, count in items:
    card_destaques = card_destaques.replace(target, val, count)

cards_html.append(card_destaques)

# Slide 6: card_cta (Chamada para Ação no meio da apresentação)
with open(os.path.join(template_path, 'card_cta.html'), 'r', encoding='utf-8') as f:
    card_cta = f.read()
card_cta = card_cta.replace('[DELAY]', '600')
card_cta = card_cta.replace('[IMAGEM_URL]', 'logo.png')
card_cta = card_cta.replace('[IMAGEM_ALT]', 'Logo SSH Orchestrator')
card_cta = card_cta.replace('[DELAY+200]', '800')
card_cta = card_cta.replace('[TAG_SUPERIOR]', 'Sincronização Automática')
card_cta = card_cta.replace('[TITULO_PRINCIPAL]', 'Ative o Sync via')
card_cta = card_cta.replace('[TITULO_DESTAQUE]', 'GitHub Private')
card_cta = card_cta.replace('[SUBTITULO]', 'Conecte o SSH Orchestrator ao seu repositório privado do GitHub e sincronize seus workspaces de forma automatizada.')
card_cta = card_cta.replace('[BENEFICIO_1_TITULO]', 'Criptografia Total')
card_cta = card_cta.replace('[BENEFICIO_1_DESC]', 'Os dados são armazenados de forma cifrada com sua senha mestre local.')
card_cta = card_cta.replace('[BENEFICIO_2_TITULO]', 'Merge Determinístico')
card_cta = card_cta.replace('[BENEFICIO_2_DESC]', 'Fusão inteligente de modificações concorrentes com algoritmos de CRDT.')
card_cta = card_cta.replace('[BENEFICIO_3_TITULO]', 'Infraestrutura Própria')
card_cta = card_cta.replace('[BENEFICIO_3_DESC]', 'Nenhum servidor de nuvem de terceiros. A infraestrutura é totalmente sua.')
card_cta = card_cta.replace('[LINK_CTA]', 'https://github.com/settings/apps')
card_cta = card_cta.replace('[TEXTO_BOTAO]', 'Configurar Conexão GitHub')
card_cta = card_cta.replace('[TEXTO_GARANTIA]', 'A sincronização é direta, local para o GitHub, sem intermediários.')
cards_html.append(card_cta)

# Slide 7: card_code (Algoritmo de Conflito em Rust)
with open(os.path.join(template_path, 'card_code.html'), 'r', encoding='utf-8') as f:
    card_code = f.read()
card_code = card_code.replace('[DELAY]', '700')
card_code = card_code.replace('[LINGUAGEM]', 'RUST')

raw_rust = """// Last-Writer-Wins Register: resolve conflitos com HLC (Hybrid Logical Clock)
// Commutative, associative, and idempotent merge operations
pub fn merge(&mut self, other: Self) {
    if other.updated_at > self.updated_at {
        // Se a timestamp remota/recebida for maior, assume o novo valor
        self.value = other.value;
        self.updated_at = other.updated_at;
    }
}
"""
esc_rust = raw_rust.replace('<', '&lt;').replace('>', '&gt;')
card_code = card_code.replace('[CODIGO_RAW]', raw_rust.replace('`', '\\`'))
card_code = card_code.replace('[CONTEUDO_CODIGO]', esc_rust)
card_code = card_code.replace('[DESCRICAO_DO_ARQUIVO]', 'sync/crdt.rs — Lógica de merge e resolução de conflitos')
cards_html.append(card_code)

# Slide 8: card_tabela (SFTP Dual-Pane de Alta Velocidade)
with open(os.path.join(template_path, 'card_tabela.html'), 'r', encoding='utf-8') as f:
    card_tabela = f.read()
card_tabela = card_tabela.replace('[DELAY]', '800')
card_tabela = card_tabela.replace('[TITULO_TABELA]', 'Matriz de Operações SFTP')

# Substituir a tabela por completo para usar 4 colunas customizadas
custom_table = """
        <table class="w-full text-left border-collapse">
            <thead>
                <tr class="border-b border-white/20">
                    <th class="py-4 px-4 text-[#00FF7F] font-bold uppercase text-sm tracking-wider">Operação</th>
                    <th class="py-4 px-4 text-[#00FF7F] font-bold uppercase text-sm tracking-wider">Mecanismo</th>
                    <th class="py-4 px-4 text-[#00FF7F] font-bold uppercase text-sm tracking-wider">Concorrência</th>
                    <th class="py-4 px-4 text-[#00FF7F] font-bold uppercase text-sm tracking-wider">Desempenho</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-white/10">
                <tr class="hover:bg-white/5 transition-colors">
                    <td class="py-4 px-4 text-white font-medium">Upload / Download</td>
                    <td class="py-4 px-4 text-white/80">Fila assíncrona useSftpQueue</td>
                    <td class="py-4 px-4 text-white/80">Múltiplas threads</td>
                    <td class="py-4 px-4">
                        <span class="bg-[#00FF7F]/20 text-[#00FF7F] text-xs px-3 py-1 rounded-full border border-[#00FF7F]/30">
                            Alta Velocidade
                        </span>
                    </td>
                </tr>
                <tr class="hover:bg-white/5 transition-colors">
                    <td class="py-4 px-4 text-white font-medium">Navegação de Pastas</td>
                    <td class="py-4 px-4 text-white/80">Comandos Tauri IPC Invokes</td>
                    <td class="py-4 px-4 text-white/80">Assíncrona via Tokio</td>
                    <td class="py-4 px-4">
                        <span class="bg-[#00FF7F]/20 text-[#00FF7F] text-xs px-3 py-1 rounded-full border border-[#00FF7F]/30">
                            Instantânea (&lt;50ms)
                        </span>
                    </td>
                </tr>
                <tr class="hover:bg-white/5 transition-colors">
                    <td class="py-4 px-4 text-white font-medium">Transferência Recursiva</td>
                    <td class="py-4 px-4 text-white/80">russh SFTP Engine nativa</td>
                    <td class="py-4 px-4 text-white/80">Processamento em Lote</td>
                    <td class="py-4 px-4">
                        <span class="bg-[#00FF7F]/20 text-[#00FF7F] text-xs px-3 py-1 rounded-full border border-[#00FF7F]/30">
                            Estável / Seguro
                        </span>
                    </td>
                </tr>
            </tbody>
        </table>
"""
card_tabela = re.sub(r'<table.*?>.*?</table>', custom_table, card_tabela, flags=re.DOTALL)
card_tabela = card_tabela.replace('* Dados atualizados em [DATA]', '* Informações extraídas da especificação da API de I/O em Rust.')
cards_html.append(card_tabela)

# Slide 9: card_progresso (A Escalada do DevOps)
with open(os.path.join(template_path, 'card_progresso.html'), 'r', encoding='utf-8') as f:
    card_progresso = f.read()
card_progresso = card_progresso.replace('[DELAY]', '900')
card_progresso = card_progresso.replace('[TITULO_PROGRESSO]', 'Adoção e Configuração')

progress_body = """        <div>
            <div class="flex justify-between mb-2">
                <span class="font-semibold text-white/80">Etapa 1: Inicialização do Vault Criptografado Local</span>
                <span class="primary-color font-bold">100%</span>
            </div>
            <div class="w-full h-3 bg-white/20 rounded-full">
                <div class="h-full rounded-full primary-bg progress-bar-fill"
                    style="width: 0%; transition: width 2s ease-out;" data-width="100"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="font-semibold text-white/80">Etapa 2: Cadastro de Servidores e Workspaces</span>
                <span class="primary-color font-bold">75%</span>
            </div>
            <div class="w-full h-3 bg-white/20 rounded-full">
                <div class="h-full rounded-full primary-bg progress-bar-fill"
                    style="width: 0%; transition: width 2s ease-out;" data-width="75"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="font-semibold text-white/80">Etapa 3: Integração GitHub OAuth (Repositório Privado)</span>
                <span class="primary-color font-bold">50%</span>
            </div>
            <div class="w-full h-3 bg-white/20 rounded-full">
                <div class="h-full rounded-full primary-bg progress-bar-fill"
                    style="width: 0%; transition: width 2s ease-out;" data-width="50"></div>
            </div>
        </div>
        <div>
            <div class="flex justify-between mb-2">
                <span class="font-semibold text-white/80">Etapa 4: Sincronização Automática entre Outros Dispositivos</span>
                <span class="primary-color font-bold">25%</span>
            </div>
            <div class="w-full h-3 bg-white/20 rounded-full">
                <div class="h-full rounded-full primary-bg progress-bar-fill"
                    style="width: 0%; transition: width 2s ease-out;" data-width="25"></div>
            </div>
        </div>"""

default_progress_block = """        <div>
            <div class="flex justify-between mb-2">
                <span class="font-semibold">[LABEL]</span>
                <span class="primary-color font-bold">[VALOR]%</span>
            </div>
            <div class="w-full h-3 bg-white/20 rounded-full">
                <div class="h-full rounded-full primary-bg progress-bar-fill"
                    style="width: 0%; transition: width 2s ease-out;" data-width="[VALOR]"></div>
            </div>
        </div>"""

card_progresso = card_progresso.replace(default_progress_block, progress_body)
cards_html.append(card_progresso)

# Slide 10: card_grid (O Ecossistema Sob Seu Controle)
with open(os.path.join(template_path, 'card_grid.html'), 'r', encoding='utf-8') as f:
    card_grid = f.read()
card_grid = card_grid.replace('[DELAY]', '1000')
card_grid = card_grid.replace('[ICONE]', 'network')
card_grid = card_grid.replace('[TITULO_GRID]', 'Estação de Trabalho Completa')

grid_body = """
        <div class="rounded-lg p-6 bg-white/5" data-aos="zoom-in">
            <div class="text-xl font-bold primary-color mb-2">xterm.js Engine</div>
            <p class="text-white/80 text-sm">Emulador de terminal completo e rápido com abas, split-pane e 6 temas visuais elegantes.</p>
        </div>
        <div class="rounded-lg p-6 bg-white/5" data-aos="zoom-in" data-aos-delay="100">
            <div class="text-xl font-bold primary-color mb-2">portable-pty Shell</div>
            <p class="text-white/80 text-sm">Terminal local nativo integrado para executar ferramentas e comandos em sua própria máquina.</p>
        </div>
        <div class="rounded-lg p-6 bg-white/5" data-aos="zoom-in" data-aos-delay="200">
            <div class="text-xl font-bold primary-color mb-2">russh SSH Engine</div>
            <p class="text-white/80 text-sm">Engine de conectividade SSH robusta e rápida em Rust assíncrono para I/O imediata.</p>
        </div>
        <div class="rounded-lg p-6 bg-white/5" data-aos="zoom-in" data-aos-delay="300">
            <div class="text-xl font-bold primary-color mb-2">CRDT Sincronizado</div>
            <p class="text-white/80 text-sm">Resolução matemática de conflitos via HLC, garantindo fusões de workspaces sem perda de dados.</p>
        </div>
"""
card_grid = re.sub(r'<div class="rounded-lg p-6 bg-white/5".*?</div>\s*</div>', grid_body + '</div>', card_grid, flags=re.DOTALL)
cards_html.append(card_grid)


# 4. Carregar e preencher o Footer
with open(os.path.join(template_path, 'footer.html'), 'r', encoding='utf-8') as f:
    footer = f.read()
footer = footer.replace('[FONTE_REFERENCIA]', 'Referência do Projeto: https://github.com/marcos2872/SSH_Orchestrator')
footer = footer.replace('canal_sandeco_logo.png', 'logo.png')
footer = footer.replace('Canal Sandeco', 'SSH Orchestrator')

# Juntar tudo
body_content = header + '\n' + '\n'.join(cards_html) + '\n' + footer

# Injetar o corpo no layout base
final_html = layout_start + '<body class="font-sans">\n' + body_content + '\n' + layout_end

# 5. Aplicar o tema neon-emerald (substituições globais no CSS do layout base)
final_html = final_html.replace('#FF904D', '#00FF7F')
final_html = final_html.replace('rgba(255, 144, 77', 'rgba(0, 255, 127')
final_html = final_html.replace('rgba(255, 162, 3', 'rgba(0, 255, 127')
final_html = final_html.replace('#ff9f7d', '#80FFC0')

theme_override = """
    :root {
        --mira-primary: #00FF7F;
        --mira-bg: #000000;
        --mira-text: #ffffff;
        --mira-text-soft: rgba(255, 255, 255, 0.70);
        --mira-text-softer: rgba(255, 255, 255, 0.50);
        --mira-card-bg: rgba(0, 255, 127, 0.03);
        --mira-card-border: rgba(0, 255, 127, 0.15);
        --mira-glow-soft: rgba(0, 255, 127, 0.12);
        --mira-glow-strong: rgba(0, 255, 127, 0.22);
        --mira-icon-bg: rgba(0, 255, 127, 0.12);
        --mira-icon-border: rgba(0, 255, 127, 0.25);
        --mira-pill-bg: rgba(255, 255, 255, 0.04);
        --mira-pill-border: rgba(255, 255, 255, 0.08);
        --mira-stage-glow: rgba(0, 255, 127, 0.06);
        --mira-accent-2: #80FFC0;
    }
"""
final_html = final_html.replace('</style>', theme_override + '\n</style>')

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html do SSH Orchestrator gerado com sucesso!")
