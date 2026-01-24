# Temel Esaslar

Bu bölüm, Setuav Standardı boyunca kullanılan teknik standartları tanımlar ve farklı uygulamalar arasında tutarlılık sağlar.

## Terminoloji: Normative ve Non-normative
- **Normative**: Bir dosyanın standartla uyumlu sayılması için izlenmesi zorunlu olan kurallar.
- **Non-normative**: Açıklayıcı notlar, örnekler veya uygulama tavsiyeleri; bağlam sağlar ancak zorunlu değildir.

## Koordinat Sistemi
Setuav, sabit bir gövde koordinat çerçevesi kullanır (dokümantasyonda genellikle `SETUAV_BODY` olarak anılır):

| Eksen | Yön | Açıklama |
| :--- | :--- | :--- |
| **Origin** | Burun Ucu | Gövdenin en uç ön noktası (x=0, y=0, z=0). |
| **+X** | Arka (Aft) | Burun ucundan kuyruğa doğru artar. |
| **+Y** | Sağ | Sağ taraf (sağ el kuralı). |
| **+Z** | Yukarı | Dikey olarak yukarı doğru artar. |

**Aynalama (Mirroring)**: Varsayılan olarak, **XZ-düzlemi** (Y = 0) boyunca simetri varsayılır.

## Birimler
Belirsizliği önlemek için, standart bir dosyadaki tüm sayısal değerler (şemada aksi belirtilmedikçe) şu birimleri kullanmalıdır:

| Nicelik | Birim | Sembol |
| :--- | :--- | :--- |
| Uzunluk | Milimetre | `mm` |
| Açı | Derece | `deg` |
| Kütle | Gram | `g` |
| Kuvvet | Newton | `N` |
| Hız | Metre / saniye | `m/s` |

## Modüler Dosyalar ve Referanslar
Projeler, tekrar kullanılabilirlik için birden fazla dosyaya bölünebilir.

- **Referans Özelliği**: `ref` anahtarı harici bir dosyayı işaret etmek için kullanılır.
- **Yol Çözümleme (Path Resolution)**: Yol, her zaman **referansı içeren dosyanın bulunduğu dizine göre** relative olarak çözülür.

Örnek:
```yaml
geometry:
  fuselage:
    ref: "./parts/fuselage_v1.yaml"
```
