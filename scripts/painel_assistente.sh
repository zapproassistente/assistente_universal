#!/bin/bash
# painel_assistente.sh - Painel de automação local do Assistente Universal

PROJETO=~/assistente_universal
SCRIPTS="$PROJETO/scripts"

cd "$PROJETO" || {
    echo "❌ Projeto não encontrado em $PROJETO"
    exit 1
}

clear
while true; do
    echo "=============================="
    echo "🧠 ASSISTENTE UNIVERSAL - TERMINAL DEV"
    echo "📍 Projeto: $PROJETO"
    echo "=============================="
    echo "1️⃣  Git Sync     (add, commit, pull --rebase, push, deploy landing)"
    echo "2️⃣  Git Push     (add, commit, push)"
    echo "3️⃣  Git Pull     (pull --rebase)"
    echo "4️⃣  Abrir no VS Code"
    echo "0️⃣  Sair"
    echo "=============================="
    read -rp "👉 Escolha uma opção: " opcao

    case "$opcao" in
        1) bash "$SCRIPTS/git_sync.sh" ;;
        2) bash "$SCRIPTS/git_push.sh" ;;
        3) bash "$SCRIPTS/git_pull.sh" ;;
        4) code . ;;
        0) echo "👋 Saindo do painel." && break ;;
        *) echo "❌ Opção inválida. Tente novamente." ;;
    esac

    echo -e "\n🔄 Pressione ENTER para voltar ao menu..."
    read
    clear
done
