# 启动软件

FILE=./config2.ini
if [[ -f "$FILE" ]]; then
    echo "$FILE exists."
else
    echo "$FILE  not exists!"
    > filename3.txt;
fi