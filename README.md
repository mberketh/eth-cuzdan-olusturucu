# Basit Ethereum Cüzdan Oluşturucu

Bu proje, Python kullanarak yerel konsolunuzda rastgele bir Ethereum cüzdanı (adres, genel anahtar ve özel anahtar) oluşturan basit bir script içerir.

## Kullanım

Bu script, `eth_account` ve `secrets` kütüphanelerini kullanarak rastgele bir özel anahtar oluşturur ve bu özel anahtardan bir Ethereum hesabı türetir. Hesap bilgileri aynı dizinde bir `ethereum_wallet.txt` dosyasına kaydedilir.

### Gereksinimler

- Python 3.x
- eth_account kütüphanesi

### Kurulum

1. Gerekli Python paketlerini Terminal'den yükleyin:
    ```sh
    pip3 install eth_account
    ```

2. `eth_wallet_generator.py` dosyasını çalıştırın:
    ```sh
    python3 eth_wallet_generator.py
    ```

3. Çalıştırma sonucunda oluşturulan `ethereum_wallet.txt` dosyasını kontrol edin. Dosya, cüzdan adresinizi, genel anahtarınızı ve özel anahtarınızı içerecektir.

### Çıktı İçeriği

`ethereum_wallet.txt` dosyası aşağıdaki formatta bilgileri içerir:

Address: 0x...
Public: 0x...
Private: 0x...


## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.


## İletişim

Sorularınız veya geri bildirimleriniz için lütfen [mberketh](https://twitter.com/mberketh) Twitter hesabı üzerinden iletişime geçin.