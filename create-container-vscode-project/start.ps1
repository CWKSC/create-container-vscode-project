docker container run `
    --detach `
    --hostname "create-container-vscode-project-develop-container" `
    --interactive `
    --name "create-container-vscode-project-develop-container" `
    --rm `
    --stop-timeout 0 `
    --tty `
    --privileged `
    --volume "$PWD/workspace/:/workspace/" `
    create-container-vscode-project-develop-image

if (Get-Command "cursor" -errorAction SilentlyContinue)
{
    cursor --folder-uri vscode-remote://attached-container+6372656174652d636f6e7461696e65722d7673636f64652d70726f6a6563742d646576656c6f702d636f6e7461696e6572/workspace
}
elseif (Get-Command "code" -errorAction SilentlyContinue)
{
    code --folder-uri vscode-remote://attached-container+6372656174652d636f6e7461696e65722d7673636f64652d70726f6a6563742d646576656c6f702d636f6e7461696e6572/workspace
}
