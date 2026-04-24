#!/usr/bin/env sh
set -eu

if [ "$#" -eq 0 ]; then
  exec python main.py
fi

case "$1" in
  -*)
    exec python main.py "$@"
    ;;
  *)
    exec "$@"
    ;;
esac
