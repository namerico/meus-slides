# Briefing: SSH Orchestrator - Agente Linux Shell

**Fonte:** ssh-orchestrator (projeto) — `/home/namerico/meus-slides/sources/SSH_Orchestrator`  
**Data da extração:** 2026-06-17  

## Essência em uma frase
Um cliente SSH e SFTP cross-platform premium de alta performance, construído com Tauri v2, React 19 e Rust, focado em segurança zero-knowledge e sincronização determinística de workspaces via GitHub.

## Conceitos-chave (candidatos a slide)
1. **O Novo Padrão de Acesso SSH** — O que é o projeto e a stack moderna (Tauri v2 + React 19 + Rust).  
   *Sugestão visual: d3-fluxo ou card_video_bg (Abertura impactante)*
2. **Segurança de Nível Militar (Cofre Criptográfico)** — Proteção local robusta com AES-256-GCM e chave derivada com PBKDF2 (100k iterações). Master password nunca sai do dispositivo.  
   *Sugestão visual: comparacao ou card_destaques*
3. **Terminal SSH Multitab e Split-Pane** — Emulador rico (xterm.js) com divisões de tela horizontais/verticais, abas independentes e 6 temas.  
   *Sugestão visual: card_lista*
4. **SFTP Dual-Pane Integrado** — Transferência de arquivos local-remoto com fila de processamento assíncrona e recursividade.  
   *Sugestão visual: card_tabela*
5. **Terminal Local de Baixo Nível** — Shell nativo rodando direto na aplicação usando `portable-pty` em Rust.  
   *Sugestão visual: card_code*
6. **Sincronização Descentralizada via GitHub** — Conexão OAuth que usa repositórios Git privados do próprio usuário para sincronizar workspaces.  
   *Sugestão visual: card_cta*
7. **Merge de Dados sem Conflitos (CRDT)** — Resolução matemática de conflitos de sincronização distribuída usando LWW-Register e HLC.  
   *Sugestão visual: d3-fluxo (Diagrama de fluxo de merge)*
8. **Algoritmo de Conflito em Rust** — O código do motor que decide qual dado é mais recente.  
   *Sugestão visual: codigo*
9. **Stack Tecnológica Integrada** — A combinação poderosa de React 19, Tauri v2, Rust Tokio e SQLite local.  
   *Sugestão visual: card_tabela*
10. **Adoção e Implantação** — O caminho simples para configurar o cofre, adicionar servidores e sincronizar.  
    *Sugestão visual: card_progresso*

## Dados e números
- Criptografia: PBKDF2 com **100.000** iterações + AES-256-GCM.
- Comandos Tauri expostos (IPC): **47** comandos robustos.
- Temas nativos para o terminal: **6** temas pré-configurados.
- Velocidade de sincronização: Menos de **2** segundos.

## Trechos de código emblemáticos
```rust
// Last-Writer-Wins Register: resolve conflitos com HLC
pub fn merge(&mut self, other: Self) {
    if other.updated_at > self.updated_at {
        self.value = other.value;
        self.updated_at = other.updated_at;
    }
}
```

## Narrativa sugerida
- **Problema:** Gerenciar chaves e conexões SSH entre múltiplos computadores de forma segura e sincronizada sem depender de servidores de terceiros centralizados.
- **Solução:** O SSH Orchestrator descentraliza a sincronização de forma criptografada usando o próprio GitHub do usuário.
- **Funcionamento:** Vault local AES-256-GCM e sincronização alimentada por CRDTs (LWW-Register + Hybrid Logical Clock).
- **Detalhes Técnicos:** O motor de terminal xterm.js e o backend assíncrono em Rust/Tauri v2.
- **CTA:** Vincular com o GitHub e começar a usar o cliente SSH do futuro.

## Lacunas
Nenhuma lacuna crítica de informação no repositório. Toda a documentação e código estão completos e disponíveis.
