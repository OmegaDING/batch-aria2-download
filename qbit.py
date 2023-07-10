from qbittorrent import Client

qb = Client('http://192.168.2.100:8080/')

qb.login('admin', 'adminadmin')
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()


magnet_link ="magnet:?xt=urn:btih:622AEC26133440960B78AADD680734AE863CC6CD&dn=5+Centimeters+per+Second+%282007%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.tracker.cl%3A1337%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=https%3A%2F%2Fopentracker.i2p.rocks%3A443%2Fannounce"

dl_path = 'E:\\tempMovie'
qb.download_from_link(magnet_link, savepath=dl_path)

torrents = qb.torrents()
for torrent in torrents:
    print(torrent['name'])
print("\n")