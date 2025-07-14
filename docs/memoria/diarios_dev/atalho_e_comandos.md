## GIT perdeu o sync (rodou sudo)
 execute o codigo abaixo

cd ~/assistente_universal
sudo chown -R $USER:$USER .

git add .  #adicionar todos arquivos ou nome do arquivo unico ao lado   

git commit -m "🛠️ Fix: commit geral de sincronização pós-ajuste de permissão" #enviarr para git-hub

