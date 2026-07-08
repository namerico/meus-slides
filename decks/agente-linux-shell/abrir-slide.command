#!/bin/sh
cd "$(dirname "$0")"
if ! command -v node >/dev/null 2>&1; then
  echo "Node.js nao encontrado. Instale o Node.js em https://nodejs.org e tente novamente."
  echo "Pressione Enter para fechar..."
  read temp
  exit 1
fi
echo "Iniciando o servidor local na porta 8137..."
echo "Esta janela de terminal atua como o servidor. Para parar a apresentacao, feche-a."
npx --yes http-server . -p 8137 -c-1 -o
