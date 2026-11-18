#!/usr/bin/env python3
"""ffquick: atalhos de ffmpeg (cortar, extrair audio, gif, reduzir). Use --dry para so imprimir o comando."""
import argparse, shlex, subprocess, sys
def build(a):
    if a.cmd == "cortar": return ["ffmpeg", "-y", "-ss", a.inicio, "-to", a.fim, "-i", a.entrada, "-c", "copy", a.saida]
    if a.cmd == "audio": return ["ffmpeg", "-y", "-i", a.entrada, "-vn", "-acodec", "libmp3lame", "-q:a", "2", a.saida]
    if a.cmd == "gif": return ["ffmpeg", "-y", "-i", a.entrada, "-vf", f"fps={a.fps},scale={a.largura}:-1", a.saida]
    if a.cmd == "reduzir": return ["ffmpeg", "-y", "-i", a.entrada, "-vcodec", "libx264", "-crf", str(a.crf), "-preset", "medium", a.saida]
def main(argv=None):
    p = argparse.ArgumentParser(); p.add_argument("--dry", action="store_true"); s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("cortar"); c.add_argument("entrada"); c.add_argument("inicio"); c.add_argument("fim"); c.add_argument("saida")
    a = s.add_parser("audio"); a.add_argument("entrada"); a.add_argument("saida")
    g = s.add_parser("gif"); g.add_argument("entrada"); g.add_argument("saida"); g.add_argument("--fps", type=int, default=12); g.add_argument("--largura", type=int, default=480)
    r = s.add_parser("reduzir"); r.add_argument("entrada"); r.add_argument("saida"); r.add_argument("--crf", type=int, default=28)
    a = p.parse_args(argv); cmd = build(a)
    if a.dry: print(shlex.join(cmd)); return 0
    return subprocess.call(cmd)
if __name__ == "__main__": sys.exit(main())
