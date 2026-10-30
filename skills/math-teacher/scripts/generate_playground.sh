#!/bin/bash
# Optional maintenance helper. Teachers can open 数学探索.html directly.
set -euo pipefail
if [ "$#" -gt 1 ]; then
  printf '%s\n' '只接受一个新文件名；不接受目录、额外命令或其他参数。' >&2
  exit 2
fi
output=${1-math-explore.html}
if ! [[ "$output" =~ ^[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}\.html$ ]]; then
  printf '%s\n' '文件名须为英文字母、数字、短横线或下划线，以.html结尾；不能包含路径。' >&2
  exit 2
fi
source_dir=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
# These two wrappers keep their existing entry names and can evolve separately.
set -o noclobber
cat -- "$source_dir/数学探索.html" > "$output"
printf '已创建 %s。请手动用浏览器打开；没有联网、安装或发布操作。\n' "$output"
