#! /usr/bin/env python
# -*- coding: utf-8 -*-
from torrent import Torrent
from scrap import PB
import sys

import libtorrent, time, os

from lxml import html
import requests


class PB:
    def __init__(self, busca):
        self.busca = "https://thepiratebay.org/search/" + busca + "/0/99/0"
        self.itens = []
        self.links = []

    def get_links(self):
        pagina = requests.get(self.busca)
        tree = html.fromstring(pagina.content)

        self.itens += tree.xpath("//tr//div[@class='detName']//a/text()")
        self.links += tree.xpath(
            "//tr//a[@title='Download this torrent using magnet']/@href"
        )


class Torrent:
    def __init__(self, caminho, magnet):
        self.caminho = caminho
        self.params = {
            "save_path": os.path.join("/home/", os.getlogin(), "/Downloads/", self.caminho),
            "storage_mode": libtorrent.storage_mode_t(2),
            "paused": False,
            "auto_managed": True,
            "duplicate_is_error": True,
        }
        self.magnet = magnet

    def connect(self):

        session = libtorrent.session()
        session.listen_on(6881, 6891)
        print("Salvando o arquivo .torrent em: " + self.caminho + "...")

        handle = libtorrent.add_magnet_uri(session, self.magnet, self.params)
        session.start_dht()
        while not handle.has_metadata():
            time.sleep(0.1)

        info = handle.get_torrent_info()

        store = libtorrent.file_storage()

        for arquivo in info.files():
            store.add_file(arquivo)

        torarquivo = libtorrent.create_torrent(store)
        torarquivo.set_comment(info.comment())
        torarquivo.set_creator(info.creator())

        f = open(self.caminho, "wb")

        f.write(libtorrent.bencode(torarquivo.generate()))
        f.close()

        print("Começando o download...")

        s = handle.status()

        while s.state != libtorrent.torrent_status.seeding:
            time.sleep(10)
            print("\nBaixando...")
            print(
                "%.2f COMPLETOS\n%.1f kbps DOWNLOAD"
                % (s.progress * 100, s.download_rate / 1000)
            )
            s = handle.status()


def main():
    print("TORR Terminal Client")
    busca = raw_input("\nPesquisar: ")
    num = int(raw_input("Número máximo de arquivos: "))

    pb = PB(busca)
    pb.get_links()

    if pb.links:

        print("\n0 - Sair")

        for i in range(num):
            print(str(i + 1) + " - " + pb.itens[i])
        escolha = int(raw_input("\nEscolha: ")) - 1

        if int(escolha) + 1 == 0:
            sys.exit("Sair")

        magnet = pb.links[escolha]
        caminho = pb.itens[escolha]
        torrent = Torrent(caminho, magnet)

        torrent.connect()

    else:
        sys.exit("Não foram encontrados torrents com sua busca.")


if __name__ == "__main__":
    main()
