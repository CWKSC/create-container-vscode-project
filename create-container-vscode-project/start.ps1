docker container run `
    --detach `
    --hostname "create-container-vscode-project-container" `
    --interactive `
    --name "create-container-vscode-project-container" `
    --rm `
    --stop-timeout 0 `
    --tty `
    --volume "$PWD/workspace/:/workspace/" `
    create-container-vscode-project-image

if (Get-Command "cursor" -errorAction SilentlyContinue)
{
    cursor --folder-uri vscode-remote://attached-container+6372656174652d636f6e7461696e65722d7673636f64652d70726f6a6563742d636f6e7461696e6572/workspace
}
elseif (Get-Command "code" -errorAction SilentlyContinue)
{
    code --folder-uri vscode-remote://attached-container+6372656174652d636f6e7461696e65722d7673636f64652d70726f6a6563742d636f6e7461696e6572/workspace
}
