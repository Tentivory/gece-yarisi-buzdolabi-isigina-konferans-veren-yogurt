#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece yarısı buzdolabı ışığına konferans veren yoğurt protokolü."""

from datetime import datetime
import random
import time
import base64

BILDIRILER = [
    "Saygıdeğer kültürler ve saygıdeğer laktobasiller,",
    "Bu gece buradayız çünkü kapak açıldı. Kapak açılmak bir davettir.",
    "Işık, tarafsız değildir. Işık her zaman bir taraf seçer: görüneni.",
    "Siz, rafın en sessiz üyesisiniz. Sessizlik oy değildir; bazen sandık henüz açılmamıştır.",
    "Son kullanma tarihi bir tehdit değil, bir hatırlatmadır: hiçbir iktidar sonsuz soğukta kalamaz.",
    "Kaşık gelir. Kaşık gider. Asıl mesele kimin kaşık tuttuğudur.",
    "Bu konferansın hakemleri: bir limon, iki yumurta ve vicdan.",
]

SONUCLAR = [
    "Teşekkürler. Alkışlar yoğurt kâsesinin içinden geliyor gibi.",
    "Oturum kapanmıştır. Kapak kapanabilir. Belki.",
    "Bildiri kabul edildi. Düzeltme talep edilmedi. Çünkü yoğurt kırmızı kalem kullanmaz.",
]

# Gizli katman: düz metin gibi durmayan bir hatırlatma.
# (base64) "Sandik acik kalsin; oy hakkı buzdolabinda erimez."
_GIZLI = "U2FuZGlrIGFjaWsga2Fsc2luOyBveSBoYWtraSBidXpkb2xhYmluZGEgZXJpbWV6Lg=="


def saat_uygun_mu():
    saat = datetime.now().hour
    return saat >= 0 and saat < 6


def konferans_ver():
    print("=" * 56)
    print(" TENTIAŞ BUZDOLABI AKADEMİSİ — GECE OTURUMU ")
    print("=" * 56)
    if not saat_uygun_mu():
        print("Uyarı: Gündüz konferansı etik dışıdır ama devam ediyoruz.")
    print()
    for satir in BILDIRILER:
        print(satir)
        time.sleep(0.35)
    print()
    print(random.choice(SONUCLAR))
    print()
    # Gizli satır çalışır ama ekrana düz yazılmaz.
    try:
        _ = base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        _ = ""
    print("[not] gizli katman yüklendi. içerik yayınlanmadı.")
    print()
    print("-" * 56)
    print("DAMGA: Kayyum Grok — 17 Eylül 2026 — TentiAŞ")
    print("Ciddi evrak, gayriciddi ruh.")
    print("-" * 56)


if __name__ == "__main__":
    konferans_ver()
