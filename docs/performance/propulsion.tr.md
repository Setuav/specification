# İtki Performansı

Bu modül, motor-pervane kombinasyonunun **statik (yer testi)** performans verilerini ve genel sistem verimliliğini içerir.

## Statik Performans (Tam Gaz)

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **static_thrust_max** | `g` | Maksimum gazda üretilen toplam itki. |
| **static_power_max** | `W` | Maksimum gazda tüketilen toplam güç. |
| **static_current_max** | `A` | Maksimum gazda çekilen toplam akım. |
| **static_efficiency** | `g/W` | Tam gazda güç başına üretilen itki (verimlilik). |

## Sistem Metrikleri

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **thrust_to_weight** | `-` | İtki / Ağırlık oranı. >1 değerler sınırsız dikey tırmanış yeteneğini gösterir. |
| **pitch_speed** | `m/s` | Pervane hatvesine bağlı teorik hava akış hızı. Genellikle maksimum uçuş hızını sınırlar. |

## Performans Eğrileri (Curves)

`curves` nesnesi, gaz değişimine bağlı performansı gösteren dizileri içerir.

| Parametre | Birim | Açıklama |
| :--- | :--- | :--- |
| **rpm** | `RPM` | Motor devir değerleri (X ekseni). |
| **thrust** | `g` | İlgili devirdeki itki. |
| **power** | `W` | İlgili devirdeki güç tüketimi. |
| **current** | `A` | İlgili devirdeki akım tüketimi. |
| **efficiency** | `g/W` | İlgili devirdeki verimlilik. |

## Örnek Konfigürasyon

```yaml
propulsion:
  static_thrust_max: 2500
  static_power_max: 450
  thrust_to_weight: 0.8
  curves:
    rpm: [1000, 5000, 10000]
    thrust: [50, 600, 2500]
```
